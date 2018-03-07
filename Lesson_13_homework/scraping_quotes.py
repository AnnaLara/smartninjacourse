#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#finds a number within range that does not exist in a list
def find_new_number(list, in_range):
    import random
    while True:
        new_number = random.randint(0, in_range)
        if list.count(new_number) == 0:
            return new_number

#generates a list of a desired quantity of numbers within range
def generate_numbers(quantity, in_range):
    numbers_list = []
    for x in range (1, quantity+1):
        numbers_list.append(find_new_number(numbers_list, in_range))
 
    return numbers_list


def main():

    print "This program will generate 5 quotes about marriage"

    from BeautifulSoup import BeautifulSoup
    from urllib2 import urlopen


    url = "http://quotes.yourdictionary.com/theme/marriage/"
    data = urlopen(url).read()
    soup = BeautifulSoup(data)

    quote_list =[]

    for item in soup.findAll('p', attrs={"class": "quoteContent"}):
        quote_list.append(item.text)

    for item in generate_numbers(5, len(quote_list)-1):
        print quote_list[item]



if __name__ == "__main__":
    main()