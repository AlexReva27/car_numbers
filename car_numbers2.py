import os, keyboard

file = open("base.txt").read().split()


def inp():
    guess = input("Введите номер автомобиля или часть номера: ").strip()
    if len(guess) != 0:
        return guess
    else:
        print("Вы ничего не ввели")
        ex()


def search(guess):
    return [word for word in file if guess in word]


def out(num):
    if len(num) != 0:
        for x in num:
            print(x)
        print("Колличество найденых номеров: " + str(len(num)))
    else:
        print("Таких номеров нет в базе")
    ex()


def ex():
    print("\nДля нового поиска - нажмите Space.\nДля выхода из программы - нажмите Esc.")
    while True:
        if keyboard.is_pressed('Esc'):
            break
        if keyboard.is_pressed('space'):
            start()


def start():
    out(search(inp()))


start()


