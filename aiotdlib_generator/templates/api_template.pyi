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
    """
    This class contains all TDJson API methods
    """

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
        {%- for parameter in entity.parameters %}
        :param {{ parameter.name }}: {{ parameter.doc }}{% if parameter.nullable %}, defaults to None{% endif %}
        :type {{ parameter.name }}: {{ parameter.doc_type }}{% if parameter.nullable %}, optional{% endif %}
        {% endfor %}
        :param request_id: custom request ID. By default random UUID4 will be generated, defaults to None
        :type request_id: :class:`str`
        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`
        :param skip_validation: when set to `True` request would be send to TDLib unvalidated, defaults to False
        :type skip_validation: :class:`bool`
        {% if entity.return_type_str %}
        :return: response from TDLib
        :rtype: :class:`aiotdlib.api.types.{{ entity.return_type_str }}`
        {%- endif %}
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
