#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def main():
    import random
    secret = random.randint(1,10)
    guess = int(raw_input("Guess a number from 1 to 10: "))
    print "The secret numer was " + str(secret)
    if guess == secret:
        print "You won!"
    else:
        print "You lost... Try again!"


if __name__ == "__main__":
    main()