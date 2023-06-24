from __future__ import annotations

import os
import pathlib
import shutil
import typing

from jinja2 import (
    Environment,
    FileSystemLoader,
)

from .parser import (
    Constructor,
    Function,
    TDApiParser,
)

Entities = list[typing.Union[Constructor, Function]]

LIBRARY_ROOT_PATH = str(pathlib.Path(__file__).parent.parent)


class Generator:
    def __init__(
            self,
            destination: str = f"{LIBRARY_ROOT_PATH}/aiotdlib/api",
            notice: str = "This file has been generated automatically!! Do not change this manually!",
    ):
        self.notice = notice
        self.destination = destination
        self.jinja_env = Environment(
            loader=FileSystemLoader(f'{pathlib.Path(__file__).parent}/templates'),
            # trim_blocks=True,
            # lstrip_blocks=True
        )

    def __prepare_directories(self):
        functions_dir = f"{self.destination}/functions/"
        shutil.rmtree(functions_dir, ignore_errors=True)
        os.makedirs(functions_dir, exist_ok=True)

    def render_types_init_file(self, entities: Entities):
        section_init_file_template = self.jinja_env.get_template('types_package_init_template.py.jinja2')

        with open(f"{self.destination}/types/__init__.py", "w", encoding="utf-8") as f:
            f.write(
                section_init_file_template.render(
                    notice=self.notice,
                    entities=[e for e in entities if e.is_constructor]
                )
            )

    def render_functions_init_file(self, entities: Entities):
        section_init_file_template = self.jinja_env.get_template('functions_package_init_template.py.jinja2')

        with open(f"{self.destination}/functions/__init__.py", "w", encoding="utf-8") as f:
            f.write(
                section_init_file_template.render(
                    notice=self.notice,
                    entities=[e for e in entities if e.is_function]
                )
            )

    def render_package_init_file(self, entities: Entities):
        package_init_file_template = self.jinja_env.get_template('package_init_template.py.jinja2')

        with open(f"{self.destination}/__init__.py", "w", encoding="utf-8") as f:
            f.write(package_init_file_template.render(notice=self.notice, entities=entities))

    def render_types(self, entities: Entities):
        class_template = self.jinja_env.get_template('types_template.py.jinja2')
        entities = [e for e in entities if not e.is_function]

        with open(f"{self.destination}/types/all.py", 'w', encoding='utf-8') as f:
            f.write(class_template.render(notice=self.notice, entities=entities))

    def render_functions(self, entities: Entities):
        class_template = self.jinja_env.get_template('functions_template.py.jinja2')
        entities = [e for e in entities if e.is_function]

        for entity in entities:
            with open(f"{self.destination}/functions/{entity.snake_name}.py", 'w', encoding='utf-8') as f:
                f.write(class_template.render(notice=self.notice, entity=entity))

    def render_main_api_class(self, entities: Entities):
        api_template = self.jinja_env.get_template('api_template.py.jinja2')

        with open(f"{self.destination}/api.py", "w", encoding="utf-8") as f:
            f.write(api_template.render(notice=self.notice, entities=entities))

    def generate(self):
        self.__prepare_directories()

        entities = TDApiParser.parse()

        self.render_types(entities)
        self.render_types_init_file(entities)
        self.render_functions(entities)
        self.render_functions_init_file(entities)
        self.render_main_api_class(entities)
        self.render_package_init_file(entities)

        os.system(f'black -l 120 {self.destination}')
