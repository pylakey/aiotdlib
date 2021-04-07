from __future__ import annotations

import os
import re
import shutil
import typing
import urllib.request

from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel, validator

HOME = "generator/api"
DESTINATION = "aiotdlib/api"
NOTICE = "This file has been generated automatically!! Do not change this manually!"

core_types = {
    'int': 'int', 'int32': 'int', 'int53': 'int', 'int64': 'int', 'long': 'int', 'double': 'float',
    'Double': 'float',
    'float': 'float',
    'Int': 'int',
    'string': 'str',
    'str': 'str',
    'Str': 'str',
    'String': 'str',
    'bool': 'bool',
    'boolFalse': 'bool',
    'boolTrue': 'bool',
    'Bool': 'bool',
    # TODO: Bytes in TDLib should be encoded as base64, so they should be stored as str
    'bytes': 'str',
    'Bytes': 'str',
    # 'bytes': 'typing.Union[str, bytes]',
    # 'Bytes': 'typing.Union[str, bytes]',
}
dash_prefix_types = {'json'}

jinja_env = Environment(loader=FileSystemLoader('templates'))


def upper_first(s: str):
    return s[:1].upper() + s[1:]


def lower_first(s: str):
    return s[:1].lower() + s[1:]


def snake_case(s: str):
    if not str:
        return ""

    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    s = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower()


vector_type_regex = re.compile(r"vector<(?P<type>.*)>")
list_type_regex = re.compile(r".*list\[(?P<type>\w+)].*")


class BaseType(BaseModel):
    name: str

    @property
    def snake_name(self) -> str:
        return snake_case(self.name)

    @property
    def lf_name(self) -> str:
        """
        lf - abbreviation of Lower_First
        """
        return lower_first(self.name)

    @property
    def uf_name(self) -> str:
        """
        uf - abbreviation of Upper_First
        """
        return upper_first(self.name)


class Parameter(BaseModel):
    type: str
    name: str
    alias: str = None
    doc: str = ""
    default: str = None

    @validator('name')
    def check_name(cls, name):
        if name in ['json', 'filter', 'type', 'hash']:
            return f"{name}_"

        return name

    @validator('alias', always=True)
    def set_alias(cls, alias, values):
        name = values.get('name').rstrip('_')

        if name in ['json', 'filter', 'type', 'hash']:
            return name

        return None

    @validator('type', pre=True)
    def convert_tl_type(cls, tl_type: str) -> str:
        if not tl_type:
            return ""

        if tl_type in core_types:
            return core_types[tl_type]

        vector_type_match = vector_type_regex.match(tl_type)

        if vector_type_match:
            return f"list[{cls.convert_tl_type(vector_type_match.group('type'))}]"

        return upper_first(tl_type)

    @property
    def is_constructor(self) -> bool:
        return self.import_type is not None

    @property
    def is_vector_type(self) -> bool:
        return "list" in self.type

    @property
    def doc_type(self) -> str:
        if self.is_vector_type:
            return f"(:obj:`{self.type}`)"

        return f"(:class:`{self.type}`)"

    @property
    def import_type(self) -> typing.Optional[str]:
        if self.type in core_types:
            return None

        if self.is_vector_type:
            inner_vector_type = list_type_regex.match(self.type).group('type')

            if inner_vector_type in core_types:
                return None

            return inner_vector_type

        return self.type


class Dependency(BaseModel):
    name: str
    type: str

    def __eq__(self, other):
        if not isinstance(other, Dependency):
            return False

        return self.name == other.name and self.type == other.type

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return str.__hash__(f"{self.name}.{self.type}")


class BaseEntity(BaseType):
    doc: str = ""
    parameters: list[Parameter] = []

    @property
    def has_shadow_names(self) -> bool:
        return any(p.name[-1] == '_' for p in self.parameters)

    @property
    def is_method(self) -> bool:
        return isinstance(self, Method)

    @property
    def is_constructor(self) -> bool:
        return isinstance(self, ConstructorShort)

    @property
    def dependencies(self) -> list[Dependency]:
        return []


class ConstructorShort(BaseEntity):
    is_abstract: bool = False


