import os


def scan_directory(directory):
    for item in os.listdir(directory):
        # Получаем путь к текущему объекту
        item_path = os.path.join(directory, item)
        # Определяем тип текущего объекта (файл/директория)
        item_type = "file" if os.path.isfile(item_path) else "dir"
        item_info = f"{item} - {item_type}"

        if os.path.isfile(item_path):  # Если объект - файл, то добавляется его размер
            item_size = os.path.getsize(item_path)
            item_info += f" - {item_size} bytes"

        print(item_info)


# Здесь нужно указать путь к директории
directory_path = r"C:\Users\Учебная\Desktop\виртуалка\pyt"
scan_directory(directory_path)
