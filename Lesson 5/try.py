import json

book = {
    'Roman': 89997771313,
    'Ivan': 89107645343,
    'Semen': 845673456,
    'Fedor': 834563456
}

with open('phonebook.json', 'w') as f:
    json.dump(book, f)