class Constructor(ConstructorShort):
    subclasses: list[Constructor] = []
    cross_deps: list[Constructor] = []
    parent_class: typing.Optional[ConstructorShort] = None

    @property
    def has_shadow_names(self) -> bool:
        for s in self.subclasses:
            for p in s.parameters:
                if "_" in p.name:
                    return True

        for cd in self.cross_deps:
            for p in cd.parameters:
                if "_" in p.name:
                    return True

        return super(Constructor, self).has_shadow_names

    @property
    def dependencies(self) -> list[Dependency]:
        deps = set()
        cross_deps = [c.name for c in self.cross_deps]

        for p in self.parameters:
            if bool(p.import_type) and not bool(p.import_type) in cross_deps:
                deps.add(Dependency(name=snake_case(p.import_type), type=p.import_type))

        for subclass in self.subclasses:
            for p in subclass.parameters:
                if (
                        bool(p.import_type)
                        and p.import_type != self.uf_name
                        and upper_first(p.import_type) not in cross_deps
                ):
                    deps.add(Dependency(
                        name=snake_case(p.import_type),
                        type=p.import_type
                    ))

        for dep in self.cross_deps:
            for p in dep.parameters:
                if bool(p.import_type) and p.import_type != self.uf_name:
                    deps.add(Dependency(
                        name=snake_case(p.import_type),
                        type=p.import_type
                    ))

        return list(sorted(deps, key=lambda x: x.name))


class Method(BaseEntity):
    return_type: typing.Union[str, Constructor]

    @validator('return_type', pre=True)
    def _convert_return_type(cls, return_type: typing.Union[str, Constructor]) -> typing.Union[str, Constructor]:
        if not return_type:
            return ""

        if isinstance(return_type, str):
            if return_type in core_types:
                return core_types[return_type]
            else:
                raise ValueError

        return return_type

    @property
    def return_type_str(self) -> str:
        return self.return_type if isinstance(self.return_type, str) else self.return_type.uf_name

    @property
    def dependencies(self) -> list[Dependency]:
        deps = set()

        for p in self.parameters:
            if p.import_type is not None:
                deps.add(Dependency(
                    name=snake_case(p.import_type),
                    type=p.import_type
                ))

        return list(sorted(deps, key=lambda x: x.name))


BaseEntity.update_forward_refs()
Constructor.update_forward_refs()


def parse_tl_schema(file_path: str = None) -> list[typing.Union[Constructor, Method]]:
    abstract_class_docs_regex = re.compile(r"^//@class (?P<name>[^@]*) @description (?P<description>.*)$")
    description_regex = re.compile(r"^//@description (?P<description>.*)$")
    parameter_description_regex = re.compile(r"^//@(?P<name>.*?) (?P<description>.*)$")
    entity_regex = re.compile(r'^(?P<name>\w+)\s(?P<args>(?:.*))=\s(?P<return_type>\w+);$')
    args_regex = re.compile(r"(?P<name>\w+):(?P<type>[\w<>]+)")

    try:
        scheme = urllib.request.urlopen(
            "https://raw.githubusercontent.com/tdlib/td/master/td/generate/scheme/td_api.tl"
        ).read().decode('utf-8')
    except:
        if file_path is None:
            raise ValueError('Unable to receive schema on Github and file_path is not set!')

        with open(file_path, encoding='utf-8') as f:
            scheme = f.read()

    # Some cleaning for better parsing
    inline_parameter_regex = re.compile(r'(?!(@description|@class))(@\w+)')
    empty_slashes_regex = re.compile(r'\n//\s*$', re.MULTILINE)

    scheme = scheme.replace('\n//-', ' ')
    scheme = inline_parameter_regex.sub(r'\n//\2', scheme)
    scheme = scheme.replace('////', '//')
    scheme = empty_slashes_regex.sub('', scheme)

    methods = {}
    constructors = {}
    is_functions_section = False
    current_entity_description: str = ""
    current_entity_params_descriptions: dict[str, str] = {}

    for line in [line.strip() for line in scheme.splitlines()[14:] if len(line) > 0]:
        # After line '---functions---' only methods are described
        if line == '---functions---':
            is_functions_section = True
            continue

        abstract_class_match = abstract_class_docs_regex.match(line)

        # Abstract classes presented as
        # //@class <ClassName> @description <description>
        if bool(abstract_class_match):
            class_name = upper_first(abstract_class_match.group('name'))
            class_description = abstract_class_match.group('description')
            constructors[class_name] = Constructor(
                name=class_name,
                doc=class_description,
                is_abstract=True
            )
            continue

        description_match = description_regex.match(line)

        if bool(description_match):
            current_entity_description = description_match.group('description')
            continue

        parameter_description_match = parameter_description_regex.match(line)

        if bool(parameter_description_match):
            param_name = parameter_description_match.group('name')
            param_description = parameter_description_match.group('description')
            current_entity_params_descriptions[param_name] = param_description
            continue

        entity_match = entity_regex.match(line)

        if bool(entity_match):
            entity_name = upper_first(entity_match.group('name'))
            entity_return_type = upper_first(entity_match.group('return_type'))
            entity_uf_return_type = upper_first(entity_return_type)
            entity_parameters: list[Parameter] = []

            for arg_name, arg_type in args_regex.findall(entity_match.group('args')):
                if arg_name in ['description', 'class']:
                    arg_name = f'param_{arg_name}'

                arg_description = current_entity_params_descriptions.get(arg_name)
                entity_parameters.append(Parameter(
                    name=arg_name,
                    type=arg_type,
                    doc=arg_description,
                ))

            if is_functions_section:
                methods[entity_name] = Method(
                    name=entity_name,
                    doc=current_entity_description,
                    parameters=entity_parameters,
                    return_type=(
                        constructors[entity_uf_return_type]
                        if entity_uf_return_type in constructors
                        else entity_return_type
                    )
                )
            else:
                if entity_uf_return_type in constructors:
                    parent = constructors[entity_uf_return_type]
                    entity = Constructor(
                        name=entity_name,
                        doc=current_entity_description,
                        parameters=entity_parameters,
                        parent_class=ConstructorShort(
                            name=parent.name,
                            doc=parent.doc,
                            parameters=parent.parameters,
                            is_abstract=parent.is_abstract
                        ),
                    )
                    parent.subclasses.append(entity)
                else:
                    constructors[entity_name] = Constructor(
                        name=entity_name,
                        doc=current_entity_description,
                        parameters=entity_parameters,
                    )

            current_entity_params_descriptions = {}
            current_entity_description = ""
            continue

        raise RuntimeError('Something goes wrong!')

    # Separately process cross-dependencies to avoid circular import error
    cross_deps: dict[str, set[str]] = {}

    for constructor in sorted(constructors.values(), key=lambda x: x.name):
        for parameter in constructor.parameters:
            parameter_constructor = constructors.get(parameter.import_type)

            # Skip core types
            if not bool(parameter_constructor):
                continue

            # Skip subclasses as they will be checked above in parent class processing
            if bool(parameter_constructor.parent_class):
                continue

            # Check parameters of constructor parameters
            for p in parameter_constructor.parameters:
                if p.import_type == constructor.name:
                    if parameter.import_type not in cross_deps:
                        cross_deps[constructor.name] = set()

                    cross_deps[constructor.name].add(constructor.name)

            # Check parameter constructor subclasses' parameters
            for subclass in parameter_constructor.subclasses:
                for subclass_parameter in subclass.parameters:
                    if subclass_parameter.import_type == constructor.name:
                        if parameter.import_type not in cross_deps:
                            cross_deps[parameter.import_type] = set()

                        cross_deps[parameter.import_type].add(constructor.name)

    for constructor_name, cross_deps_constructors_names in cross_deps.items():
        for name in cross_deps_constructors_names:
            dep_constructor = constructors.pop(name)
            constructors[constructor_name].cross_deps.append(dep_constructor)

    methods_list: list[Method] = list(methods.values())
    constructors_list: list[Constructor] = list(constructors.values())

    # Sorting subclasses and cross_deps lists
    for constructor in constructors_list:
        constructor.subclasses.sort(key=lambda x: x.name)
        constructor.cross_deps.sort(key=lambda x: x.name)

    return list(sorted([*methods_list, *constructors_list], key=lambda x: x.name))


