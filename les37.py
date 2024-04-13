# import requests
# from bs4 import BeautifulSoup
#
#
# # r = requests.get("https://ru.wordpress.org/")
# # print(r.text)
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find('header', id='masthead').find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()
import csv

# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# # r = requests.get("https://ru.wordpress.org/")
# # print(r.text)
#
# def get_html(url):
#     r = requests.get(url)
#
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data["name"], data["url"], data["rating"]))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     s = soup.find_all("section", "plugin-section")[1]
#     plugins = s.find_all("article")
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a").get("href")
#         rating = plugin.find("span", class_="rating-count").find("a").text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#     # return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

#
import requests
from bs4 import BeautifulSoup


# r = requests.get("https://ru.wordpress.org/")
# print(r.text)

def get_html(url):
    r = requests.get(url)
    return r.text


def refine_sy(s):
    return s.split()


def write_cy(data):
    with open("plugins1.csv", "a") as f:
        write = csv.writer(f, delimiter=";", lineterminator="\r")
        write.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("article")
    for el in elements:
        try:
            name = el.find("h3").text
        except AttributeError:
            name = ""

        try:
            url = el.find('h3').find('a')["href"]
        except AttributeError:
            url = ""

        try:
            snippet = el.find("div", class_="entry-excerpt").text.strip()
        except AttributeError:
            snippet = ""

        try:
            active = el.find("span", class_="active-installs").text.strip()
        except AttributeError:
            active = ""

        try:
            c = el.find("span", class_="tested-with").text.strip()
            cy = refine_sy(c)[-1]
        except AttributeError:
            cy = ""

        data = {
            'name': name,
            'url': url,
            'snippet': snippet,
            'active': active,
            'cy': cy
        }

        write_cy(data)


def main():
    for i in range(1, 24):
        url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
        get_data(get_html(url))


if __name__ == '__main__':
    main()

# from persers37 import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()
