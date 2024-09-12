"""
Practice with modules and explore a Python class.
File: sentence.py
Initial developers: COMP 801 instructors
Created: February 2024
Developer: Swathi
Collaborator(s):
Date: 9/12/2024
"""


class Sentence:
    """
    Encapsulate sentence transformations.
    Instance variable: `self.sentence` of type str
    """

    def __init__(self, sentence):
        """
        Create and initialize Sentence object with `sentence`value
        :param sentence: string, has words separated by spaces
        """
        self.sentence = sentence

    def size(self) -> int:
        """
        Return how many characters are in self.sentence.
        """
        return len(self.sentence)

    def remove_extra_spaces(self):
        """
        Remove extra spaces between the words in `self.sentence`.
        """
        word_lst = self.sentence.split()
        self.sentence = " ".join(word_lst)

    def only_integers(self):
        """
        Update `self.sentence` such that is has only integers.

        Example 1: if `self.sentence` is 'happy new 2024 year', then calling
        the method updates `self.sentence` with '2024'.

        Example 2: 'happy 1st UNH semester in spring 2024' will become '2024'

        Requirements:
            Apply the accumulation pattern
            Use appropriate str methods

        Hint: Generate a list of words from `self.sentence` using the str
        split() method.
        """

    def filter_words(self, word_lst):
        """
        Update `self.sentence` such that it does not have the words in
        `word_lst`.

        Example:
        If `self.sentence` has 'umm learn aah python', and `word_lst` has
        ['umm', 'aah'], updated `self.sentence` is 'learn python'.

        Hint: Generate a list of words from `self.sentence` using the str
        split() method.
        """
