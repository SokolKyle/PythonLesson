import re

# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198765 Hello[-World]'
# reg = r'[a-zA-z]\[-]'
#
# print(re.findall(reg, s))

# st = 'Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты в диапазоне от 00 до 59. 2021-06-15Т01:09'
# req = r'[0-9][0-9]:[0-9][0-9]'  # Но пройдет 99:99
# req = r'[0-9]{2}:[0-9]{2}'
# req = r'[0-2][0-9]:[0-9][0-9]'  # Но пройдет 29:99
# req = r'[0-2][0-9]:[0-5][0-9]'  # Но пройдет 29:99
# req = r'.'  # Искать один любой символ.
# req = r'\.'  # Экранирует точку для поиска именно точки.
# req = r'[.]'  # Экранирует точку для поиска именно точки.
# req = r'[.a-z]'  # Искать либо, точку, либо любой символ алфавита в нижнем регистре.
# req = r'\d'  # Искать только цифры.
# req = r'\D'  # Искать все кроме цифр.
# req = r'\s'  # Искать пробел.
# req = r'\S'  # Искать все кроме пробела.
# req = r'\w'  # Искать цифры, символы и пробел.
# req = r'\W'  # Искать все цифр, символов и пробела.
# req = r'\A...'  # Искать в начале строки.
# req = r'...\Z'  # Искать в конце строки.
# req = r'...\b'  # Искать по границе элемента.
# req = r'\b...'  # Искать по границе элемента.
# req = r'...\B'  # Искать по границе элемента не начинающихся с символов.
# req = r'\B...'  # Искать по границе элемента не начинающихся с символов.

# d = 'Цифры: 7, +17, --42, 0013, 0.3'
# print(re.findall(r'[+-]?\d+[\.\d]*', d))
# req = r'20+'  # От нуля до любого количества - элемента может не быть.
# req = r'20*'  # От одного до любого количества - элемент присутствовать должен обязательно хотя бы один раз.
# print(re.findall(req, st))

# st = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub(r'#.*', '', st))
# print('Дата рождения:', re.sub(r'#.*', '', st).replace('-','.'))
# print('Дата рождения:', re.sub('-', '.', re.sub(r'#.*', '', st)))
# print('Дата рождения:', re.sub(r'\s#.*', '', st))
# st = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub(r'-', '.', re.search(r'\d{2}-\d{2}-\d{4}', st)[0]))

# st = 'author=Пушкин А. С.; title = Евгений Онегин; price =200; year= 1831'
# req = r'\w+\s*=\s*[^;]*'
# print(re.findall(req, st))

# st = '12 сетября 2021 года'
# req = r'\d{2,4}'
# print(re.findall(req, st))

# st = '+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578'
# # req = r'[+]?7\d*'
# req = r'\+?7[^\s]*\d'
# print(re.findall(req, st))


# def valid_login(name):
#     return re.findall(r'^[A-za-z0-9_-]{6,16}$', name)  # от 6 до 16, английские буквы, _, -, 0-9
#
#
# print(valid_login('Python_master'))
# print(valid_login('!!!!!Python'))
# print(valid_login('Python!!!!!!'))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = 'hello world'
# # print(re.findall(r'\w+', text))
# print(re.findall(r'\w\+', text, re.DEBUG))

# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198765 Hello[-World]'
# reg = r'я'
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))
# print(re.findall('one$', text))
# print(re.findall('one$', text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+  # part1
# @         # @
# [a-z.-]+  # part2
# """, 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = '(?im)^python'
# print(re.findall(reg, text))


