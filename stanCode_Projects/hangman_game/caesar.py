"""
File: caesar.py
Name: Yutung
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This application uses a shifted alphabetic sequence to decrypt a given text.
    """
    s = int(input('Secret number: '))
    new_alphabet = ""
    new_alphabet += ALPHABET[len(ALPHABET)-s:]
    new_alphabet += ALPHABET[:len(ALPHABET)-s]
    c = str(input("What's the ciphered string? "))  # ciphered
    c = c.upper()
    d = ""
    for i in range(len(c)):
        if c[i] == ' ':
            d += ' '
        elif c[i] == '!':
            d += '!'
        else:
            i = new_alphabet.find(c[i])
            d += ALPHABET[i]

    print('The deciphered string is: '+d)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
