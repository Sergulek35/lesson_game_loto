import random


def separator(simbol):  # Разделитель
    return simbol * 40


class Kegs:
    def __init__(self):
        # количество бочонков в мешке
        self.kegs = [keg for keg in range(1, 91)]

    def __str__(self):
        return f'(Осталось - {len(self.kegs)})'

    def kegs_minus(self, number):
        # выкидываем случайный бочонок
        self.kegs.remove(number)


class Card:

    def __init__(self):
        # создать карту
        selection = random.sample(range(1, 91), 15)
        self.card = [*sorted(selection[:5]), '\n', '', *sorted(selection[5:10]), '\n', *sorted(selection[10:])]
        self.once = 0

    def card_out(self, number):
        # зачёркиваем бочонок

        ind = self.card.index(number)
        self.card.insert(ind, "-")
        self.card.remove(number)
        self.once += 1

    def __eq__(self, other):
        return self.card != self.once


class Person:
    def __init__(self):
        self.person = {}

    def __str__(self):
        return f'Всего игроков: {len(self.person)}'


    def add_player(self, name):
        if name in self.person:
            self.text = 'Такое имя уже есть!'
        else:
            new_player = Card()
            self.person[name] = new_player
            self.text = 'Игрок успешно создан!'
