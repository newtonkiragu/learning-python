#!/usr/bin/python

def solution(n):
    numbers = range(1,100)
    cont = []
    a = 0
    b = 0
    c = 0

    for number in numbers:
        if number % 3 == 0 and number % 5 == 0:
            a += 1
            print 'fizzbuzz'
        elif number % 5 == 0:
            b += 1
            print 'buzz'

        elif number % 3 == 0:
            c += 1
            print 'fizz'
        else: print (number)

    cont.append(a)
    cont.append(b)
    cont.append(c)


    return cont