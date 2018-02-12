#!/usr/local/bin/python
# -*- coding: utf-8 -*-

print "Hello! I will convert kilometers into miles for you!"

repeat = "YES"

while repeat == "YES":
    km = float(raw_input("Please, enter the number of kilometers: "))
    print km
    miles = km / 1.61
    print str(km) + " km is equal to " + str(miles) + " miles"
    repeat = raw_input("Whould you like to conver something else? Please type YES or NO: ").upper()
    print repeat

    while (repeat != "YES") and (repeat != "NO"):
        repeat = raw_input("You have not answered. Please type YES or NO: ").upper()

    if repeat == "NO":
        print "Good Buy!"
        break