# from jinja2 import Template
#
# # name = "Игорь"
# # age = 28
# #
# # tm = Template("Мне {{ a*2 }} лет. Меня зовут {{n.upper()}}.")
# # msg = tm.render(n=name, a=age)
# #
# # print(msg)
#
# # per = {'name': "Игорь", 'age': 28}
# #
# # tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.name }}.")
# # msg = tm.render(p=per)
# #
# # print(msg)
#
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def get_name(self):
# #         return self.name
# #
# #
# # per = Person("Игорь", 28)
# #
# # tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.get_name() }}.")
# # msg = tm.render(p=per)
# #
# # print(msg)
#
# # cities = [
# #     {'id': 1, 'city': 'Москва'},
# #     {'id': 2, 'city': 'Смоленск'},
# #     {'id': 3, 'city': 'Нягань'},
# #     {'id': 4, 'city': 'Киров'},
# #     {'id': 5, 'city': 'Сочи'}
# # ]
# #
# # link = """<select>
# # {% for c in cities -%}
# #     {%- if c.id > 3 -%}
# #     <option value="{{ c.id }}">{{ c['city']}}</option>
# #     {% elif c.city = "Москва" %}
# #     <option>{{ c['city']}}</option>
# #     {% else -%}
# #     {{ c['city'] }}
# #     {% endif -%}
# # {% endfor -%}
# # </select>"""
# #
# # tm = Template(link)
# # msg = tm.render(cities=cities)
# #
# # print(msg)
#
# # hr = [
# #     {'a': "index", 't': "Главная"},
# #     {'a': "news", 't': "Новости"},
# #     {'a': "about", 't': "компании"},
# #     {'a': "shop", 't': "Магазин"},
# #     {'a': "contacts", 't': "Контакты"}
# # ]
# #
# # link = """
# # <ul>
# #     {% for item in path %}
# #         {% if item.url == 'index' %}
# #         <li><a href="/{{ hr.a }}" class='active'>{{ hr.t }}</a></li>
# #         {% else %}
# #         <li><a href="/{{ hr.a }}">{{ hr.t }}</a></li>
# #         {% endif %}
# #     {% endfor %}
# # </ul>
# # """
# # tm = Template(link)
# # msg = tm.render(hr=hr)
# #
# # print(msg)
#
#
# # cars = [
# #     {'model': 'Audi', 'price': 23000},
# #     {'model': 'Skoda', 'price': 17300},
# #     {'model': 'Renault', 'price': 44300},
# #     {'model': 'Wolksvagen', 'price': 21300}
# # ]
# #
# # tpl = "Сумма: {{ cs | sum(attribute='price')}}"
# #
# # tm = Template(tpl)
# # msg = tm.render(cs=cars)
# #
# # print(msg)
#
#
# # cars = [
# #     {'model': 'Audi', 'price': 23000},
# #     {'model': 'Skoda', 'price': 17300},
# #     {'model': 'Renault', 'price': 44300},
# #     {'model': 'Wolksvagen', 'price': 21300}
# # ]
# #
# # # tpl = "MAX: {{ (cs | max(attribute='price')).model}}"
# # # tpl = "MIN: {{ (cs | min(attribute='price')).model}}"
# # # tpl = "RANDOM: {{ cs | random}}"
# # # tpl = "REPLACE: {{ cs | replace('model', 'brand')}}"
# #
# # tm = Template(tpl)
# # msg = tm.render(cs=cars)
# #
# # print(msg)
#
#
# # html = """
# # {% macro fun_input(name, value='', type='text', size=20) %}
# #     <input type="{{ type }}" name="{{ name }}" value = "{{ value }}" size= "{{ size }}">
# # {% endmacro %}
# #
# # <p>{{ fun_input('username')}}</p>
# # <p>{{ fun_input('email')}}</p>
# # <p>{{ fun_input('password', type="password")}}</p>
# # """
# #
# # tm = Template(html)
# # msg = tm.render()
# #
# # print(msg)


from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": "Алексей", "year": 18, "weight": 78.5},
    {"name": "Никита", "year": 28, "weight": 82.3},
    {"name": "Виталий", "year": 33, "weight": 94.0}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('index.html')
msg = tm.render(users=persons)

print(msg)
