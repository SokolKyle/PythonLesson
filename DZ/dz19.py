import re
#Решил сделать через input, что бы пользователь мог вводить любой текст и программа будет искать только адреса в нем.
#Текст для проверки
#Привет. Меня зовут Николай. Мне 31 год. Мой электронный адрес: sokoloffKyle@mail.ru
#123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-3@.ru, login.3-67@i.ru, 1login@ru.name.ru

text_user = input("Введите текст: ")
e_mail = re.findall(r'[.\-\w]+@[.\w]+', text_user)
print(e_mail)