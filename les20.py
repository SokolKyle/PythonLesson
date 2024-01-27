import re

# # s = '<p>Изображение <img src="bg.jpg"> - фон страницы</p>'
# s = '<p>Изображение <img  alt="картинка" src="bg.jpg"> - фон страницы</p>'
# # reg = r'<img.*?>'
# # reg = r'<img[^>]*>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# text = "Python (в русском языке встречаются названия пито́н[16]или па́йтон[17]) — высокоуровневый язык " \
#        "программирования общего назначения с динамической строгой типизацией " \
#        "и автоматическим управлением памятью[18][19]."
#
# # reg = r'\[\d+\]'
# reg = r'\[.*?]'
# print(re.findall(reg, text))

# s = 'Петр, Ольга и Виталий отлично учатся!'
# reg = 'Петр|Виктор|Ольга'
# print(re.findall(reg, s))

# s = 'int = 4, float = 42.0f, double = 8.0'
# # reg = r'\w+\s*=\s*\d[.\w]*'
# # reg = r'(?:int|float)\s*=\s*\d[.\w]*'
# reg = r'((int|float)\s*=\s*(\d[.\w]*))'
# print(re.findall(reg, s))
# print(re.search(reg, s).group())
#
# # (?: ....) - это группирующая скобка является не сохраняющая

# # s = '127.0.0.1'
# s = '127.168.255.255'
# # pattern = r'(\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3})'
# pattern = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(pattern, s))

# s = '5 + 7*2 - 4'
# reg = r'\s*(?:[+*-])\s*'
# print(re.split(reg, s))

# a = '28-08-2021'
# # pattern = '[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]'
# # pattern = '[0-2][0-9]|3[0-1]-[0-9][0-9]-[0-9][0-9][0-9][0-9]'
# pattern = '(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[1-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(pattern, a))

# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта.'
# reg = r'([0-9]+)\s(\D+)'
# # print(re.findall(reg, s))
# # print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])

text = """
Самара
Москва
Тверь
Уфа
Казань
"""
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f'<piton value="{count}">{m.group(1)}</option>\n'
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))

# s = "<p>Изображение <img src='bg.jpg\" alt='картинка'> - фон страницы </p>"
# reg = f"<img\s+[^>]*src\s*=(?P<q>['\"])(.+?)(?P=q)>"
# print(re.findall(reg, s))

# s = 'Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024.'  # 23.10.2024
# pattern = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(pattern, r'\2-\1-\3', s))

# s = 'yandex.com and yandex.ru'
# pattern = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(pattern, r'http://\1', s, re.IGNORECASE))
















