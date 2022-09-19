import random
from lotto_features import separator, Kegs, Person

barrels = Kegs()
players = Person()
corrent_player = None

print('    ИГРА НАЧИНАЕТСЯ! ')
while True:
    print(separator('-'))
    print(f'Всего игроков: {len(players.person)}')
    print('1. Человек')
    print('2. Компьютер')
    print('3. Играть')
    print(separator('/'))

    choise = input('Выберите пункт меню: ')
    if choise == '1':
        name = input('Введите имя игрока: ')
        players.add_player(name)
        print(players.text)
    elif choise == '2':
        name = input('Введите имя компьютера: ') + '(cru)'
        players.add_player(name)
        print(players.text)

    elif choise == '3':
        if players.person:
            break
        else:
            print(' Чтобы играть, нужно добавить игрока!')

    else:
        print('Введите 1,2 или 3')

while players:

    for name in players.person:
        corrent_player = players.person[name]

        print(f'   ---------- {name} ----------')

        print('', *corrent_player.card[:5], sep='      ')
        print(*corrent_player.card[5:10], sep='    ')
        print('', *corrent_player.card[10:], sep='     ')

        print(separator('-'))

    # input('Нажмите "Enter", чтобы достать бочёнок из мешка:  ') -- можно добавить,когда играют компьютеры
    number = random.choice(barrels.kegs)
    barrels.kegs_minus(number)
    print(separator('.'))
    print(f'Выпал бочонок : {number} (Осталось - {len(barrels.kegs)})')

    for name in players.person.copy():
        corrent_player = players.person.copy()[name]
        if not '(cru)' in name:
            print(separator('.'))
            cross_out = input(f'Игрок {name} зачеркнуть цифру? (+/-): ')

            if cross_out == '+':
                if number in corrent_player.card:
                    corrent_player.card_out(number)

                else:
                    print(separator('"'))
                    print(f'Цифры нет на карте\nИгрок {name} проиграл!')
                    del players.person[name]

            elif cross_out == '-':
                if number in corrent_player.card:
                    print(separator('"'))
                    print(f'Цифра есть на карте\nИгрок {name} проиграл!')
                    del players.person[name]

            else:
                print(f'Не правильный ввод\nИгрок {name} проиграл!')
                del players.person[name]
        else:
            if number in corrent_player.card:
                corrent_player.card_out(number)
        if corrent_player.once == 15:
            print(f'Игрок {name} выйграл ')
    if corrent_player.once == 15:
        break
else:
    print(separator('/'))
    print('ИГРА ОКОНЧЕНА! ')
