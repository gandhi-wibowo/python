#!/usr/bin/python

question = " "

while question != '' or question[0].lower() != 'y' and question[0].lower() != 'n':
    question = raw_input("yes or no : ")
    if question[0].lower() == "y":
        print "you chose Yes "
    elif question[0].lower() == "n":
        print "you chose No"
