# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    count_str = str(count)

    string_1 = 'Number of donuts: many'
    string_2 = 'Number of donuts: ' + count_str
    
    if count > 9:
        return string_1
    else:
        return string_2
    raise NotImplementedError


"""
Given an int count of a number of donuts, return a string of the
form 'Number of donuts: <count>', where <count> is the number
passed in. However, if the count is 10 or more, then use the word
'many' instead of the actual count.

>>> donuts(4)
'Number of donuts: 4'
>>> donuts(9)
'Number of donuts: 9'
>>> donuts(10)
'Number of donuts: many'
>>> donuts(99)
'Number of donuts: many'
"""

def both_ends(s):
    if len(s) < 2:
        return ''
    else:
        s_2 = s[0:2] + s[-2:len(s)]
        return s_2
    raise NotImplementedError


    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """



def fix_start(s):

    s_tail = s[1:]
    initial = s[0]
    word = ''

    for letter in s_tail:
        if letter == initial:
            word = word + '*'
        else:
            word = word + letter
    s_2 = s[0] + word

    print(s_2)


def mix_up(a, b):
    string_1 = a[0:2]
    string_2 = a[2:]
    string_3 = b[0:2]
    string_4 = b[2:]

    string_concat = string_3 + string_2 + ' ' + string_1 + string_4
    return string_concat

    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError


def verbing(s):
    if len(s) < 3:
        return s
    else:
        if s[-3:] == 'ing':
            s_new = s + 'ly'
        else:
            s_new = s + 'ing'
        return s_new

    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    raise NotImplementedError


def not_bad(s):

    not_loc = s.find('not')
    bad_loc = s.find('bad')

    if bad_loc > not_loc:
        s_new = s[:not_loc] + "good" + s[bad_loc + 3:]
        return s_new
    else:
        return s


    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError


def front_back(a, b):

    if len(a) % 2 == 0:
        a_front = a[:int(len(a) / 2)]
        a_back = a[int(len(a) / 2):]
    else:
        a_front = a[:int(len(a) / 2 + 0.5)]
        a_back = a[int(len(a) / 2 + 0.5):]

    if len(b) % 2 == 0:
        b_front = b[:int(len(b) / 2)]
        b_back = b[int(len(b) / 2):]
    else:
        b_front = b[:int(len(b) / 2 + 0.5)]
        b_back = b[int(len(b) / 2 + 0.5):]

    string_combi = a_front + b_front + a_back + b_back

    return string_combi

    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
