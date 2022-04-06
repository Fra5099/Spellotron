"""
file: tools.py
description: some helping functions for spellotron.py
language: python3.7
author: Faisal Alzahrany
"""


LEGAL_WORD_FILE={}
KEY_ADJACENCY_FILE={}

def print_file(filename):
    """
    this function to print the text file
    :param filename: file text name
    :return:
    """
    file=open(filename)
    sentences=""
    for word in file:
        sentences+=word

    print(sentences)

def read_english_dic(filename):
    """
    this function read the file and put the words inside dictionary
    :param filename: the name of the file we want to read
    :return: dictionary
    """
    file=open(filename)

    global LEGAL_WORD_FILE

    for word in file:
        word=word.strip()
        lst=[]
        for ch in range(0,len(word)):
            lst+=[word[ch]]
        lst.sort()
        new_word=""
        for ch in range(0,len(lst)):
            new_word+=lst[ch]
        if new_word not in LEGAL_WORD_FILE:
            LEGAL_WORD_FILE[new_word]=[]
        LEGAL_WORD_FILE[new_word]+=[word]

def replace_dic(filename):
    """
    this function to put every letter with its adjacent letters in a dictionary
    :param filename: the file text name
    :return:
    """
    global KEY_ADJACENCY_FILE
    file=open(filename)
    for line in file:
        line=line.split()
        ch=1
        KEY_ADJACENCY_FILE[line[0]]=[]
        while ch<len(line):
            KEY_ADJACENCY_FILE[line[0]]+=line[ch]
            ch+=1

def remove_punct(word):
    """
    this function remove all the punctuation from the string
    :param word: the word that we want to remove the punctuation from it
    :return: new_word
    """
    new_word=""
    for ch in word:
        if ch.isalpha():
            new_word+=ch
    return new_word


def readd_punct(word,new_word):
    """
    this function readd the punctuation to the corrected word
    :param word: the old word that with punctuation
    :param new_word: the new corrected word that we want to readd the punctuation to it
    :return: word
    """
    if word.isalpha():
        return new_word
    count=0
    end=0
    for index in range(0,len(word)):
        if word[index].isalpha():
            end=index
            count+=1

    count=end-(count)
    word=word[:count+1]+new_word+word[end+1:]

    return word

def find_word(string):
    """
    this function find the word that we want from English dictionary
    :param string: the word that we want to find its anagrams
    :return: string(the word we want) or if it is not in the dictionary it will return None
    """
    lst=[]
    word=""
    for ch in string:
        lst+=[ch]
    lst.sort()
    for ch in range(0,len(lst)):
        word+=lst[ch]
    if word not in LEGAL_WORD_FILE:
        return None
    else:
        if string not in LEGAL_WORD_FILE[word]:
            return None
        else:
            return string

read_english_dic("american-english.txt")
replace_dic("keyboard-letters.txt")