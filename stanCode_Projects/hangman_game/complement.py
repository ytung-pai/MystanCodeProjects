"""
File: complement.py
Name: Yutung
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program generates the complementary string of 'A','T','C','G' in DNA.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna: str, characters are all CAPITAL
    :return: str, characters are all CAPITAL
    """
    if dna == "":
        complement = 'DNA strand is missing.'
    else:
        complement = ""
        for i in range(len(dna)):
            ch = dna[i]
            if ch == 'A':
                complement += 'T'
            if ch == 'T':
                complement += 'A'
            if ch == 'C':
                complement += 'G'
            if ch == 'G':
                complement += 'C'
    return complement



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
