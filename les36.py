# import csv
#
# with open('data2.csv', encoding='utf-8') as file:
#     file_reader = csv.reader(file, delimiter=',')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы {", ".join(row)}')
#         else:
#             print(f'{row[0]} - {row[1]}. Родился в {row[2]}')
#         count += 1

import csv
# import json
#
# with open('data3.csv') as f:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         count += 1

# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("data_new.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open("data_new.csv", "r") as f:
#     print(f.read())

# with open("stud.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     writer.writerow({"Имя": "Вова", "Возраст": "14"})


# data = [{
#
#     'hostname': 'sw1',
#
#     'location': 'London',
#
#     'model': '3750',
#
#     'vendor': 'Cisco'
#
# }, {
#
#     'hostname': 'sw2',
#
#     'location': 'Liverpool',
#
#     'model': '3850',
#
#     'vendor': 'Cisco'
#
# }, {
#
#     'hostname': 'sw3',
#
#     'location': 'Liverpool',
#
#     'model': '3650',
#
#     'vendor': 'Cisco'
#
# }, {
#
#     'hostname': 'sw4',
#
#     'location': 'London',
#
#     'model': '3650',
#
#     'vendor': 'Cisco'
#
# }]
#
# with open("dict_writer.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=data[0].keys())
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# with open("todos.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=todos[0].keys())
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)

#   Парсинг


from bs4 import BeautifulSoup

# f = open('index 2.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# row = soup.find_all("div", {'data-set': "salary"})
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", {"class": "name"})
# row = soup.find("div", class_="name").txt
# row = soup.find("div", string="Alena").findParent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)

# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index 2.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
#
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)


# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     r = re.search(pattern, s).group()
#     print(r)
#
#
# f = open('index 2.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
#
# for i in salary:
#     # get_salary()
#     print(i.text)


import requests
from bs4 import BeautifulSoup


# r = requests.get("https://ru.wordpress.org/")
# print(r.text)

def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    p1 = soup.find('header', id='masthead').find("p", class_="site-title").text
    return p1


def main():
    url = "https://ru.wordpress.org/"
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
