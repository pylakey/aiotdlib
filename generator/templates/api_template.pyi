{{ '# ' + "=" * (notice.__len__() + 6) + " #"}}
{{ '# ' + " " * (notice.__len__() + 6) + " #"}}
#    {{ notice }}    #
{{ '# ' + " " * (notice.__len__() + 6) + " #"}}
{{ '# ' + "=" * (notice.__len__() + 6) + " #"}}

import typing

from .functions import *
from .types import *
from .base_object import BaseObject

if typing.TYPE_CHECKING:
    from aiotdlib.client import Client

ReturnType = typing.TypeVar('ReturnType', bound=BaseObject)


class API:
    class Types:
        # Types and Functions
        ANY = '*'
        {%- for entity in entities %}
        {{ entity.snake_name.upper() }} = '{{ entity.lf_name }}'
        {%- for subclass in entity.subclasses %}
        {{ subclass.snake_name.upper() }} = '{{ subclass.lf_name }}'
        {%- endfor %}
        {%- endfor %}

    def __init__(self, client: 'Client'):
        self.client = client
    {% for entity in entities if entity.is_function %}
    async def {{ entity.snake_name }}{% if entity.parameters %}(
            self,
            {%- for parameter in entity.parameters %}
            {{ parameter.name }}: {% if parameter.nullable %}{{ parameter.optional_type }}{% else %}{{ parameter.type }}{% endif %},
            {%- endfor %}
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ){%- else %}(self, *, request_id: str = None, request_timeout: int = None){% endif %} -> {{ entity.return_type_str }}:
        """
        {{ entity.doc }}
        {% if entity.parameters %}
        Params:
            {%- for parameter in entity.parameters %}
            {{ parameter.name }} {{ parameter.doc_type }}
                {{ parameter.doc }}
            {% endfor %}
        {%- endif %}
        """

        {%- if entity.parameters %}
        _constructor = {{ entity.uf_name }}.construct if skip_validation else {{ entity.uf_name }}
        {% endif %}
        return await self.client.request(
            {% if entity.parameters %}_constructor(
                {%- for parameter in entity.parameters %}
                {{ parameter.name.rstrip('_') }}={{ parameter.name }},
                {%- endfor %}
            ){% else %}{{ entity.uf_name }}(){% endif %},
            request_id=request_id,
            request_timeout=request_timeout,
        )
    {% endfor %}
