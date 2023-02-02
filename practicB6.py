
# Игровые клетки
def cells(f):
    print('\t\t   \033[4m0 1 2\033[0m')
    for i in range(len(f)):
        print('\t\t' + str(i) + '| ' + ' '.join(field[i]))

# Ввод координат и проверка на ошибки ввода
def input_coordinates(f, x_o, user):
    print(f"_______\n\033[32mХодит {user} игрок - {x_o}.\033[0m")
    while True:
        coord = input(f"Введите координаты через пробел:").split()
        if not ((coord[0].isdigit()) and (coord[1].isdigit())):
            print('_______\n\033[31mОШИБКА! Вы ввели символы.\033[0m Попробуйте числа.')
            continue
        if len(coord) != 2:
            print('_______\n\033[31mОШИБКА!\033[0m Введите ДВЕ координаты. Например:2 2')
            continue
        x, y = map(int, coord)
        if not (x >= 0 and x < 3 and y >= 0 and  y < 3 ):
            print('_______\n\033[31mОШИБКА! Таких координат нет. \033[0mПопробуйте снова.')
            continue
        if f[x][y] != '-':
            print('_______\n\033[31mОШИБКА! Клетка занята. \033[0mПопробуте снова.')
            continue
        break
    return x,y

# Проверка выигрыша
def win_check (f,x_o):
    def check_line(с1, с2, с3, x_o):
        if с1 == x_o and с2 == x_o and с3 == x_o:
            return True
        return False
    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], x_o) or \
                check_line(f[0][n], f[1][n], f[2][n], x_o) or \
                check_line(f[0][0], f[1][1], f[2][2], x_o) or \
                check_line(f[2][0], f[1][1], f[0][2], x_o):
            return True
    return False

print('\n\t\033[31m\033[1mX_\033[33mO \033[34mИгра "Крестики-Нолики" \033[31mX_\033[33mO\033[0m\n')
field = [['-'] * 3 for _ in range(3)]
count = 0
while True:
    simbol = input("Введите, чем будет играть первый игрок \033[31mX\033[0m или \033[33mO\033[0m:")
    simbol = simbol.upper()
    if simbol != "X" and simbol != "O" and simbol != "Х" and simbol != "О": #англ и русс раскладка
        print("\033[31mОшибка!! Необходимо ввести: X или O\033[0m")
        continue
    break
s = 'X' if simbol == "O" or simbol == "О" else "O" #англ и русс раскладка
print(f"Второй игрок соответственно игрок играет:\033[32m{s}\033[0m\n")
while True:
    cells(field)
    if count % 2 == 0:
        user = "1-й"
        x_o = simbol
    else:
        user = "2-й"
        x_o = 'X' if x_o == "O" or x_o == "О" else "O"
    if count < 9:
        x, y = input_coordinates(field, x_o, user)
        field[x][y] = x_o
    elif count == 9:
        print('_______\n\033[33mНИЧЬЯ! Ходы закончились\033[0m')
        break
    if win_check(field,x_o):
        cells(field)
        print(f"_______\n\033[33mПОБЕДА! Выйграл {user} игрок - {x_o} \033[0m")
        break
    count += 1
print("\n\033[31mКонец игры")

