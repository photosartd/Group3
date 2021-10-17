import argparse

book = {
    'Roman': 89997771313,
    'Ivan': 89107645343,
    'Semen': 845673456,
    'Fedor': 834563456
}

parser = argparse.ArgumentParser(description='This is parser \
                                             for telephone book')
parser.add_argument('-a', '--add', dest='param1')
parser.add_argument('-d', '--delete', dest='param2')
parser.add_argument('-s', '--save', dest='param3')

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


# Dima:894234324
if args.param1:
    action_on_param1(args.param1)
elif args.param2:
    action_on_param2(args.param2)
