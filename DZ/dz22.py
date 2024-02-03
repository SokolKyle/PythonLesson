# Функция для чтения текстового файла и возврата содержимого как список строк
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()


# Функция для записи списка строк в текстовый файл
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)


# Исходные строки с текстом
text_lines = [
    'Замена строки в текстовом файле;\n',
    'изменить строку в списке;\n',
    'записать список в файл;\n'
]

# Записываем исходные строки в файл
write_file('dz22.txt', text_lines)

# Предлагаем пользователю выбор строк которые нужно поменять
pos1 = int(input('Введите номер первой строки для замены: ')) - 1
pos2 = int(input('Введите номер второй строки для замены: ')) - 1

# Проверка введенных номеров строк
if pos1 < 0 or pos2 < 0 or pos1 >= len(text_lines) or pos2 >= len(text_lines):
    print('Таких строк не существует.')
else:
    # Меняем выбранные строки местами
    text_lines[pos1], text_lines[pos2] = text_lines[pos2], text_lines[pos1]

    # Перезаписываем файл с измененными строками
    write_file('dz22.txt', text_lines)
    print('Строки успешно поменяли местами в файле.')
