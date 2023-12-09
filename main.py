# task_1

import random


def guess(x):
    a= True
    random_number = random.randint(1, x)
    # print(random_number)
    while a:
        guesNumber = int(input("Guess a number between 1 and " + str(x) + ":"))
        if guesNumber < random_number:
            print("Sorry, guess again. Too low")
        elif guesNumber > random_number:
            print("Sorry, guess again. Too high")
        elif guesNumber == random_number:
            print("Kudos! you have guessed the number " + str(random_number) + " correctly ")
            a = False

guess(20)


# task_2

massive = [ 2 , 2, 2, 2, 2, 2, 2, 6, 7]


def task():
    i = massive[0]
    for x in massive:
        if x != i:
            print(x)


task()

# task_3

a = int(input("Enter century of year: "))


def century():

    if 1801 < a < 1900:
        print("19th century")

    elif 1901 < a < 2000:
        print("20th century")

    elif 2001 < a < 2024:
        print("21th century")


century()



