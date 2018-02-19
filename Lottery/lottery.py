#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def find_new_number(list):
    import random
    while True:
        new_number = random.randint(1, 100)
        if list.count(new_number) == 0:
            return new_number


def generate_numbers(number):
    lottery_list = []
    for x in range(1, number):
        lottery_list.append(find_new_number(lottery_list))
    print lottery_list
    print "END"


def main():
    print "Welcome to the Lottery numbers generator."
    print "It can generate up to 100 numbers which will not repeat"

    num = ""
    while isinstance(num, int) == False:
        try:
            num = int(raw_input("Please enter how many random numbers would you like to have: "))
            generate_numbers(num)
        except ValueError:
            print "Invalid number"


if __name__ == "__main__":
    main()