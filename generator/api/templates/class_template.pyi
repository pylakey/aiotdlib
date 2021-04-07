{{ '# ' + "=" * (notice.__len__() + 6) + " #"}}
{{ '# ' + " " * (notice.__len__() + 6) + " #"}}
#    {{ notice }}    #
{{ '# ' + " " * (notice.__len__() + 6) + " #"}}
{{ '# ' + "=" * (notice.__len__() + 6) + " #"}}
from __future__ import annotations

from pydantic import Field

{% for d in entity.dependencies -%}
from {% if entity.is_method %}..types{% else %}.{{ d.name }}{% endif %} import {{ d.type }}
{% endfor -%}
from ..base_object import BaseObject


class {{ entity.uf_name }}(BaseObject):
    """
    {{ entity.doc }}
    {% if entity.parameters %}
    Params:
        {%- for parameter in entity.parameters %}
        {{ parameter.name }} {{ parameter.doc_type }}
            {{ parameter.doc }}
        {% endfor -%}
    {% endif %}
    """

    ID: str = Field("{{ entity.lf_name }}", alias="@type")
    {%- for parameter in entity.parameters %}
    {%- if parameter.alias %}
    {{ parameter.name }}: {{ parameter.type }} = Field(..., alias='{{ parameter.alias }}')
    {%- else %}
    {{ parameter.name }}: {{ parameter.type }}
    {%- endif %}
    {%- endfor %}

    {% if not entity.is_abstract -%}
    @staticmethod
    def read(q: dict) -> {{ entity.uf_name }}:
        return {{ entity.uf_name }}.construct(**q)
    {%- endif -%}

{% for subclass in entity.subclasses %}
class {{ subclass.uf_name }}({{entity.uf_name}}):
    """
    {{ subclass.doc }}
    {% if subclass.parameters %}
    Params:
        {%- for parameter in subclass.parameters %}
        {{ parameter.name }} {{ parameter.doc_type }}
            {{ parameter.doc }}
        {% endfor %}
    {%- endif %}
    """

    ID: str = Field("{{ subclass.lf_name }}", alias="@type")
    {%- for parameter in subclass.parameters %}
    {%- if parameter.alias %}
    {{ parameter.name }}: {{ parameter.type }} = Field(..., alias='{{ parameter.alias }}')
    {%- else %}
    {{ parameter.name }}: {{ parameter.type }}
    {%- endif %}
    {%- endfor %}

    @staticmethod
    def read(q: dict) -> {{ subclass.uf_name }}:
        return {{ subclass.uf_name }}.construct(**q)

{% endfor -%}
{%- for dep in entity.cross_deps %}
class {{ dep.uf_name }}(BaseObject):
    """
    {{ dep.doc }}
    {% if dep.parameters %}
    Params:
        {%- for parameter in dep.parameters %}
        {{ parameter.name }} {{ parameter.doc_type }}
            {{ parameter.doc }}
        {% endfor -%}
    {% endif %}
    """

    ID: str = Field("{{ dep.lf_name }}", alias="@type")
    {%- for parameter in dep.parameters %}
    {%- if parameter.alias %}
    {{ parameter.name }}: {{ parameter.type }} = Field(..., alias='{{ parameter.alias }}')
    {%- else %}
    {{ parameter.name }}: {{ parameter.type }}
    {%- endif %}
    {%- endfor %}

    {% if not dep.is_abstract -%}
    @staticmethod
    def read(q: dict) -> {{ dep.uf_name }}:
        return {{ dep.uf_name }}.construct(**q)
    {%- endif %}
{%- endfor %}

