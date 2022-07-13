{{ '# ' + "=" * (notice.__len__() + 6) + " #"}}
{{ '# ' + " " * (notice.__len__() + 6) + " #"}}
#    {{ notice }}    #
{{ '# ' + " " * (notice.__len__() + 6) + " #"}}
{{ '# ' + "=" * (notice.__len__() + 6) + " #"}}

from enum import Enum

from .api import API
from .base_object import BaseObject
from .errors import *
from .functions import *
from .types import *

BaseObject._all = {
    {%- for entity in entities if entity.is_constructor %}
    '{{ entity.lf_name }}': {{ entity.uf_name }},
    {%- for subclass in entity.subclasses %}
    '{{ subclass.lf_name }}': {{ subclass.uf_name }},
    {%- endfor %}
    {%- endfor %}
}

__all__ = [
    'AioTDLibError',
    'BadRequest',
    'NotFound',
    'Unauthorized',
    'API',
    'BaseObject',

    # Types and Functions
    {%- for entity in entities %}
    '{{ entity.uf_name }}',
    {%- for subclass in entity.subclasses %}
    '{{ subclass.uf_name }}',
    {%- endfor %}
    {%- endfor %}
]

