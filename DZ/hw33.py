import json
from random import choice


def gen_tel():
    tel = ''
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    while len(tel) != 10:
        tel += choice(num)

    return tel


def gen_person():
    name = ''

    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']

    while len(name) != 7:
        name += choice(letter)

    person = {
        'name': name,
        'tel': gen_tel()
    }
    return person


def add_person():
    try:
        data = json.load(open('pers.json'))
    except FileNotFoundError:
        data = {}

    data[gen_tel()] = gen_person()
    with open('pers.json', 'w') as f:
        json.dump(data, f, indent=2)


def add_person_list():
    try:
        data = json.load(open('pers.json'))
    except FileNotFoundError:
        data = {}

    tmp = {}
    for i in range(3):
        tmp[gen_tel()] = gen_person()

    data.update(tmp)
    with open('pers.json', 'w') as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    for i in range(3):
        add_person()

    add_person_list()
