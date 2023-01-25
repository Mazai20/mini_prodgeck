from random import *


def get_word(pets, sport, african_animals):
    word_list_pets = ["свинья", "лошадь", "кошка", "корова", "собака", "овца", "козел", "курица"]
    word_list_sport = ["футбол", "хоккей", "теннис", "регби", "гольф", "биатлон", "дзюдо", "бокс"]
    word_list_african_animals = ["обезьяна", "жираф", "носорог", "слон", "бегемот", "зебра", "лев", "буйвол",
                                 "антилопа"]
    word_list = []

    if pets: word_list.extend(word_list_pets)
    if sport: word_list.extend(word_list_sport)
    if african_animals: word_list.extend(word_list_african_animals)

    return "" if len(word_list) == 0 else choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    tries = 7

    now = []

    for i in range(len(word)):
        now.append('-')

    print(''.join(now))

    while (tries):
        ans = input("Введите Ваш ответ\n").upper()

        if (len(ans) == len(word)):
            for i in range(len(ans)):
                if ((ans[i] == word[i]) and (now[i] == '-')):
                    now[i] = ans[i]

        print(''.join(now))

        if (ans == word):
            print("Ура! Вы выиграли!")
            return

        tries -= 1

        print(display_hangman(tries))

    print("Увы, Вы проиграли :(")


def __main():
    s = "да"

    while (s.lower() == "да"):
        pets = bool(input("Включать слова на тему <<Домашние животные>> ?\n").lower() == "да")
        sport = bool(input("Включать слова на тему <<Спорт>> ?\n").lower() == "да")
        african_animals = bool(input("Включать слова на тему <<Африканские животные>> ?\n").lower() == "да")

        word = get_word(pets, sport, african_animals)

        if word == "":
            print("Вы не выбрали ни одну из тем")
        else:
            play(word)

        s = input("Играть заново?\n")

        # print(display_hangman(1))

    print("До скорой встречи!")


__main()