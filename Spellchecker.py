import os
import sys
from difflib import SequenceMatcher
from datetime import datetime
import timeit
import time



while True:


    english = open("EnglishWords.txt", "r")
    english = english.read()
    english = english.split('\n')

    print("Welcome to Spellchecker")

    print(" ")                                          #Border block, appears throughout the program
    ucd = ('\u03A6') * 70
    print(ucd)
    time.sleep(1)

    print("Please choose an option: ", "0. Quit", "1. Spellcheck a sentence", "2. Spellcheck a file ", sep='\n')
    optionList = [ "quit", "spellcheck a sentence", "spellcheck a file"]



    while True:
        optionSelect = input("Please enter the number of your chosen option: ")            #Main menu: asks users for they type of input, or quit
        if optionSelect not in ('1', '2', '0'):
            print("Please enter a valid option.")
            continue
        else:
            break

    print(" ")
    ucd = ('\u03A6') * 70
    print(ucd)
    time.sleep(1)

    print("You chose to " + optionList[int(optionSelect)])


    #If  '1' prompted to enter sentence
    badChars = [',', ':', ':', '!', '?', '/', '#', '*', '.', "'", '-', '-', '+',
     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if optionSelect == '1':                                                          #If 1 is selected in the main menu, user is asked for sentence input

        enterSentence = input("Please enter a sentence to be spellchecked: ")

        start = time.time()

        for x in badChars:                                                           #Replaces unwanted characters and validates input
            enterSentence = enterSentence.replace(x, '')
        enterSentence = enterSentence.lower()
        inputs = str(enterSentence)
        print("You have entered the following words: " + str(enterSentence))
        enterSentence = enterSentence.split(" ")

        correctWords = []                                                            #Stores correct words in correct words list
        for good in enterSentence:
            if good in(english):
                print("Correct Words: " + good)
                correctWords.insert(0, good)


        incorrectWords = []                                                         #Stores incorrect words in incorrect words list
        for bad in enterSentence:
            if bad not in(english):
                print("Incorrect words: " + bad)
                incorrectWords.insert(0, bad)

        dictWords = []
        suggestWords = []
        markedWords = []

        print(" ")
        ucd = ('\u03A6') * 70
        print(ucd)
        time.sleep(1)

        for words in enterSentence:                                                #Offers 4 options to deal with incorrect words
            if words not in(english):
                while True:
                    print("Please select an option for incorrect words: ", "1. Ignore", "2. Mark",
                     "3. Add to dictionary", "4. Suggest a likely spelling", sep='\n')
                    incorrectOptionList = ["Ignore", "Mark", "Add to dictionary", "Suggest a likely spelling"]
                    incorrectOptionSelect = input("Please enter the number of your chosen option for: " + words + " " )
                    if incorrectOptionSelect not in ('1', '2', '3', '4'):
                        print("Please select a valid option.")
                        continue
                    else:
                        break

                print(" ")
                ucd = ('\u03A6') * 70
                print(ucd)
                time.sleep(1)

                print("You have chosen the following option: " + incorrectOptionList[int(incorrectOptionSelect) -1])



                if incorrectOptionSelect == '2':                                   #When 2 is selected in the previous menu, word is marked and added to marked list
                    print(" ")
                    ucd = ('\u03A6') * 70
                    print(ucd)
                    time.sleep(1)

                    print("The incorrect word " + words + " has been marked:")
                    words = words + "?"
                    print(words)
                    markedWords.insert(0, words)


                if incorrectOptionSelect == '3':                                   #When 3 is selected in the previous menu, word is added to dictionary and added to dictionary list
                    print(" ")
                    ucd = ('\u03A6') * 70
                    print(ucd)
                    time.sleep(1)

                    addWords = open("EnglishWords.txt", "a")
                    addWords = addWords.write('\n' + words)
                    incorrectWords.remove(words)
                    correctWords.insert(0, words)
                    dictWords.insert(0, words)


                if incorrectOptionSelect == '4':                                   #When 4 is selected, the program looks for suggestions in the dictionary

                    print(" ")
                    ucd = ('\u03A6') * 70
                    print(ucd)
                    time.sleep(1)

                    for j in english:
                        suggest = SequenceMatcher(None, str(words), str(j)).ratio()
                        if suggest >= 0.8:                                         #If the ratio of sequencematcher is greater than 0.8, the program offers suggestions
                            print("Suggest word is : " + j)
                            print("Please choose an option: ", "0. Accept suggested word", "1. Ignore suggestion", sep = '\n')
                            suggestList = ["accept suggested word", "ignore suggestion"]
                            while True:
                                suggestOption = input("Please enter your chosen option: ") #Asks for input on whether to accept or reject suggestion
                                if suggestOption not in('0', '1'):
                                    print("Please enter a valid option")
                                else:
                                    break
                            print("You've chosen to: " + suggestList[int(suggestOption)])

                            print(" ")
                            ucd = ('\u03A6') * 70
                            print(ucd)
                            time.sleep(1)

                            if suggestOption == '0':
                                correctWords.insert(0, j)
                                incorrectWords.remove(words)
                                suggestWords.insert(0, j)
                                break


        end = time.time()

        numberWords = []
        for n in enterSentence:
            numberWords.insert(0, n)

        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")





    #If 2-Prompted for filename
    if optionSelect == '2':

        print(" ")
        ucd = ('\u03A6') * 70
        print(ucd)
        time.sleep(1)


        while True:
            try:
                enterFilename = input("Please enter a file name: ")           #If 2 is selected in the main menu, program asks for file name, asks again if file doesn't exist
                print("You have selected the following file: " + str(enterFilename))
                file = open(enterFilename, "r")
            except FileNotFoundError:
                print("Oops! File not found. Please try again.")
                continue
            else:
                break

        print(" ")
        ucd = ('\u03A6') * 70
        print(ucd)
        time.sleep(1)

        start = time.time()

        file = file.read()
        for x in badChars:
            file = file.replace(x, '')
        file = file.lower()
        inputs = str(file)
        print("The file contains the following words: ")
        print(file)
        file = file.split(" ")

        correctWords = []
        for good in file:
            if good in(english):
                print("Correct Words: " + good)
                correctWords.insert(0, good)


        incorrectWords = []
        for bad in file:
            if bad not in(english):
                print("Incorrect words: " + bad)
                incorrectWords.insert(0, bad)

        markedWords = []
        dictWords = []
        suggestWords = []

        print(" ")
        ucd = ('\u03A6') * 70
        print(ucd)
        time.sleep(1)

        for words in file:
            if words not in(english):
                while True:
                    print("Please select an option for incorrect words: ", "1. Ignore", "2. Mark",
                     "3. Add to dictionary", "4. Suggest a likely spelling", sep='\n')
                    incorrectOptionList = ["Ignore", "Mark", "Add to dictionary", "Suggest a likely spelling"]
                    incorrectOptionSelect = input("Please enter the number of your chosen option for: " + words + " " )
                    if incorrectOptionSelect not in ('1', '2', '3', '4'):
                        print("Please select a valid option.")
                        continue
                    else:
                        break
                print("You have chosen the following option: " + incorrectOptionList[int(incorrectOptionSelect) -1])


                if incorrectOptionSelect == '2':

                    print(" ")
                    ucd = ('\u03A6') * 70
                    print(ucd)
                    time.sleep(1)

                    print("The incorrect word " + words + " has been marked:")
                    words = words + "?"
                    print(words)
                    markedWords.insert(0, words)



                if incorrectOptionSelect == '3':

                    print(" ")
                    ucd = ('\u03A6') * 70
                    print(ucd)
                    time.sleep(1)


                    addWords = open("EnglishWords.txt", "a")
                    addWords = addWords.write('\n' + words)
                    incorrectWords.remove(words)
                    correctWords.insert(0, words)
                    dictWords.insert(0, words)
                    print(correctWords)
                    print(incorrectWords)

                if incorrectOptionSelect == '4':

                    print(" ")
                    ucd = ('\u03A6') * 70
                    print(ucd)
                    time.sleep(1)


                    for j in english:
                        suggest = SequenceMatcher(None, str(words), str(j)).ratio()
                        if suggest >= 0.8:
                            print("Suggest word is : " + j)
                            print("Please choose an option: ", "0. Accept suggested word", "1. Ignore suggestion", sep = '\n')
                            suggestList = ["accept suggested word", "ignore suggestion"]

                            while True:
                                suggestOption = input("Please enter your chosen option: ")
                                if suggestOption not in('0', '1'):
                                    print("Please enter a valid option")
                                else:
                                    break
                            print("You've chosen to: " + suggestList[int(suggestOption)])

                            print(" ")
                            ucd = ('\u03A6') * 70
                            print(ucd)
                            time.sleep(1)


                            if suggestOption == '0':
                                correctWords.insert(0, j)
                                incorrectWords.remove(words)
                                suggestWords.insert(0, j)
                                break



        end = time.time()

        numberWords = []
        for n in file:
            numberWords.insert(0, n)


        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    #If 0- Quit
    if optionSelect == '0':
        sys.exit()




    # Summary
    # print: total words, num correct words, num incorrect words, num added to dictionary, num words changed by accepting suggested

    print(" ")
    ucd = ('\u03A6') * 70
    print(ucd)
    time.sleep(1)


    summary =    ("Summary")                                                      #Defines summary and statistics
    a =    ("Total number of words: " + str(len(numberWords)))
    b =   ("Total number of correctly spelt words: " + str(len(correctWords)))
    c =    ("Total number of incorrectly spelt words: " + str(len(incorrectWords)))
    d =    ("Total number of words added to the dictionary: " + str(len(dictWords)))
    e =    ("Total number of words marked: " + str(len(markedWords)))
    f =    ("Total number of accepted suggested words: " + str(len(suggestWords)))
    dt =   ("Time and date of spellcheck: " + now)
    mwords = '\n'.join(markedWords)
    m = ("Marked words: " + mwords)
    td = (end - start)
    te = ("Time elapsed during spellcheck: " + str(td) + " seconds")
    inp = ("Inputs entered: " + inputs)


    g = (str(summary) + '\n' + str(a) + '\n' +  str(b) + '\n' + str(c) + '\n' + str(c) +
     '\n' + str(d) + '\n' + str(e) + '\n' + str(f) + '\n' + dt + '\n' + te)

    h = (str(summary) + '\n' + str(a) + '\n' +  str(b) + '\n' + str(c) + '\n' + str(c)
     + '\n' + str(d) + '\n' + str(e) + '\n' + str(f) + '\n' + '\n' + '\n' + dt + '\n' + te
     + '\n' + m + '\n' + inp)

    print(g)


    print(" ")
    ucd = ('\u03A6') * 70
    print(ucd)
    time.sleep(1)

    while True:                                     #Asks for file name to store statistics
        try:
            statistics = input("Please enter the name of the file you want to output the statistics to: ")
            statisticsFile = open(statistics + ".txt", "x")
        except FileExistsError:
            print("The file already exists. Please enter a different name.")
            continue
        else:
            break

    statisticsFile.close()
    stats = open(statistics + ".txt", "w")
    stats.write(h)

    print(" ")
    ucd = ('\u03A6') * 70
    print(ucd)
    time.sleep(1)

    print("Please choose an option: ", "0. Quit", "1. Return to main menu", sep = '\n')

    while True:                                         #Final menu asks if you want to quit or to return to main menu
        finalMenu = input("Please enter your chosen option: ")
        if finalMenu not in('0', '1'):
            print("Please enter a valid option")
            continue
        else:
            break
    if finalMenu == '0':
        break
        sys.exit()
    if finalMenu == '1':
        print(" ")
        ucd = ('\u03A6') * 70
        print(ucd)
        time.sleep(1)
        continue
