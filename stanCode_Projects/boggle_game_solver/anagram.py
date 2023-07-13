"""
File: anagram.py
Name: Yutung
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    This program finds the anagrams for the word input by the user.
    It iteratively generates all the anagrams found and outputs the
    number of anagrams along with a list.
    """
    start = time.time()
    ####################
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    anagrams = []
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break
        print('Searching...')
        anagrams = find_anagrams(word)
        print(f'{len(anagrams)} anagrams:  {anagrams}')
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    """
    :return: list
    """
    with open(FILE) as f:
        dictionary = [line.strip() for line in f]
    return dictionary


def find_anagrams(s):
    """
    :param s: str
    :return anagrams: list
    """
    dictionary = read_dictionary()
    anagrams = []
    search_anagrams('', s, dictionary, anagrams)
    return anagrams


def search_anagrams(current, remaining, dictionary, anagrams):
    """
    :param current: str
    :param remaining: str
    :param dictionary: list
    :param anagrams: list
    """
    if len(remaining) == 0:
        if current in dictionary and current not in anagrams:
            print(f'Found:  {current}')
            print('Searching...')
            anagrams.append(current)
    else:
        for i in range(len(remaining)):
            search_anagrams(current + remaining[i], remaining[:i] + remaining[i+1:], dictionary, anagrams)


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: str
    :param dictionary: dict
    :return: bool
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
