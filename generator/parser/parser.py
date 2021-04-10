import logging
import re
import typing
import urllib.request

from .entities import Constructor, ConstructorShort, Method, Parameter
from .utils import upper_first


class Parser:
    def __init__(self, file_path: str = None):
        self.file_path = file_path

    def parse(self) -> list[typing.Union[Constructor, Method]]:
        abstract_class_docs_regex = re.compile(r"^//@class (?P<name>[^@]*) @description (?P<description>.*)$")
        description_regex = re.compile(r"^//@description (?P<description>.*)$")
        parameter_description_regex = re.compile(r"^//@(?P<name>.*?) (?P<description>.*)$")
        entity_regex = re.compile(r'^(?P<name>\w+)\s(?P<args>.*)=\s(?P<return_type>\w+);$')
        args_regex = re.compile(r"(?P<name>\w+):(?P<type>[\w<>]+)")
        param_length_constraint = re.compile(r"(?P<min_length>\d+)-(?P<max_length>\d+) characters")
        nullability_constraint = re.compile(r".*may be null.*")

        try:
            scheme = urllib.request.urlopen(
                "https://raw.githubusercontent.com/tdlib/td/master/td/generate/scheme/td_api.tl"
            ).read().decode('utf-8')
        except Exception as e:
            logging.error(f"Unable to retrieve tl schema from github {e}")

            if self.file_path is None:
                raise RuntimeError('Unable to receive schema on Github and file_path is not set!')

            with open(self.file_path, encoding='utf-8') as f:
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
                    arg_nullable = False
                    arg_min_length = None
                    arg_max_length = None

                    if ";" in arg_description:
                        # Parsing parameter constraints
                        # https://github.com/tdlib/td/issues/1016#issuecomment-618959102
                        for c in arg_description.split(";"):
                            c = c.strip()

                            if nullability_constraint.match(c):
                                arg_nullable = True

                            param_length_constraint_match = param_length_constraint.match(c)

                            if bool(param_length_constraint_match):
                                arg_min_length = int(param_length_constraint_match.group('min_length'))

                                if arg_min_length == 0:
                                    arg_nullable = True

                                arg_max_length = int(param_length_constraint_match.group('max_length'))

                    entity_parameters.append(Parameter(
                        name=arg_name,
                        type=arg_type,
                        doc=arg_description,
                        nullable=arg_nullable,
                        min_length=arg_min_length,
                        max_length=arg_max_length,
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
