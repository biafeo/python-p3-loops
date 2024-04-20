#!/usr/bin/env python3

def happy_new_year(num):
    i = num
    while i>=1 :
     print(i)
     i -= 1 
    print("Happy New Year!")

def square_integers(int_list):
    squared_list = []
    for integer in int_list:
        squared = integer ** 2
        squared_list.append(squared)
    return squared_list

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        message = "FizzBuzz"
    elif num % 3 == 0:
        message = "Fizz"
    elif num % 5 == 0:
        message = "Buzz"
    else:
        message = str(num)
    return message