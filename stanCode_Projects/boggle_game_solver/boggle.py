"""
File: boggle.py
Name: Yutung
----------------------------------------
This program executes a game in which the
user enters a 4 by 4 square grid and finds
all valid words. It terminates when all the
valid words are found and the total number
of words found is calculated.
"""

import time  # This file allows you to calculate the speed of your algorithm

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    This program uses backtracking to recursively find words
    in a 4 by 4 square grid entered by the user.
    """
    start = time.time()
    ####################

    grid = []
    for i in range(4):
        row = input(f'{i+1} row of letters: ').lower().split()
        # Check if the input has a space between each letter
        if len(row) != 4:
            print('Illegal input')
            return
        grid.append(row)

    dictionary = read_dictionary()
    words_found = set()

    for i in range(4):
        for j in range(4):
            find_words(grid, i, j, '', dictionary, words_found)

    for word in words_found:
        print(f'Found: {word}')

    print(f'There are {len(words_found)} words in total.')

    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(grid, row, col, prefix, dictionary, words_found):
    """
    Recursive function to find words in the grid using backtracking.
    """
    if row < 0 or col < 0 or row >= 4 or col >= 4:
        return

    # Mark the current letter as visited
    letter = grid[row][col]
    grid[row][col] = '#'

    # Append the current letter to the prefix
    prefix += letter

    # Check if the prefix is a valid word or a prefix of a valid word
    if prefix in dictionary:
        words_found.add(prefix)

    if has_prefix(prefix, dictionary):
        # Explore the neighboring cells in all eight directions
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    find_words(grid, row + i, col + j, prefix, dictionary, words_found)

    # Restore the grid cell
    grid[row][col] = letter


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    dictionary = set()
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip().lower()
            if len(word) >= 4:
                dictionary.add(word)
    return dictionary


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :param dictionary: (set) A set of valid words that the user want to search for in the grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
