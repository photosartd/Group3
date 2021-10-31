#!/usr/bin/env python
import argparse
import json

FILEPATH = 'Lesson 5/phonebook.json'


def load_json(filepath: str) -> dict:
    dct = None
    with open(filepath, 'r') as f:
        dct = json.load(f)
    return dct


book = load_json(FILEPATH)

parser = argparse.ArgumentParser(description='This is parser \
                                             for telephone book')
parser.add_argument('-a', '--add', dest='param1')
parser.add_argument('-d', '--delete', dest='param2')
parser.add_argument('-s', '--show', dest='param3')

args = parser.parse_args()


def action_on_param1(s: str):
    name, teleph = s.split(':')
    if name in book:
        print(f'Контакт {name} обновлен')
    else:
        print(f'Контакт {name} создан')
    book[name] = int(teleph)


def action_on_param2(name: str):
    if name in book:
        del book[name]
        print(f'Контакт {name} удален')
    else:
        print(f'Такого контакта нет в книге')


def action_on_param3():
    for name, phone in book.items():
        print(f'{name}: {phone}')


def save_changes():
    with open(FILEPATH, 'w') as f:
        json.dump(book, f)


# Dima:894234324
if args.param1:
    action_on_param1(args.param1)
elif args.param2:
    action_on_param2(args.param2)
elif args.param3:
    action_on_param3()
save_changes()
