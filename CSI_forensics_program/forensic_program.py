#!/usr/local/bin/python
# -*- coding: utf-8 -*-



##Use this data types for input parameters:
##dna = ''
##human_char = {}
##suspects = {}

##extracts characteristics found in the criminal's dna
def extract_char(human_char, dna):

    dna_char = {}

    for key in human_char:
        for k, v in human_char[key].iteritems():

            if dna.find(v) >= 0:
                dna_char[key] = k

    return dna_char

##compares characretistics of the criminal with suspects
def compare_dna(dna_char,suspects):

    criminal = ''
    for k, v in suspects.iteritems():
        if v == dna_char:
            criminal = k
            print "It is " + criminal + " who ate the icecream!"
    if criminal is False:
        print "None of the suspects is the criminal!"
    return criminal

#executes extract_char, prints the criminal's features and compares them to the suspects
def get_the_criminal(dna, suspects, human_char):
    dna_char = extract_char(human_char, dna)

    print "This is what our criminal looks like:"
    for k, v in dna_char.iteritems():
        print k + ": " + v

    compare_dna(dna_char, suspects)


def main():
    print "Hi! This program will find the criminal who ate all the icecream!"

    # extract dna from the text file
    dna_file = open("dna.txt", "r")
    dna = dna_file.read()

    ##create dictionaries containing the available data
    human_char = {}
    human_char['hair'] = {'black': 'CCAGCAATCGC', 'brown': 'GCCAGTGCCG', 'blonde': 'TTAGCTATCGC'}
    human_char['face'] = {'square': 'GCCACGG', 'round': 'ACCACAA', 'oval': 'AGGCCTCA'}
    human_char['eyes'] = {'blue': 'TTGTGGTGGC', 'green': 'GGGAGGTGGC', 'brown': 'AAGTAGTGAC'}
    human_char['gender'] = {'female': 'TGAAGGACCTTC', 'male': 'TGCAGGAACTTC'}
    human_char['race'] = {'white': 'AAAACCTCA', 'black': 'CGACTACAG', 'asian': 'CGCGGGCCG'}

    suspects = {}
    suspects['Eva'] = {'gender': 'female', 'race': 'white', 'hair': 'blonde', 'eyes': 'blue', 'face': 'oval'}
    suspects['Larisa'] = {'gender': 'female', 'race': 'white', 'hair': 'brown', 'eyes': 'brown', 'face': 'oval'}
    suspects['Matej'] = {'gender': 'male', 'race': 'white', 'hair': 'black', 'eyes': 'blue', 'face': 'oval'}
    suspects['Miha'] = {'gender': 'male', 'race': 'white', 'hair': 'brown', 'eyes': 'green', 'face': 'square'}

    get_the_criminal(dna, suspects, human_char)


if __name__ == "__main__":
    main()