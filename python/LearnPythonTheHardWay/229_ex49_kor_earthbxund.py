# -*- coding: utf-8 -*-


class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, object):
        # ('명사', '공주') 꼴의 튜플을 받아 변환합니다.
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop[0]

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, '제외')

    if peek(word_list) == '동사':
        return match(word_list, '동사')
    else:
        raise ParserError("동사가 나올 차례입니다.")


def parse_object(word_list):
    skip(word_list, '제외')
    next = peek(word_list)

    if next == '명사':
        return match(word_list, '명사')
    if next == '방향':
        return match(word_list, '방향')
    else:
        raise ParserError("명사나 방향이 나올 차례입니다.")


def parse_subject(word_list):
    try:
        obj = parse_object(word_list)
    except ParserError:
        # 명사가 하나만 있으면 주어가 아니라 목적어로 가정한다
        obj = subj
        # 주어가 없으면 플레이어로 가정한다
        subj = ('명사', '플레이어')
    verb = parse_verb(word_list)

    return Sentence(subj, verb, obj)


def parse_sentence(word_list):
    skip(word_list, '제외')

    start = peek(word_list)
    if start == '명사':
        subj = match(word_list, '명사')
        return parse_subject(word_list, subj)
    elif start == '방향' or start == '동사':
        # 주어가 없으면 플레이어로 가정한다
        return parse_subject(word_list, ('명사', '플레이어'))
    else:
        raise ParserError("%s가 아닌 주어, 목적어, 동사 가운데 하나로 시작해야 합니다." % start)
