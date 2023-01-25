from random import *


def is_valide(text, x , y): # проверка на соответтвия
    return text.isdigit() and float(text) - int(text) == 0 and x <= int(text) <= y


def is_valued_num(down_num = 0, up_num = 9999):  # ввод данных, значениями по умолчанию.
    # заданы верхний и нижний возможные пределы
    while True:
        text = input()
        if is_valide(text, down_num,up_num):
            return int(text)
        else:
            print(f'А может быть все-таки введем целое число от {down_num} до {up_num}?')


def compare_num(down_num, up_num):
    num = randint(down_num,up_num)
    total = 0
    while True:
        text = is_valued_num()
        total += 1
        if text < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif text > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угодали поздравляю!!! число ваших попыток составило: --{total}-- ')
            break


def counter_game(): # предложение продолжить игру
    counter = input("хотите продолжить игру('д'/'н')?\n")
    while True:
        if counter not in ('y', 'д', 'n', 'н'):
            counter = input("не верное значение чё тупой ? \nхотите продолжить игру('д'/'н'?) ")
        elif counter in ('n', 'н'):
            print("До новых встреч!!! сука")
            return False
        else:
            return True


def geme(): # запуск игры
    print("Добро пожаловать в игру угадайка")
    while True:
        print("Укажите в каком диапазоне Вы готовы угадывать число:")
        x, y = is_valued_num(), is_valued_num()
        if x > y:
            x, y = y, x
        print(f'введите число от {x} до {y}')
        compare_num(x, y)
        if counter_game():
            continue
        else:
            break


geme()