def prepare_directories():
    types_dir = f"{DESTINATION}/types/"
    functions_dir = f"{DESTINATION}/functions/"
    shutil.rmtree(types_dir, ignore_errors=True)
    shutil.rmtree(functions_dir, ignore_errors=True)
    os.makedirs(types_dir, exist_ok=True)
    os.makedirs(functions_dir, exist_ok=True)


def start():
    prepare_directories()
    entities: list[typing.Union[Method, Constructor]] = parse_tl_schema(f'{HOME}/source/td_api.tl')

    class_template = jinja_env.get_template('class_template.pyi')
    api_template = jinja_env.get_template('api_template.pyi')
    section_init_file_template = jinja_env.get_template('section_init_template.pyi')
    package_init_file_template = jinja_env.get_template('package_init_template.pyi')

    types_entities = [e for e in entities if not e.is_method]
    functions_entities = [e for e in entities if e.is_method]

    with open(f"{DESTINATION}/types/__init__.py", "w", encoding="utf-8") as f:
        f.write(section_init_file_template.render(notice=NOTICE, entities=types_entities))

    with open(f"{DESTINATION}/functions/__init__.py", "w", encoding="utf-8") as f:
        f.write(section_init_file_template.render(notice=NOTICE, entities=functions_entities))

    with open(f"{DESTINATION}/api.py", "w", encoding="utf-8") as f:
        f.write(api_template.render(notice=NOTICE, entities=entities))

    with open(f"{DESTINATION}/__init__.py", "w", encoding="utf-8") as f:
        f.write(package_init_file_template.render(notice=NOTICE, entities=entities))

    for entity in entities:
        section = "functions" if entity.is_method else "types"

        with open(f"{DESTINATION}/{section}/{entity.snake_name}.py", 'w', encoding='utf-8') as f:
            f.write(class_template.render(notice=NOTICE, entity=entity))


if __name__ == '__main__':
    HOME = "."
    DESTINATION = "../../aiotdlib/api"
    start()
