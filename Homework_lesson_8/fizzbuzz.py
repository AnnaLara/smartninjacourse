#!/usr/local/bin/python
# -*- coding: utf-8 -*-

number = int(raw_input("Select a number between 1 and 100: "))

while number > 100 or number < 1:
    print "Number is not valid"
    number = int(raw_input("Select a number between 1 and 100: "))

count = 1

while count <= number:
    if (count % 3) == 0 and (count % 5) == 0:
        print "fizzbuzz"
    elif (count % 3) == 0 :
        print "fizz"
    elif (count % 5) == 0:
        print "buzz"
    else: print count

    count += 1
