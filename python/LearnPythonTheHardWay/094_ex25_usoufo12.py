# -*- coding: utf-8 -*-

def break_words(stuff):
    """This function breaks the string into words"""
    words = stuff.split(' ')
    return break_words

def sort_words(words):
    """sort the words"""
    return sorted(words)

def print_first_word(words):
    """ takes the firstword and prints""" # The word is remobed from list
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """ takes the lastword and prints"""
    word = words.pop(-1)
    print(word)
    
def sort_sentence(sentence):
    """with given a whole sentence, it sorts the words and returns"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """문장이 처음과 마지막 단어를 출력합니다."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """sorts the word and prints the first and last"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    