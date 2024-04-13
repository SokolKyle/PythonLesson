import requests
from bs4 import BeautifulSoup


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        # game = self.html.find_all("div", id="content")
        game = self.html.find_all("tr", class_="gai")

        # print(game)
        for item in game:
            title = item.find_all('a')
            for t in title:
                game_text = t.get_text(strip=True)
                # print(game_text)
                self.res = game_text



    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            i = 1
            for item in self.res:
                f.write(f"Игра № {i}\n\nНазвание: {self.res}\n")
                i += 1

    def run(self):
        for i in range(1, 4):
            self.url = self.url.format(i)
            self.get_html()
            self.parsing()
            self.save()
