#!/usr/bin/env python3

def happy_new_year():
    i = 0
    while i <= 10:
        print(i)
        i += 1
    print("Happy New Year!")

def square_integers(int_list):
    return [int * int for int in int_list]

def fizzbuzz():
    i = 0
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
