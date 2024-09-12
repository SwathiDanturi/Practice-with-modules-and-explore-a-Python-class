"""
Test Sentence methods.
File: tests.py
Initial developers: COMP 801 Instructors
Created: February 2024
Developer(s): Swathi
Conllaborator(s):
Date: 9/12/2024
"""
import pytest

from sentence import Sentence


def test_only_integers_4_1():
    """
    Test sentence that has 4 words, one of which is an integer.
    """
    test_sentence = 'happy new 2024 year'
    s_obj = Sentence(test_sentence)
    expected = '2024'
    s_obj.only_integers()
    actual = s_obj.sentence
    assert actual == expected


def test_only_words_4_1_1():
    """
    Test sentence that has 4 words, one of which is an integer, and another
    one has digits and other characters.
    """


def test_filter_words_4_2_2():
    """
    Test sentence that has 4 words, including 2 words in the word_lst of
    of length 2
    """


def test_filter_words_4_0_3():
    """
    Test sentence that has 4 words, none of which is in the word_lst of length
    3
    """


pytest.main()
