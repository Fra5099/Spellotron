"""
file: spellotron.py
description: program to fix the spelling mistakes
language: python3.7
author: Faisal Alzahrany
"""


from sys import *
from tools import *


def replace_ch(word):
    """
    this function will replace the letter with its adjacent letter if the word has this problem
    :param word: the word that we want to fix it
    :return: if the problem fixed will return the corrected word if not then it will return None
    """
    for inx in range(0,len(word)):
        new_word=word
        ch=word[inx]
        list_a=KEY_ADJACENCY_FILE[ch]
        count=len(KEY_ADJACENCY_FILE[ch])
        stop=0
        while stop<count:
            new_word=list(new_word)
            new_word[inx]=list_a[stop]
            new_word="".join(new_word)
            test=find_word(new_word)
            stop+=1
            if test is None:
                pass
            else:
                return test
    return None


def extra_one(word):
    """
    this function will fix the word if it has extra character
    :param word: the word we want to fix it
    :return: it will return the corrected word or if not fixed will return None
    """
    for inx in range(0,len(word)):
        new_word=list(word)
        new_word.pop(inx)
        new_word="".join(new_word)
        test=find_word(new_word)
        if test is not None:
            return test
    return None


def we_need_ch(word):
    """
    this function will fix the word that need a character by adding it
    :param word: the word we need to fix
    :return: it will return the corrected word or if not fixed will return None
    """
    for inx in range(0,len(word)+1):
        for ch in range(ord("a"),ord("z")+1):
            list_ch = list(word)
            list_ch.insert(inx,chr(ch))
            new_word="".join(list_ch)
            test=find_word(new_word)
            if test is not None:
                return test

    return None




def check_spell(word):
    """
    this function will fix the word by checking it on three conditions which are the hitting the key adjacent
    or it has extra character or it need one character
    :param word: the word that we want to fix it
    :return: it will return the corrected word or if not fixed will return None
    """
    if find_word(word) is not None:
        return word
    else:
        new_word=word.lower()

        new_word=remove_punct(word)
        if we_need_ch(new_word) is not None:
            new_word=we_need_ch(new_word)
            new_word=add_punct(word,new_word)
            return new_word
        elif extra_one(new_word) is not None:
            new_word=extra_one(new_word)
            new_word=add_punct(word,new_word)
            return new_word
        elif replace_ch(new_word) is not None:
            new_word=replace_ch(new_word)
            new_word=add_punct(word,new_word)
            return new_word
        else:
            return None



def file_words(filename):
    """
        this function the words mode when the user want to use text file

    :param filename: the text file name
    :return:
    """
    file=open(filename)

    corrected = []
    original = []
    unknown = []
    num_words = 0
    for line in file:
        line=line.split()
        for word in line:
            num_words += 1
            new_word = check_spell(word)
            if new_word==word:
                pass
            elif new_word is not None:
                if word[0].isupper() == True:
                    new_word=list(new_word)
                    new_word[0]=new_word[0].upper()
                    new_word="".join(new_word)

                corrected += [new_word]
                original += [word]
            else:
                unknown += [word]
    print_file(filename)
    print("")
    for word in range(0,len(corrected)):
        print(original[word],"->",corrected[word])
    print("")
    print(num_words, "words read from file")
    print("")
    print(len(corrected), "Corrected words")
    print(original)
    print("")
    print(len(unknown), "Unknown words")
    print(unknown)



def file_lines(filename):
    """
    this function the lines mode when the user want to use text file
    :param filename: the text file name
    :return:
    """
    file=open(filename)
    corrected = []
    original = []
    unknown = []
    new_sentence=[]
    num_words = 0
    for line in file:
        line=line.split()
        new_line=""
        for word in line:
            num_words += 1
            new_word = check_spell(word)

            if new_word==word:
                new_line+=word
            elif new_word is not None:
                if word[0].isupper() == True:
                    new_word=list(new_word)
                    new_word[0]=new_word[0].upper()
                    new_word="".join(new_word)

                corrected += [new_word]
                original += [word]
                new_line+=new_word
            else:
                new_line+=word
                unknown += [word]

            new_line+=" "
        new_sentence+=[new_line]
    print("")
    for line in new_sentence:
        print(line)
    print("")
    print(num_words, "words read from file")
    print("")
    print(len(corrected), "Corrected words")
    print(original)
    print("")
    print(len(unknown), "Unknown words")
    print(unknown)


def main():
    """
    this function will execute the spellotron program
    :return:
    """
    read_english_dic("american-english.txt")
    replace_dic("keyboard-letters.txt")
    print(len(argv))
    if  2>len(argv) or len(argv)>3:
        raise TypeError("retype because there was mistake in your input")
    elif argv[1]=="words":
        if len(argv)==3:

            file_words(argv[2])
        else:
            while True:
                file=input()
                if file=="":
                    break
                else:
                    corrected = []
                    original = []
                    unknown = []
                    num_words = 0
                    file=file.split()
                    for word in file:
                        num_words += 1
                        new_word = check_spell(word)
                        if new_word == word:
                            pass
                        elif new_word is not None:
                            if word[0].isupper() == True:
                                new_word = list(new_word)
                                new_word[0] = new_word[0].upper()
                                new_word = "".join(new_word)
                            corrected += [new_word]
                            original += [word]
                        else:
                            unknown += [word]
                    for word in range(0, len(corrected)):
                        print(original[word], "->", corrected[word])
                    print(num_words, "words read from file")
                    print(len(corrected), "Corrected words")
                    print(original)
                    print(len(unknown), "Unknown words")
                    print(unknown)

    elif argv[1]=="lines":
        if len(argv)==3:
            file_lines(argv[2])
        else:
            while True:
                file=input()
                if file=="":
                    break
                corrected = []
                original = []
                unknown = []
                new_sentence = ""
                num_words = 0
                file=file.split()
                for word in file:
                    num_words += 1
                    new_word = check_spell(word)
                    if new_word == word:
                        new_sentence += word
                    elif new_word is not None:
                        if word[0].isupper() == True:
                            new_word = list(new_word)
                            new_word[0] = new_word[0].upper()
                            new_word = "".join(new_word)
                        corrected += [new_word]
                        original += [word]
                        new_sentence += new_word
                    else:
                        new_sentence += word
                        unknown += [word]
                    new_sentence+=" "
                print(new_sentence)
                print(num_words, "words read from file")
                print(len(corrected), "Corrected words")
                print(original)
                print(len(unknown), "Unknown words")
                print(unknown)
    else:
        raise TypeError("retype because there was mistake in your input")


main()