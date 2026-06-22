#!/usr/bin/env python3

from random import randint

def verif_tri(a_list):
    '''Verifies if a list has been sorted'''
    for i in range(1, len(a_list)):
        if a_list[i-1] > a_list[i]:
            return False
    return True


def tri_par_interjection(a_list):
    '''A very inefficient sort method that indexes randomly. Works on both lists of numbers and lists of strings.'''
    l = len(a_list)
    while verif_tri(a_list) is False: 
        # randomly choose first and second index
        i1 = randint(0, l-1)
        i2 = randint(0, l-1)
        # picks second index again if they are equal
        while i2 == i1:
            i2 = randint(0, l-1)
        # verify that first index is inferior to second index
        if i1 < i2 and a_list[i2] < a_list[i1]:
            # switch the positions of elements of first index and second index
            a_list[i1], a_list[i2] = a_list[i2], a_list[i1]
    return a_list


# usage example with smaller lists
if __name__ == "__main__":
    list_of_numbers = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    list_of_strings = ["kyoko", "brad", "jon", "cassie"]

    print(tri_par_interjection(list_of_numbers))
    print(tri_par_interjection(list_of_strings))


