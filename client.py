"""
File: client.py
Initial developers: COMP 801 instructors
Developer: Swathi
Collaborator(s):
Date: 9/12/2024
"""
from sentence import Sentence


def main():
    """
    Check the functionality of `Sentence` class.
    """
    s_obj = Sentence('Welcome to the week 3 class, assignment 2 is submitted')
    wordslist = ['the', 'week']
    s_obj.filter_words(wordslist)
    print(s_obj.sentence)
    s_obj.only_integers()
    print(s_obj.sentence)


main()
