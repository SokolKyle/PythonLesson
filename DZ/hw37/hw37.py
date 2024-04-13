from hw_perser37 import Parser


def main():
    url = "https://rutor-gamer.info/games/page/{}/"
    pars = Parser(url, "hw_game37.txt")
    pars.run()


if __name__ == '__main__':
    main()
