tpl = tuple(input('Введите по порядку, без пробелов, элементы кортежа: '))
lst = []
print(tpl)
for num in tpl:
    if num not in lst:
        lst.append(num)
        count = tpl.count(num)
        print('Количество', num, '=', count)
