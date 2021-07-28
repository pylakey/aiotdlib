{{ '# ' + "=" * (notice.__len__() + 6) + " #"}}
{{ '# ' + " " * (notice.__len__() + 6) + " #"}}
#    {{ notice }}    #
{{ '# ' + " " * (notice.__len__() + 6) + " #"}}
{{ '# ' + "=" * (notice.__len__() + 6) + " #"}}

{% for entity in entities -%}
{%- if entity.subclasses -%}
from .{{ entity.snake_name }} import (
    {{ entity.uf_name }},
    {%- for subclass in entity.subclasses %}
    {{ subclass.uf_name }},
    {%- endfor %}
    {%- for dep in entity.cross_deps %}
    {{ dep.uf_name }},
    {%- endfor %}
)
{% else -%}
from .{{ entity.snake_name }} import {{ entity.uf_name }}
{% endif %}
{%- endfor %}

__all__ = [
    {%- for entity in entities %}
    "{{ entity.uf_name }}",
    {%- for subclass in entity.subclasses %}
    "{{ subclass.uf_name }}",
    {%- endfor %}
    {%- for dep in entity.cross_deps %}
    "{{ dep.uf_name }}",
    {%- endfor %}
    {%- endfor %}
]

