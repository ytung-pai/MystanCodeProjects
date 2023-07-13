"""
File: hangman.py
Name: Yutung
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7
ALPHABET = 'ABCDEFGHIJKLMNOPQRXTUVWXYZ'


def main():
    """
    Algorithm:
    1. Set word, start_str
    2. Set up blank, guesses, guess, attempts
    3. Test input and save it in guesses
    4. Put everything in the while loop
    5. Put attempts into the game
    6. Show word
    """
    word = random_word()
    start_str = ""
    for i in range(len(word)):
        start_str += '-'
    blank = len(word)
    attempts = N_TURNS
    s = start_str
    print('The word looks like ' + s)
    answer = ""
    s2 = ""
    s3 = ""
    through = 0
    first = 1
    second = 0
    while blank > 0 and attempts > 0:
        s = ""
        print('You have ' + str(attempts) + ' wrong guesses left.')
        guess = input('Your guess: ').upper()
        if guess in word:
            for i in range(len(word)):
                    if word[i] == guess:
                        s += guess
                        answer += guess
                        through = 1
                    else:
                        s += '-'
                        through = 1
            if first == 1:
                s2 = s
                first = 0
            if second == 1 and s3 is "":
                if through == 1 and s2 != "":
                    for j in range(len(word)):
                        if s2[j] != '-' and s[j] == '-':
                            s3 += s2[j]
                        elif s2[j] == '-' and s[j] != '-':
                            s3 += guess
                        elif s2[j] == '-' and s[j] == '-':
                            s3 += '-'
                through = 0
                s2 = ""
                j = 0
            else:
                if s3 is not "":
                    through = 1
                else:
                    through = 0
            second = 1

            if through == 1 and s3 != "":
                for j in range(len(word)):
                    if s3[j] != '-' and s[j] == '-':
                        s2 += s3[j]
                    elif s3[j] == '-' and s[j] != '-':
                        s2 += guess
                    elif s3[j] == '-' and s[j] == '-':
                        s2 += '-'
                through = 0
                s3 = ""
                j = 0
            else:
                through = 0
            if answer == word:
                print('The word looks like ' + answer)
                break
            else:
                if s3 is "":
                    print('The word looks like ' + s2)

                elif s2 is "":
                    print('The word looks like ' + s3)

            print('You are correct!')
        else:
            attempts = attempts - 1
            print("There is no " + guess + "'s in the word.")
            if s2 is not "":
               print('The word looks like ' + s2)
            else:
                print('The word looks like ' + s3)

    # gets here when blank == 0 OR when attempts == 0
    if attempts == 0:
        print('You are completely hung : (')
    else:
        print('You win!')
    print('The word was: ' + word)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
