from jinja2 import Template

html = """
{%- macro input(name, placeholder, type='text') -%}
    <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
{%- endmacro %}

<p>{{ input('firstname', 'Имя') }}</p>
<p>{{ input('lastname', 'Фамилия') }}</p>
<p>{{ input('address', 'Адрес') }}</p>
<p>{{ input('phone', 'Телефон', type="tel") }}</p>
<p>{{ input('email', 'Почта', type="email") }}</p>
"""

tm = Template(html)
msg = tm.render()

print(msg)