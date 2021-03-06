# -*- coding: utf-8 -*-

def break_words(stuff):
    """이 함수는 문자열을 단어로 쪼개 줍니다."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """단어를 정렬합니다."""
    return sorted(words)

def print_first_word(words):
    """첫 단어를 꺼내서 출력합니다."""
    word = words.pop(0)
    print word
    
def print_last_word(words):
    """마지막 단어를 꺼내서 출력합니다."""
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """한 문장을 통쨰로 받아 단어를 정렬해서 반환합니다."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """문장의 처음과 마지막 단어를 출력합니다."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """단어를 정렬하고 처음과 마지막 단어를 출력합니다."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
# 이렇게 함수를 지정해두면 내가 만든 '모듈'이 완성됨!
# 임의의 문장을 가지고 터미널에서 python을 실행해 결과를 관찰해 볼 것.
