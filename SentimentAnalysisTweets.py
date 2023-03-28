# Marieke Schelhaas
# S4132734
# Research Methods - Final Project
# 28 mrt. 2023

import sys


def handle_command_line(sys):
    '''Opens file and checks if there is only one .txt document as input'''
    infile_name = sys
    infile = open(infile_name, "r")
    return infile


def count_happy_words(infile):
    '''Takes file and counts words the words that are in the happy word list, an'''
    amount_happy = sum(infile.count(word) for word in ("yay", "jeej", "birthday", "verjaardag", "shopping", "winkelen", "awesome", "geweldig", "concert", "cool", "cute",
                                                       "schattig", "lunch", "middageten", "books", "boeken", "happy", "blij", "lovely", "heerlijk", "concert", "lucky", "gelukkig",
                                                       "bought", "gekocht", "dinner", "avondeten", "eten", "food", "drink", "drankje", "drunk", "dronken", "going out",
                                                       "uitgaan", "books", "boeken", "foto's", "pictures", "new", "nieuw", "lots", "veel", "interesting", "interessant",
                                                       "film", "movie", "party", "film", "fun", "plezier", "saturday", "zaterdag"))
    amount_not_happy = sum(infile.count(word) for word in ("not awesome", "niet geweldig", "niet cool", "not cute", "not drunk", "niet dronken", "not new",
                                                           "niet nieuw", "not lots", "niet veel", "not interesting", "niet interessant", "niet schattig",
                                                           "not happy", "niet blij", "not lovely", "not heerlijk", "not cool", "niet gelukkig"))
    amount_happy = amount_happy - amount_not_happy

    return amount_happy


def main():
    total = 0
    for num in range(1, 6):
        file = handle_command_line(sys.argv[num])
        amount_happy_words = count_happy_words(file.read())
        total = total + amount_happy_words
        print("Amount happy words in file", num, "=", amount_happy_words)
    print("Total happy words =", total)


if __name__ == "__main__":
    main()
