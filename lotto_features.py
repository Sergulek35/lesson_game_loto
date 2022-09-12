import random


def separator(simbol):  # Разделитель
    return simbol * 40


class Keds:
    def __init__(self):
        # количество бочонков в мешке
        self.kegs = [keg for keg in range(1, 91)]

    def kegs_minus(self, number):
        # выкидываем случайный бочонок
        self.kegs.remove(number)


class Card:

    def __init__(self):
        # создать карту
        selection = random.sample(range(1, 91), 15)
        self.card = [*sorted(selection[:5]), *sorted(selection[5:10]), *sorted(selection[10:])]
        self.once = 0

    def card_out(self, number):
        # зачёркиваем бочонок

        ind = self.card.index(number)
        self.card.insert(ind, "-")
        self.card.remove(number)
        self.once += 1
