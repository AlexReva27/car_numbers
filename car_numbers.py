import os, keyboard

file = open("base.txt").read()


def func():
    guess = input("Введите номер автомобиля или часть номера: ").strip()
    if len(guess) != 0:
        numbers = [word for word in file.split() if guess in word]
        if len(numbers) != 0:
            for x in numbers:
                print(x)
            print("Колличество найденых номеров: " + str(len(numbers)))
        else:
            print("Таких номеров нет в базе")
    else:
        print("Вы ничего не ввели")
    print("\nДля нового поиска - нажмите Space.\nДля выхода из программы - нажмите Esc.")
    ex()


def ex():
    while True:
        if keyboard.is_pressed('Esc'):
            break
        if keyboard.is_pressed('space'):
            func()


func()
