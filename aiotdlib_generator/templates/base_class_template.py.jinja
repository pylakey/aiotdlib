{% macro class(entity, parent='BaseObject') -%}
class {{ entity.uf_name }}({{ parent }}):
    """
    {{ entity.doc }}
    {% if entity.parameters %}
    {%- for parameter in entity.parameters %}
    :param {{ parameter.name }}: {{ parameter.doc }}{% if parameter.nullable %}, defaults to None{% endif %}
    :type {{ parameter.name }}: {{ parameter.doc_type }}{% if parameter.nullable %}, optional{% endif %}
    {% endfor -%}
    {% endif %}
    """

    ID: str = Field("{{ entity.lf_name }}", alias="@type")
    {%- for parameter in entity.parameters %}
    {%- if parameter.alias or parameter.has_constraints %}
    {{ parameter.name }}: {% if parameter.nullable %}{{ parameter.optional_type }}{% else %}{{ parameter.type }}{% endif %} = Field(
        {%- if parameter.nullable %}None{% else %}...{% endif %}
        {%- if parameter.alias %}, alias='{{ parameter.alias }}'{% endif %}
        {%- if parameter.min_length %}, min_length={{ parameter.min_length }}{% endif %}
        {%- if parameter.max_length %}, max_length={{ parameter.max_length }}{% endif -%}
    )
    {%- else %}
    {{ parameter.name }}: {% if parameter.nullable %}{{ parameter.optional_type }}{% else %}{{ parameter.type }}{% endif %}{% if parameter.nullable %} = None{% endif %}
    {%- endif %}
    {%- endfor %}

    {% if not entity.is_abstract -%}
    @staticmethod
    def read(q: dict) -> {{ entity.uf_name }}:
        return {{ entity.uf_name }}.construct(**q)
{% endif %}
{%- endmacro %}