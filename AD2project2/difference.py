#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 2: Search String Replacement

Team Number:
Student Names:
'''
import unittest
# Sample matrix provided by us:
from string import ascii_lowercase
from collections import defaultdict

# from pandas import *


def char_position(letter):
    return ord(letter) - 97


def skip_cost(u, r):
    return 1


def insert_cost(u, r):
    return 1


def change_cost(x, y, u, r, R):
    if y == x and u[x - 1] == r[y - 1]:
        return 0
        print "boo"
    else:
        return R[u[x - 1]][r[y - 1]]


# Solution to part b:
def min_difference(u, r, R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int
    Pre:
    Post:
    Example: Let R be the resemblance matrix where every change and skip costs 1
             min_difference("dynamick","dynamic",R) ==> 3
    """
    # To get the resemblance between two letters, use code like this:
    # difference = R['a']['b']

    # while len(u) < len(r):
    #     u = u+str("-")
    # matrix = [[1000 for i in range(len(r) + 1)] for j in range(len(u) + 1)]
    # for i in range(len(r) + 1):
    #     matrix[0][i] = i
    # for i in range(len(u) + 1):
    #     matrix[i][0] = i
    # for y in range(1, len(r) + 1):
    #     for x in range(1, len(u) + 1):
    #         surr = []
    #         # if u[x - 1] == r[y - 1]:
    #         #     #     #     print u[y - 1] + " : " + r[x - 1]
    #         #     #     #     matrix[x][y] = matrix[x - 1][y - 1]
    #         #     #     # surr.append(matrix[x - 1][y - 1] + change_cost(x, y, u, r, R))  # + R[u[x - 1]][r[y - 1]])
    #         #     #     # matrix[x][y] = min(surr)
    #         #     cost = 0
    #         #     print "hej"
    #         # else:
    #         #     cost = R[u[x - 1]][r[y - 1]]
    #
    #         # surr.append(matrix[x - 1][y] + R[u[x - 1]][r[y - 1]])  # delete/skip
    #         # surr.append(matrix[x][y - 1] + R[u[x - 1]][r[y - 1]])  # insert
    #         # surr.append(matrix[x - 1][y - 1] + cost)  # insert
    #         # if y < len(u):
    #         #     print "uno"
    #         #     delete = matrix[x - 1][y] + 1
    #         #     insert = matrix[x][y - 1] + 1
    #         #     substitution = matrix[x - 1][y - 1] + change_cost(x, y, u, r, R)
    #         # else: -
    #         #om man kommer frpn vänster, ska vi sätta in nått, bindesträck.
    #         #uppifrån bindesträck på på r
    #         #snett uppifrån om det är samma 0 andndars R[x, y] annars lägg inte in på backtarack
    #
    #         delete = matrix[x - 1][y] + +change_cost(x, y, u, r, R)
    #         insert = matrix[x][y - 1] + change_cost(x, y, u, r, R)
    #         substitution = matrix[x - 1][y - 1] + change_cost(x, y, u, r, R)
    #
    #         matrix[x][y] = min(delete, insert, substitution)
    #         # matrix[x][y] = min(surr)  # R[u[x - 1]][r[y - 1]]
    #
    #         #   print "X-value: " + str(u[x - 1]) + " : " +"Y-value: " + str(r[y - 1]) + " cost: " + str(R[u[x - 1]][r[y - 1]])
    #         #   print "X-value: " + str(x) + " : " +"Y-value: " + str(y)
    #         #   print "Surrounding: " + str(surr)
    #         #
    #         #     # print u[x - 1] + "::::::" + r[y - 1]
    #         #     matrix[x][y] = (min(surr)
    #         #     # print R[u[x - 1]][r[y - 1]]
    #
    # # print hej
    # # print DataFrame(matrix)
    matrix = [[None for i in range(len(r) + 1)] for j in range(len(u) + 1)]
    matrix[0][0] = 0
    for i in range(1, len(r) + 1):
        matrix[0][i] = matrix[0][i - 1] + R['-'][r[i - 1]]
    for i in range(1, len(u) + 1):
        matrix[i][0] = matrix[i - 1][0] + R[u[i - 1]]['-']
    for x in range(1, len(u) + 1):
        for y in range(1, len(r) + 1):
            if u[x - 1] == r[y - 1]:
                matrix[x][y] = matrix[x - 1][y - 1]
            else:
                west = matrix[x][y - 1] + R['-'][r[y - 1]]
                north = matrix[x - 1][y] + R[u[x - 1]]['-']
                northWest = matrix[x - 1][y - 1] + R[u[x - 1]][r[y - 1]]
                matrix[x][y] = min(north, west, northWest)
    return matrix[len(u)][len(r)]


# Solution to part c:
def min_difference_align(u, r, R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int, string, string
    Pre:
    Post:
    Example: Let R be the resemblance matrix where every change and skip costs 1
             min_difference_align("dinamck","dynamic",R) ==>
                                    3, "dinam-ck", "dynamic-"
    """
    matrix = [[None for i in range(len(r) + 1)] for j in range(len(u) + 1)]
    matrix[0][0] = 0
    for i in range(1, len(r) + 1):
        matrix[0][i] = matrix[0][i - 1] + R['-'][r[i - 1]]
    for i in range(1, len(u) + 1):
        matrix[i][0] = matrix[i - 1][0] + R[u[i - 1]]['-']
    for x in range(1, len(u) + 1):
        for y in range(1, len(r) + 1):
            if u[x - 1] == r[y - 1]:
                matrix[x][y] = matrix[x - 1][y - 1]
            else:
                west = matrix[x][y - 1] + R['-'][r[y - 1]]
                north = matrix[x - 1][y] + R[u[x - 1]]['-']
                northWest = matrix[x - 1][y - 1] + R[u[x - 1]][r[y - 1]]
                matrix[x][y] = min(north, west, northWest)


    lenU = len(u)
    lenR = len(r)
    print "Lenngth of U = " + str(lenU)
    print "Lenngth of R = " + str(lenR)
    uu = u
    rr = r
    for x in range(len(u) + 1):
        for y in range(len(r) + 1):
            # print matrix[lenU - x][lenR - y]
            # print matrix[lenU - x - 1][lenR - y - 1]
            # print "staph"
            print x
            print y
            if matrix[lenU-x][lenR-y] == matrix[lenU-x-1][lenR-y-1]:
                print "nothing"
            elif matrix[lenU-x][lenR-y] == (matrix[lenU-x-1][lenR-y])+R[u[lenU-x-1]][r[lenR-y-1]]:
                print "substitution"
            elif matrix[lenU-x][lenR-y] == matrix[lenU-x-1][lenR-y]-R['-'][r[lenR-y]]:
                print "alfred is gay"
                uu = u[:x - 1] + '-' + u[x - 1:]
            elif matrix[lenU-x][lenR-y] == matrix[lenU-x][lenR-y-1] + R[r[lenR-y-1]]['-']:
                print "alfred is cool"
                rr = r[:y-1] + '-' + r[y-1:]

    print uu
    print rr
    # print DataFrame(matrix)
    return "hej"


def qwerty_distance():
    """Generates a QWERTY Manhattan distance resemblance matrix

    Costs for letter pairs are based on the Manhattan distance of the
    corresponding keys on a standard QWERTY keyboard.
    Costs for skipping a character depends on its placement on the keyboard:
    adding a character has a higher cost for keys on the outer edges,
    deleting a character has a higher cost for keys near the middle.

    Usage:
        R = qwerty_distance()
        R['a']['b']  # result: 5
    """
    from collections import defaultdict
    import math
    R = defaultdict(dict)
    R['-']['-'] = 0
    zones = ["dfghjk", "ertyuislcvbnm", "qwazxpo"]
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for num, content in enumerate(zones):
        for char in content:
            R['-'][char] = num + 1
            R[char]['-'] = 3 - num
    for a in ascii_lowercase:
        rowA = None
        posA = None
        for num, content in enumerate(keyboard):
            if a in content:
                rowA = num
                posA = content.index(a)
        for b in ascii_lowercase:
            for rowB, contentB in enumerate(keyboard):
                if b in contentB:
                    R[a][b] = int(math.fabs(rowB - rowA) + math.fabs(posA - contentB.index(b)))
    return R


# class MinDifferenceTest(unittest.TestCase):
#     """Test Suite for search string replacement problem
#
#     Any method named "test_something" will be run when this file is
#     executed. Use the sanity check as a template for adding your own test
#     cases if you wish.
#     (You may delete this class from your submitted solution.)
#     """
#
#     def test_diff_sanity(self):
#         """Difference sanity test
#
#         Given a simple resemblance matrix, test that the reported
#         difference is the expected minimum. Do NOT assume we will always
#         use this resemblance matrix when testing!
#         """
#         alphabet = ascii_lowercase + '-'
#         # The simplest (reasonable) resemblance matrix:
#         R = dict([(
#             a,
#             dict([(b, (0 if a == b else 1)) for b in alphabet])
#         ) for a in alphabet])
#         # Warning: we may (read: 'will') use another matrix!
#         self.assertEqual(min_difference("dinamck", "dynamic", R), 3)
#
#     # def test_align_sanity(self):
#     #     """Simple alignment
#     #
#     #     Passes if the returned alignment matches the expected one.
#     #     """
#     #     # QWERTY resemblance matrix:
#     #     R = qwerty_distance()
#     #     diff, u, r = min_difference_align("polynomial", "exponential", R)
#     #     # Warning: we may (read: 'will') use another matrix!
#     #     self.assertEqual(diff, 15)
#     #     # Warning: there may be other optimal matchings!
#     #     self.assertEqual(u, '--polyn-om-ial')
#     #     self.assertEqual(r, 'exp-o-ne-ntial')


if __name__ == '__main__':
    # A = defaultdict(type('dict'), {
    #     '-': {'-': 0, 'a': 3, 'c': 2, 'b': 2, 'e': 2, 'd': 1, 'g': 1, 'f': 1, 'i': 2, 'h': 1, 'k': 1, 'j': 1, 'm': 2,
    #           'l': 2, 'o': 3, 'n': 2, 'q': 3, 'p': 3, 's': 2, 'r': 2, 'u': 2, 't': 2, 'w': 3, 'v': 2, 'y': 2, 'x': 3,
    #           'z': 3},
    #     'a': {'-': 1, 'a': 0, 'c': 3, 'b': 5, 'e': 3, 'd': 2, 'g': 4, 'f': 3, 'i': 8, 'h': 5, 'k': 7, 'j': 6, 'm': 7,
    #           'l': 8, 'o': 9, 'n': 6, 'q': 1, 'p': 10, 's': 1, 'r': 4, 'u': 7, 't': 5, 'w': 2, 'v': 4, 'y': 6, 'x': 2,
    #           'z': 1},
    #     'c': {'-': 2, 'a': 3, 'c': 0, 'b': 2, 'e': 2, 'd': 1, 'g': 3, 'f': 2, 'i': 7, 'h': 4, 'k': 6, 'j': 5, 'm': 4,
    #           'l': 7, 'o': 8, 'n': 3, 'q': 4, 'p': 9, 's': 2, 'r': 3, 'u': 6, 't': 4, 'w': 3, 'v': 1, 'y': 5, 'x': 1,
    #           'z': 2},
    #     'b': {'-': 2, 'a': 5, 'c': 2, 'b': 0, 'e': 4, 'd': 3, 'g': 1, 'f': 2, 'i': 5, 'h': 2, 'k': 4, 'j': 3, 'm': 2,
    #           'l': 5, 'o': 6, 'n': 1, 'q': 6, 'p': 7, 's': 4, 'r': 3, 'u': 4, 't': 2, 'w': 5, 'v': 1, 'y': 3, 'x': 3,
    #           'z': 4},
    #     'e': {'-': 2, 'a': 3, 'c': 2, 'b': 4, 'e': 0, 'd': 1, 'g': 3, 'f': 2, 'i': 5, 'h': 4, 'k': 6, 'j': 5, 'm': 6,
    #           'l': 7, 'o': 6, 'n': 5, 'q': 2, 'p': 7, 's': 2, 'r': 1, 'u': 4, 't': 2, 'w': 1, 'v': 3, 'y': 3, 'x': 3,
    #           'z': 4},
    #     'd': {'-': 3, 'a': 2, 'c': 1, 'b': 3, 'e': 1, 'd': 0, 'g': 2, 'f': 1, 'i': 6, 'h': 3, 'k': 5, 'j': 4, 'm': 5,
    #           'l': 6, 'o': 7, 'n': 4, 'q': 3, 'p': 8, 's': 1, 'r': 2, 'u': 5, 't': 3, 'w': 2, 'v': 2, 'y': 4, 'x': 2,
    #           'z': 3},
    #     'g': {'-': 3, 'a': 4, 'c': 3, 'b': 1, 'e': 3, 'd': 2, 'g': 0, 'f': 1, 'i': 4, 'h': 1, 'k': 3, 'j': 2, 'm': 3,
    #           'l': 4, 'o': 5, 'n': 2, 'q': 5, 'p': 6, 's': 3, 'r': 2, 'u': 3, 't': 1, 'w': 4, 'v': 2, 'y': 2, 'x': 4,
    #           'z': 5},
    #     'f': {'-': 3, 'a': 3, 'c': 2, 'b': 2, 'e': 2, 'd': 1, 'g': 1, 'f': 0, 'i': 5, 'h': 2, 'k': 4, 'j': 3, 'm': 4,
    #           'l': 5, 'o': 6, 'n': 3, 'q': 4, 'p': 7, 's': 2, 'r': 1, 'u': 4, 't': 2, 'w': 3, 'v': 1, 'y': 3, 'x': 3,
    #           'z': 4},
    #     'i': {'-': 2, 'a': 8, 'c': 7, 'b': 5, 'e': 5, 'd': 6, 'g': 4, 'f': 5, 'i': 0, 'h': 3, 'k': 1, 'j': 2, 'm': 3,
    #           'l': 2, 'o': 1, 'n': 4, 'q': 7, 'p': 2, 's': 7, 'r': 4, 'u': 1, 't': 3, 'w': 6, 'v': 6, 'y': 2, 'x': 8,
    #           'z': 9},
    #     'h': {'-': 3, 'a': 5, 'c': 4, 'b': 2, 'e': 4, 'd': 3, 'g': 1, 'f': 2, 'i': 3, 'h': 0, 'k': 2, 'j': 1, 'm': 2,
    #           'l': 3, 'o': 4, 'n': 1, 'q': 6, 'p': 5, 's': 4, 'r': 3, 'u': 2, 't': 2, 'w': 5, 'v': 3, 'y': 1, 'x': 5,
    #           'z': 6},
    #     'k': {'-': 3, 'a': 7, 'c': 6, 'b': 4, 'e': 6, 'd': 5, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 0, 'j': 1, 'm': 2,
    #           'l': 1, 'o': 2, 'n': 3, 'q': 8, 'p': 3, 's': 6, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 5, 'y': 3, 'x': 7,
    #           'z': 8},
    #     'j': {'-': 3, 'a': 6, 'c': 5, 'b': 3, 'e': 5, 'd': 4, 'g': 2, 'f': 3, 'i': 2, 'h': 1, 'k': 1, 'j': 0, 'm': 1,
    #           'l': 2, 'o': 3, 'n': 2, 'q': 7, 'p': 4, 's': 5, 'r': 4, 'u': 1, 't': 3, 'w': 6, 'v': 4, 'y': 2, 'x': 6,
    #           'z': 7},
    #     'm': {'-': 2, 'a': 7, 'c': 4, 'b': 2, 'e': 6, 'd': 5, 'g': 3, 'f': 4, 'i': 3, 'h': 2, 'k': 2, 'j': 1, 'm': 0,
    #           'l': 3, 'o': 4, 'n': 1, 'q': 8, 'p': 5, 's': 6, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 3, 'y': 3, 'x': 5,
    #           'z': 6},
    #     'l': {'-': 2, 'a': 8, 'c': 7, 'b': 5, 'e': 7, 'd': 6, 'g': 4, 'f': 5, 'i': 2, 'h': 3, 'k': 1, 'j': 2, 'm': 3,
    #           'l': 0, 'o': 1, 'n': 4, 'q': 9, 'p': 2, 's': 7, 'r': 6, 'u': 3, 't': 5, 'w': 8, 'v': 6, 'y': 4, 'x': 8,
    #           'z': 9},
    #     'o': {'-': 1, 'a': 9, 'c': 8, 'b': 6, 'e': 6, 'd': 7, 'g': 5, 'f': 6, 'i': 1, 'h': 4, 'k': 2, 'j': 3, 'm': 4,
    #           'l': 1, 'o': 0, 'n': 5, 'q': 8, 'p': 1, 's': 8, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 7, 'y': 3, 'x': 9,
    #           'z': 10},
    #     'n': {'-': 2, 'a': 6, 'c': 3, 'b': 1, 'e': 5, 'd': 4, 'g': 2, 'f': 3, 'i': 4, 'h': 1, 'k': 3, 'j': 2, 'm': 1,
    #           'l': 4, 'o': 5, 'n': 0, 'q': 7, 'p': 6, 's': 5, 'r': 4, 'u': 3, 't': 3, 'w': 6, 'v': 2, 'y': 2, 'x': 4,
    #           'z': 5},
    #     'q': {'-': 1, 'a': 1, 'c': 4, 'b': 6, 'e': 2, 'd': 3, 'g': 5, 'f': 4, 'i': 7, 'h': 6, 'k': 8, 'j': 7, 'm': 8,
    #           'l': 9, 'o': 8, 'n': 7, 'q': 0, 'p': 9, 's': 2, 'r': 3, 'u': 6, 't': 4, 'w': 1, 'v': 5, 'y': 5, 'x': 3,
    #           'z': 2},
    #     'p': {'-': 1, 'a': 10, 'c': 9, 'b': 7, 'e': 7, 'd': 8, 'g': 6, 'f': 7, 'i': 2, 'h': 5, 'k': 3, 'j': 4, 'm': 5,
    #           'l': 2, 'o': 1, 'n': 6, 'q': 9, 'p': 0, 's': 9, 'r': 6, 'u': 3, 't': 5, 'w': 8, 'v': 8, 'y': 4, 'x': 10,
    #           'z': 11},
    #     's': {'-': 2, 'a': 1, 'c': 2, 'b': 4, 'e': 2, 'd': 1, 'g': 3, 'f': 2, 'i': 7, 'h': 4, 'k': 6, 'j': 5, 'm': 6,
    #           'l': 7, 'o': 8, 'n': 5, 'q': 2, 'p': 9, 's': 0, 'r': 3, 'u': 6, 't': 4, 'w': 1, 'v': 3, 'y': 5, 'x': 1,
    #           'z': 2},
    #     'r': {'-': 2, 'a': 4, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2, 'f': 1, 'i': 4, 'h': 3, 'k': 5, 'j': 4, 'm': 5,
    #           'l': 6, 'o': 5, 'n': 4, 'q': 3, 'p': 6, 's': 3, 'r': 0, 'u': 3, 't': 1, 'w': 2, 'v': 2, 'y': 2, 'x': 4,
    #           'z': 5},
    #     'u': {'-': 2, 'a': 7, 'c': 6, 'b': 4, 'e': 4, 'd': 5, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 2, 'j': 1, 'm': 2,
    #           'l': 3, 'o': 2, 'n': 3, 'q': 6, 'p': 3, 's': 6, 'r': 3, 'u': 0, 't': 2, 'w': 5, 'v': 5, 'y': 1, 'x': 7,
    #           'z': 8},
    #     't': {'-': 2, 'a': 5, 'c': 4, 'b': 2, 'e': 2, 'd': 3, 'g': 1, 'f': 2, 'i': 3, 'h': 2, 'k': 4, 'j': 3, 'm': 4,
    #           'l': 5, 'o': 4, 'n': 3, 'q': 4, 'p': 5, 's': 4, 'r': 1, 'u': 2, 't': 0, 'w': 3, 'v': 3, 'y': 1, 'x': 5,
    #           'z': 6},
    #     'w': {'-': 1, 'a': 2, 'c': 3, 'b': 5, 'e': 1, 'd': 2, 'g': 4, 'f': 3, 'i': 6, 'h': 5, 'k': 7, 'j': 6, 'm': 7,
    #           'l': 8, 'o': 7, 'n': 6, 'q': 1, 'p': 8, 's': 1, 'r': 2, 'u': 5, 't': 3, 'w': 0, 'v': 4, 'y': 4, 'x': 2,
    #           'z': 3},
    #     'v': {'-': 2, 'a': 4, 'c': 1, 'b': 1, 'e': 3, 'd': 2, 'g': 2, 'f': 1, 'i': 6, 'h': 3, 'k': 5, 'j': 4, 'm': 3,
    #           'l': 6, 'o': 7, 'n': 2, 'q': 5, 'p': 8, 's': 3, 'r': 2, 'u': 5, 't': 3, 'w': 4, 'v': 0, 'y': 4, 'x': 2,
    #           'z': 3},
    #     'y': {'-': 2, 'a': 6, 'c': 5, 'b': 3, 'e': 3, 'd': 4, 'g': 2, 'f': 3, 'i': 2, 'h': 1, 'k': 3, 'j': 2, 'm': 3,
    #           'l': 4, 'o': 3, 'n': 2, 'q': 5, 'p': 4, 's': 5, 'r': 2, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 0, 'x': 6,
    #           'z': 7},
    #     'x': {'-': 1, 'a': 2, 'c': 1, 'b': 3, 'e': 3, 'd': 2, 'g': 4, 'f': 3, 'i': 8, 'h': 5, 'k': 7, 'j': 6, 'm': 5,
    #           'l': 8, 'o': 9, 'n': 4, 'q': 3, 'p': 10, 's': 1, 'r': 4, 'u': 7, 't': 5, 'w': 2, 'v': 2, 'y': 6, 'x': 0,
    #           'z': 1},
    #     'z': {'-': 1, 'a': 1, 'c': 2, 'b': 4, 'e': 4, 'd': 3, 'g': 5, 'f': 4, 'i': 9, 'h': 6, 'k': 8, 'j': 7, 'm': 6,
    #           'l': 9, 'o': 10, 'n': 5, 'q': 2, 'p': 11, 's': 2, 'r': 5, 'u': 8, 't': 6, 'w': 3, 'v': 3, 'y': 7, 'x': 1,
    #           'z': 0}})
    # min_difference_align('njltszrqdwo', 'omifeqpls', A)
    # # Expected result:
    # # 22, njltszrq--dwo, omi-f-eqpls--
    #
    # B = defaultdict(type('dict'), {
    #     '-': {'-': 0, 'a': 3, 'c': 2, 'b': 2, 'e': 2, 'd': 1, 'g': 1, 'f': 1, 'i': 2, 'h': 1, 'k': 1, 'j': 1, 'm': 2,
    #           'l': 2, 'o': 3, 'n': 2, 'q': 3, 'p': 3, 's': 2, 'r': 2, 'u': 2, 't': 2, 'w': 3, 'v': 2, 'y': 2, 'x': 3,
    #           'z': 3},
    #     'a': {'-': 1, 'a': 0, 'c': 3, 'b': 5, 'e': 3, 'd': 2, 'g': 4, 'f': 3, 'i': 8, 'h': 5, 'k': 7, 'j': 6, 'm': 7,
    #           'l': 8, 'o': 9, 'n': 6, 'q': 1, 'p': 10, 's': 1, 'r': 4, 'u': 7, 't': 5, 'w': 2, 'v': 4, 'y': 6, 'x': 2,
    #           'z': 1},
    #     'c': {'-': 2, 'a': 3, 'c': 0, 'b': 2, 'e': 2, 'd': 1, 'g': 3, 'f': 2, 'i': 7, 'h': 4, 'k': 6, 'j': 5, 'm': 4,
    #           'l': 7, 'o': 8, 'n': 3, 'q': 4, 'p': 9, 's': 2, 'r': 3, 'u': 6, 't': 4, 'w': 3, 'v': 1, 'y': 5, 'x': 1,
    #           'z': 2},
    #     'b': {'-': 2, 'a': 5, 'c': 2, 'b': 0, 'e': 4, 'd': 3, 'g': 1, 'f': 2, 'i': 5, 'h': 2, 'k': 4, 'j': 3, 'm': 2,
    #           'l': 5, 'o': 6, 'n': 1, 'q': 6, 'p': 7, 's': 4, 'r': 3, 'u': 4, 't': 2, 'w': 5, 'v': 1, 'y': 3, 'x': 3,
    #           'z': 4},
    #     'e': {'-': 2, 'a': 3, 'c': 2, 'b': 4, 'e': 0, 'd': 1, 'g': 3, 'f': 2, 'i': 5, 'h': 4, 'k': 6, 'j': 5, 'm': 6,
    #           'l': 7, 'o': 6, 'n': 5, 'q': 2, 'p': 7, 's': 2, 'r': 1, 'u': 4, 't': 2, 'w': 1, 'v': 3, 'y': 3, 'x': 3,
    #           'z': 4},
    #     'd': {'-': 3, 'a': 2, 'c': 1, 'b': 3, 'e': 1, 'd': 0, 'g': 2, 'f': 1, 'i': 6, 'h': 3, 'k': 5, 'j': 4, 'm': 5,
    #           'l': 6, 'o': 7, 'n': 4, 'q': 3, 'p': 8, 's': 1, 'r': 2, 'u': 5, 't': 3, 'w': 2, 'v': 2, 'y': 4, 'x': 2,
    #           'z': 3},
    #     'g': {'-': 3, 'a': 4, 'c': 3, 'b': 1, 'e': 3, 'd': 2, 'g': 0, 'f': 1, 'i': 4, 'h': 1, 'k': 3, 'j': 2, 'm': 3,
    #           'l': 4, 'o': 5, 'n': 2, 'q': 5, 'p': 6, 's': 3, 'r': 2, 'u': 3, 't': 1, 'w': 4, 'v': 2, 'y': 2, 'x': 4,
    #           'z': 5},
    #     'f': {'-': 3, 'a': 3, 'c': 2, 'b': 2, 'e': 2, 'd': 1, 'g': 1, 'f': 0, 'i': 5, 'h': 2, 'k': 4, 'j': 3, 'm': 4,
    #           'l': 5, 'o': 6, 'n': 3, 'q': 4, 'p': 7, 's': 2, 'r': 1, 'u': 4, 't': 2, 'w': 3, 'v': 1, 'y': 3, 'x': 3,
    #           'z': 4},
    #     'i': {'-': 2, 'a': 8, 'c': 7, 'b': 5, 'e': 5, 'd': 6, 'g': 4, 'f': 5, 'i': 0, 'h': 3, 'k': 1, 'j': 2, 'm': 3,
    #           'l': 2, 'o': 1, 'n': 4, 'q': 7, 'p': 2, 's': 7, 'r': 4, 'u': 1, 't': 3, 'w': 6, 'v': 6, 'y': 2, 'x': 8,
    #           'z': 9},
    #     'h': {'-': 3, 'a': 5, 'c': 4, 'b': 2, 'e': 4, 'd': 3, 'g': 1, 'f': 2, 'i': 3, 'h': 0, 'k': 2, 'j': 1, 'm': 2,
    #           'l': 3, 'o': 4, 'n': 1, 'q': 6, 'p': 5, 's': 4, 'r': 3, 'u': 2, 't': 2, 'w': 5, 'v': 3, 'y': 1, 'x': 5,
    #           'z': 6},
    #     'k': {'-': 3, 'a': 7, 'c': 6, 'b': 4, 'e': 6, 'd': 5, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 0, 'j': 1, 'm': 2,
    #           'l': 1, 'o': 2, 'n': 3, 'q': 8, 'p': 3, 's': 6, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 5, 'y': 3, 'x': 7,
    #           'z': 8},
    #     'j': {'-': 3, 'a': 6, 'c': 5, 'b': 3, 'e': 5, 'd': 4, 'g': 2, 'f': 3, 'i': 2, 'h': 1, 'k': 1, 'j': 0, 'm': 1,
    #           'l': 2, 'o': 3, 'n': 2, 'q': 7, 'p': 4, 's': 5, 'r': 4, 'u': 1, 't': 3, 'w': 6, 'v': 4, 'y': 2, 'x': 6,
    #           'z': 7},
    #     'm': {'-': 2, 'a': 7, 'c': 4, 'b': 2, 'e': 6, 'd': 5, 'g': 3, 'f': 4, 'i': 3, 'h': 2, 'k': 2, 'j': 1, 'm': 0,
    #           'l': 3, 'o': 4, 'n': 1, 'q': 8, 'p': 5, 's': 6, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 3, 'y': 3, 'x': 5,
    #           'z': 6},
    #     'l': {'-': 2, 'a': 8, 'c': 7, 'b': 5, 'e': 7, 'd': 6, 'g': 4, 'f': 5, 'i': 2, 'h': 3, 'k': 1, 'j': 2, 'm': 3,
    #           'l': 0, 'o': 1, 'n': 4, 'q': 9, 'p': 2, 's': 7, 'r': 6, 'u': 3, 't': 5, 'w': 8, 'v': 6, 'y': 4, 'x': 8,
    #           'z': 9},
    #     'o': {'-': 1, 'a': 9, 'c': 8, 'b': 6, 'e': 6, 'd': 7, 'g': 5, 'f': 6, 'i': 1, 'h': 4, 'k': 2, 'j': 3, 'm': 4,
    #           'l': 1, 'o': 0, 'n': 5, 'q': 8, 'p': 1, 's': 8, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 7, 'y': 3, 'x': 9,
    #           'z': 10},
    #     'n': {'-': 2, 'a': 6, 'c': 3, 'b': 1, 'e': 5, 'd': 4, 'g': 2, 'f': 3, 'i': 4, 'h': 1, 'k': 3, 'j': 2, 'm': 1,
    #           'l': 4, 'o': 5, 'n': 0, 'q': 7, 'p': 6, 's': 5, 'r': 4, 'u': 3, 't': 3, 'w': 6, 'v': 2, 'y': 2, 'x': 4,
    #           'z': 5},
    #     'q': {'-': 1, 'a': 1, 'c': 4, 'b': 6, 'e': 2, 'd': 3, 'g': 5, 'f': 4, 'i': 7, 'h': 6, 'k': 8, 'j': 7, 'm': 8,
    #           'l': 9, 'o': 8, 'n': 7, 'q': 0, 'p': 9, 's': 2, 'r': 3, 'u': 6, 't': 4, 'w': 1, 'v': 5, 'y': 5, 'x': 3,
    #           'z': 2},
    #     'p': {'-': 1, 'a': 10, 'c': 9, 'b': 7, 'e': 7, 'd': 8, 'g': 6, 'f': 7, 'i': 2, 'h': 5, 'k': 3, 'j': 4, 'm': 5,
    #           'l': 2, 'o': 1, 'n': 6, 'q': 9, 'p': 0, 's': 9, 'r': 6, 'u': 3, 't': 5, 'w': 8, 'v': 8, 'y': 4, 'x': 10,
    #           'z': 11},
    #     's': {'-': 2, 'a': 1, 'c': 2, 'b': 4, 'e': 2, 'd': 1, 'g': 3, 'f': 2, 'i': 7, 'h': 4, 'k': 6, 'j': 5, 'm': 6,
    #           'l': 7, 'o': 8, 'n': 5, 'q': 2, 'p': 9, 's': 0, 'r': 3, 'u': 6, 't': 4, 'w': 1, 'v': 3, 'y': 5, 'x': 1,
    #           'z': 2},
    #     'r': {'-': 2, 'a': 4, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2, 'f': 1, 'i': 4, 'h': 3, 'k': 5, 'j': 4, 'm': 5,
    #           'l': 6, 'o': 5, 'n': 4, 'q': 3, 'p': 6, 's': 3, 'r': 0, 'u': 3, 't': 1, 'w': 2, 'v': 2, 'y': 2, 'x': 4,
    #           'z': 5},
    #     'u': {'-': 2, 'a': 7, 'c': 6, 'b': 4, 'e': 4, 'd': 5, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 2, 'j': 1, 'm': 2,
    #           'l': 3, 'o': 2, 'n': 3, 'q': 6, 'p': 3, 's': 6, 'r': 3, 'u': 0, 't': 2, 'w': 5, 'v': 5, 'y': 1, 'x': 7,
    #           'z': 8},
    #     't': {'-': 2, 'a': 5, 'c': 4, 'b': 2, 'e': 2, 'd': 3, 'g': 1, 'f': 2, 'i': 3, 'h': 2, 'k': 4, 'j': 3, 'm': 4,
    #           'l': 5, 'o': 4, 'n': 3, 'q': 4, 'p': 5, 's': 4, 'r': 1, 'u': 2, 't': 0, 'w': 3, 'v': 3, 'y': 1, 'x': 5,
    #           'z': 6},
    #     'w': {'-': 1, 'a': 2, 'c': 3, 'b': 5, 'e': 1, 'd': 2, 'g': 4, 'f': 3, 'i': 6, 'h': 5, 'k': 7, 'j': 6, 'm': 7,
    #           'l': 8, 'o': 7, 'n': 6, 'q': 1, 'p': 8, 's': 1, 'r': 2, 'u': 5, 't': 3, 'w': 0, 'v': 4, 'y': 4, 'x': 2,
    #           'z': 3},
    #     'v': {'-': 2, 'a': 4, 'c': 1, 'b': 1, 'e': 3, 'd': 2, 'g': 2, 'f': 1, 'i': 6, 'h': 3, 'k': 5, 'j': 4, 'm': 3,
    #           'l': 6, 'o': 7, 'n': 2, 'q': 5, 'p': 8, 's': 3, 'r': 2, 'u': 5, 't': 3, 'w': 4, 'v': 0, 'y': 4, 'x': 2,
    #           'z': 3},
    #     'y': {'-': 2, 'a': 6, 'c': 5, 'b': 3, 'e': 3, 'd': 4, 'g': 2, 'f': 3, 'i': 2, 'h': 1, 'k': 3, 'j': 2, 'm': 3,
    #           'l': 4, 'o': 3, 'n': 2, 'q': 5, 'p': 4, 's': 5, 'r': 2, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 0, 'x': 6,
    #           'z': 7},
    #     'x': {'-': 1, 'a': 2, 'c': 1, 'b': 3, 'e': 3, 'd': 2, 'g': 4, 'f': 3, 'i': 8, 'h': 5, 'k': 7, 'j': 6, 'm': 5,
    #           'l': 8, 'o': 9, 'n': 4, 'q': 3, 'p': 10, 's': 1, 'r': 4, 'u': 7, 't': 5, 'w': 2, 'v': 2, 'y': 6, 'x': 0,
    #           'z': 1},
    #     'z': {'-': 1, 'a': 1, 'c': 2, 'b': 4, 'e': 4, 'd': 3, 'g': 5, 'f': 4, 'i': 9, 'h': 6, 'k': 8, 'j': 7, 'm': 6,
    #           'l': 9, 'o': 10, 'n': 5, 'q': 2, 'p': 11, 's': 2, 'r': 5, 'u': 8, 't': 6, 'w': 3, 'v': 3, 'y': 7, 'x': 1,
    #           'z': 0}})
    # min_difference_align('pbqngmt', 'gmukwsoynfjqzhp', B)
    # # Expected result:
    # # 28, -pb--q---ngm--t-, g-mukwsoynfjqzhp
    #
    #
    #
    # D = defaultdict(type('dict'), {
    #     '-': {'-': 0, 'a': 3, 'c': 2, 'b': 2, 'e': 2, 'd': 1, 'g': 1, 'f': 1, 'i': 2, 'h': 1, 'k': 1, 'j': 1, 'm': 2,
    #           'l': 2, 'o': 3, 'n': 2, 'q': 3, 'p': 3, 's': 2, 'r': 2, 'u': 2, 't': 2, 'w': 3, 'v': 2, 'y': 2, 'x': 3,
    #           'z': 3},
    #     'a': {'-': 1, 'a': 0, 'c': 3, 'b': 5, 'e': 3, 'd': 2, 'g': 4, 'f': 3, 'i': 8, 'h': 5, 'k': 7, 'j': 6, 'm': 7,
    #           'l': 8, 'o': 9, 'n': 6, 'q': 1, 'p': 10, 's': 1, 'r': 4, 'u': 7, 't': 5, 'w': 2, 'v': 4, 'y': 6, 'x': 2,
    #           'z': 1},
    #     'c': {'-': 2, 'a': 3, 'c': 0, 'b': 2, 'e': 2, 'd': 1, 'g': 3, 'f': 2, 'i': 7, 'h': 4, 'k': 6, 'j': 5, 'm': 4,
    #           'l': 7, 'o': 8, 'n': 3, 'q': 4, 'p': 9, 's': 2, 'r': 3, 'u': 6, 't': 4, 'w': 3, 'v': 1, 'y': 5, 'x': 1,
    #           'z': 2},
    #     'b': {'-': 2, 'a': 5, 'c': 2, 'b': 0, 'e': 4, 'd': 3, 'g': 1, 'f': 2, 'i': 5, 'h': 2, 'k': 4, 'j': 3, 'm': 2,
    #           'l': 5, 'o': 6, 'n': 1, 'q': 6, 'p': 7, 's': 4, 'r': 3, 'u': 4, 't': 2, 'w': 5, 'v': 1, 'y': 3, 'x': 3,
    #           'z': 4},
    #     'e': {'-': 2, 'a': 3, 'c': 2, 'b': 4, 'e': 0, 'd': 1, 'g': 3, 'f': 2, 'i': 5, 'h': 4, 'k': 6, 'j': 5, 'm': 6,
    #           'l': 7, 'o': 6, 'n': 5, 'q': 2, 'p': 7, 's': 2, 'r': 1, 'u': 4, 't': 2, 'w': 1, 'v': 3, 'y': 3, 'x': 3,
    #           'z': 4},
    #     'd': {'-': 3, 'a': 2, 'c': 1, 'b': 3, 'e': 1, 'd': 0, 'g': 2, 'f': 1, 'i': 6, 'h': 3, 'k': 5, 'j': 4, 'm': 5,
    #           'l': 6, 'o': 7, 'n': 4, 'q': 3, 'p': 8, 's': 1, 'r': 2, 'u': 5, 't': 3, 'w': 2, 'v': 2, 'y': 4, 'x': 2,
    #           'z': 3},
    #     'g': {'-': 3, 'a': 4, 'c': 3, 'b': 1, 'e': 3, 'd': 2, 'g': 0, 'f': 1, 'i': 4, 'h': 1, 'k': 3, 'j': 2, 'm': 3,
    #           'l': 4, 'o': 5, 'n': 2, 'q': 5, 'p': 6, 's': 3, 'r': 2, 'u': 3, 't': 1, 'w': 4, 'v': 2, 'y': 2, 'x': 4,
    #           'z': 5},
    #     'f': {'-': 3, 'a': 3, 'c': 2, 'b': 2, 'e': 2, 'd': 1, 'g': 1, 'f': 0, 'i': 5, 'h': 2, 'k': 4, 'j': 3, 'm': 4,
    #           'l': 5, 'o': 6, 'n': 3, 'q': 4, 'p': 7, 's': 2, 'r': 1, 'u': 4, 't': 2, 'w': 3, 'v': 1, 'y': 3, 'x': 3,
    #           'z': 4},
    #     'i': {'-': 2, 'a': 8, 'c': 7, 'b': 5, 'e': 5, 'd': 6, 'g': 4, 'f': 5, 'i': 0, 'h': 3, 'k': 1, 'j': 2, 'm': 3,
    #           'l': 2, 'o': 1, 'n': 4, 'q': 7, 'p': 2, 's': 7, 'r': 4, 'u': 1, 't': 3, 'w': 6, 'v': 6, 'y': 2, 'x': 8,
    #           'z': 9},
    #     'h': {'-': 3, 'a': 5, 'c': 4, 'b': 2, 'e': 4, 'd': 3, 'g': 1, 'f': 2, 'i': 3, 'h': 0, 'k': 2, 'j': 1, 'm': 2,
    #           'l': 3, 'o': 4, 'n': 1, 'q': 6, 'p': 5, 's': 4, 'r': 3, 'u': 2, 't': 2, 'w': 5, 'v': 3, 'y': 1, 'x': 5,
    #           'z': 6},
    #     'k': {'-': 3, 'a': 7, 'c': 6, 'b': 4, 'e': 6, 'd': 5, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 0, 'j': 1, 'm': 2,
    #           'l': 1, 'o': 2, 'n': 3, 'q': 8, 'p': 3, 's': 6, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 5, 'y': 3, 'x': 7,
    #           'z': 8},
    #     'j': {'-': 3, 'a': 6, 'c': 5, 'b': 3, 'e': 5, 'd': 4, 'g': 2, 'f': 3, 'i': 2, 'h': 1, 'k': 1, 'j': 0, 'm': 1,
    #           'l': 2, 'o': 3, 'n': 2, 'q': 7, 'p': 4, 's': 5, 'r': 4, 'u': 1, 't': 3, 'w': 6, 'v': 4, 'y': 2, 'x': 6,
    #           'z': 7},
    #     'm': {'-': 2, 'a': 7, 'c': 4, 'b': 2, 'e': 6, 'd': 5, 'g': 3, 'f': 4, 'i': 3, 'h': 2, 'k': 2, 'j': 1, 'm': 0,
    #           'l': 3, 'o': 4, 'n': 1, 'q': 8, 'p': 5, 's': 6, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 3, 'y': 3, 'x': 5,
    #           'z': 6},
    #     'l': {'-': 2, 'a': 8, 'c': 7, 'b': 5, 'e': 7, 'd': 6, 'g': 4, 'f': 5, 'i': 2, 'h': 3, 'k': 1, 'j': 2, 'm': 3,
    #           'l': 0, 'o': 1, 'n': 4, 'q': 9, 'p': 2, 's': 7, 'r': 6, 'u': 3, 't': 5, 'w': 8, 'v': 6, 'y': 4, 'x': 8,
    #           'z': 9},
    #     'o': {'-': 1, 'a': 9, 'c': 8, 'b': 6, 'e': 6, 'd': 7, 'g': 5, 'f': 6, 'i': 1, 'h': 4, 'k': 2, 'j': 3, 'm': 4,
    #           'l': 1, 'o': 0, 'n': 5, 'q': 8, 'p': 1, 's': 8, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 7, 'y': 3, 'x': 9,
    #           'z': 10},
    #     'n': {'-': 2, 'a': 6, 'c': 3, 'b': 1, 'e': 5, 'd': 4, 'g': 2, 'f': 3, 'i': 4, 'h': 1, 'k': 3, 'j': 2, 'm': 1,
    #           'l': 4, 'o': 5, 'n': 0, 'q': 7, 'p': 6, 's': 5, 'r': 4, 'u': 3, 't': 3, 'w': 6, 'v': 2, 'y': 2, 'x': 4,
    #           'z': 5},
    #     'q': {'-': 1, 'a': 1, 'c': 4, 'b': 6, 'e': 2, 'd': 3, 'g': 5, 'f': 4, 'i': 7, 'h': 6, 'k': 8, 'j': 7, 'm': 8,
    #           'l': 9, 'o': 8, 'n': 7, 'q': 0, 'p': 9, 's': 2, 'r': 3, 'u': 6, 't': 4, 'w': 1, 'v': 5, 'y': 5, 'x': 3,
    #           'z': 2},
    #     'p': {'-': 1, 'a': 10, 'c': 9, 'b': 7, 'e': 7, 'd': 8, 'g': 6, 'f': 7, 'i': 2, 'h': 5, 'k': 3, 'j': 4, 'm': 5,
    #           'l': 2, 'o': 1, 'n': 6, 'q': 9, 'p': 0, 's': 9, 'r': 6, 'u': 3, 't': 5, 'w': 8, 'v': 8, 'y': 4, 'x': 10,
    #           'z': 11},
    #     's': {'-': 2, 'a': 1, 'c': 2, 'b': 4, 'e': 2, 'd': 1, 'g': 3, 'f': 2, 'i': 7, 'h': 4, 'k': 6, 'j': 5, 'm': 6,
    #           'l': 7, 'o': 8, 'n': 5, 'q': 2, 'p': 9, 's': 0, 'r': 3, 'u': 6, 't': 4, 'w': 1, 'v': 3, 'y': 5, 'x': 1,
    #           'z': 2},
    #     'r': {'-': 2, 'a': 4, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2, 'f': 1, 'i': 4, 'h': 3, 'k': 5, 'j': 4, 'm': 5,
    #           'l': 6, 'o': 5, 'n': 4, 'q': 3, 'p': 6, 's': 3, 'r': 0, 'u': 3, 't': 1, 'w': 2, 'v': 2, 'y': 2, 'x': 4,
    #           'z': 5},
    #     'u': {'-': 2, 'a': 7, 'c': 6, 'b': 4, 'e': 4, 'd': 5, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 2, 'j': 1, 'm': 2,
    #           'l': 3, 'o': 2, 'n': 3, 'q': 6, 'p': 3, 's': 6, 'r': 3, 'u': 0, 't': 2, 'w': 5, 'v': 5, 'y': 1, 'x': 7,
    #           'z': 8},
    #     't': {'-': 2, 'a': 5, 'c': 4, 'b': 2, 'e': 2, 'd': 3, 'g': 1, 'f': 2, 'i': 3, 'h': 2, 'k': 4, 'j': 3, 'm': 4,
    #           'l': 5, 'o': 4, 'n': 3, 'q': 4, 'p': 5, 's': 4, 'r': 1, 'u': 2, 't': 0, 'w': 3, 'v': 3, 'y': 1, 'x': 5,
    #           'z': 6},
    #     'w': {'-': 1, 'a': 2, 'c': 3, 'b': 5, 'e': 1, 'd': 2, 'g': 4, 'f': 3, 'i': 6, 'h': 5, 'k': 7, 'j': 6, 'm': 7,
    #           'l': 8, 'o': 7, 'n': 6, 'q': 1, 'p': 8, 's': 1, 'r': 2, 'u': 5, 't': 3, 'w': 0, 'v': 4, 'y': 4, 'x': 2,
    #           'z': 3},
    #     'v': {'-': 2, 'a': 4, 'c': 1, 'b': 1, 'e': 3, 'd': 2, 'g': 2, 'f': 1, 'i': 6, 'h': 3, 'k': 5, 'j': 4, 'm': 3,
    #           'l': 6, 'o': 7, 'n': 2, 'q': 5, 'p': 8, 's': 3, 'r': 2, 'u': 5, 't': 3, 'w': 4, 'v': 0, 'y': 4, 'x': 2,
    #           'z': 3},
    #     'y': {'-': 2, 'a': 6, 'c': 5, 'b': 3, 'e': 3, 'd': 4, 'g': 2, 'f': 3, 'i': 2, 'h': 1, 'k': 3, 'j': 2, 'm': 3,
    #           'l': 4, 'o': 3, 'n': 2, 'q': 5, 'p': 4, 's': 5, 'r': 2, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 0, 'x': 6,
    #           'z': 7},
    #     'x': {'-': 1, 'a': 2, 'c': 1, 'b': 3, 'e': 3, 'd': 2, 'g': 4, 'f': 3, 'i': 8, 'h': 5, 'k': 7, 'j': 6, 'm': 5,
    #           'l': 8, 'o': 9, 'n': 4, 'q': 3, 'p': 10, 's': 1, 'r': 4, 'u': 7, 't': 5, 'w': 2, 'v': 2, 'y': 6, 'x': 0,
    #           'z': 1},
    #     'z': {'-': 1, 'a': 1, 'c': 2, 'b': 4, 'e': 4, 'd': 3, 'g': 5, 'f': 4, 'i': 9, 'h': 6, 'k': 8, 'j': 7, 'm': 6,
    #           'l': 9, 'o': 10, 'n': 5, 'q': 2, 'p': 11, 's': 2, 'r': 5, 'u': 8, 't': 6, 'w': 3, 'v': 3, 'y': 7, 'x': 1,
    #           'z': 0}})
    # min_difference_align('gqaxrekwjufs', 'orgktqdfsuhpmjybnil', D)
    # # Expected result:
    # # 34, ----gqaxre---kwjuf---s, orgktq-dfsuhpm-jybnil-
