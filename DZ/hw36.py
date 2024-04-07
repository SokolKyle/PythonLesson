import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")

    p1 = soup.find("h1", id="firstHeading").find("span", class_="mw-page-title-main").text
    p2 = soup.find("div", id="siteSub").text
    p3_div = soup.find("div", id="mw-content-text")
    p3 = "Параграф не найден"

    if p3_div:
        p_tags = p3_div.find_all("p")
        for p_tag in p_tags:
            p_text = p_tag.text.strip()
            if p_text:
                p3 = p_text
                break
    return f"{p1} \n{p2} \n{p3}"


def main():
    url = "https://ru.wikipedia.org/wiki/Python"
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
