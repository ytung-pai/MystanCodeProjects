"""
File: hailstone.py
Name: Yutung
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This is a program representing Hailstone Sequence.
    """
    print('This program computes Hailstone sequences.')
    number_list = []
    n = int(input('Enter a number: '))
    while n != 1:
        if n % 2 == 1:
            print(str(n) + ' is odd, so I make 3n+1: ' + str(3 * n + 1))
            n = 3 * n + 1  # reassign n and get back to while loop
            number_list.append(n)
        else:
            print(str(n) + ' is even, so I take half: ' + str(n // 2))
            n = n // 2
            number_list.append(n)
    print('It took '+str(len(number_list))+' steps to reach 1.')

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
