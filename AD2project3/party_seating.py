#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 3: Party seating problem

Team Number: 22
Student Names: Christoffer Falkovén, Alfred Lindholm
'''
import unittest
import random as rand


# If your solution needs a queue, you can use this one:
# from collections import deque

def party(known):
    """
    Sig:    int[1..m, 1..n] ==> boolean, int[1..j], int[1..k]
    Pre:
    Post:
    Ex:     [[1,2],[0],[0]] ==> True, [0], [1,2]
    """
    # Initialize an empty list representing people sitting on table one
    listTableOne = []
    # Initialize an empty list representing people sitting on table two
    listTableTwo = []
    # The amount of guests
    length = len(known)
    # Initialize a list with None that is the same length as the amount of guests specifically for table one
    tableOne = [None] * length
    # Initialize a list with None that is the same length as the amount of guests specifically for table two
    tableTwo = [None] * length
    # A list of all guests initialized at False in order to keep track of the ones already seated
    visited = [False] * length
    # Seat guest 0 on Table One as a jump off point
    tableOne[0] = True

    # Go through each guest and call the auxiliary function if that guest hasn't already been seated
    # if no seating could be found, return False and two empty lists. If every Guest is successfully placed,
    # return true and the seating lists.
    for guest in range(0, length):
        '''
        Variant:Amount of Guests in known
        '''
        if not visited[guest]:
            seating = party_aux(guest, known, tableOne, tableTwo, listTableOne, listTableTwo, visited)
            if not seating:
                return False, [], []

    return True, listTableOne, listTableTwo


def party_aux(guest, known, currentTable, otherTable, currentTableList, otherTableList, visited):
    """
        Sig:    int ,int[1..m, 1..n], boolean[], boolean[], int[], int[], boolean[] ==> boolean
        Pre:
        Post:
    """
    # Assign Guest to the current table seating list
    currentTableList.append(guest)
    # Sign the Guest as sitting on the current table
    currentTable[guest] = True
    # Sign the Guest as not sitting on the other table
    otherTable[guest] = False
    # Assign the guest as seated
    visited[guest] = True

    # Start a loop for each of the´other guests that the current guests knows and then recursively go
    # through them, checking each of the acquaintances guests in turn as well.
    for acquaintance in known[guest]:
        '''
        Variant: amount of acquaintances
        '''
        if currentTable[acquaintance]:
            return False
        elif not visited[acquaintance]:
            tableHop = party_aux(acquaintance, known, otherTable, currentTable, otherTableList, currentTableList,
                                 visited)
            if not tableHop:
                return tableHop

    return True


class PartySeatingTest(unittest.TestCase):
    """Test suite for party seating problem
    """

    def test_sanity(self):
        """Sanity test

        A minimal test case.
        """
        K = [[1, 2], [0], [0]]
        (found, A, B) = party(K)
        self.assertEqual(
            len(A) + len(B),
            len(K),
            "wrong number of guests: {!s} guests, tables hold {!s} and {!s}".format(
                len(K),
                len(A),
                len(B)
            )
        )
        for g in range(len(K)):
            self.assertTrue(
                g in A or g in B,
                "Guest {!s} not seated anywhere".format(g))
        for a1 in A:
            for a2 in A:
                self.assertFalse(
                    a2 in K[a1],
                    "Guests {!s} and {!s} seated together, and know each other".format(
                        a1,
                        a2
                    )
                )
        for b1 in B:
            for b2 in B:
                self.assertFalse(
                    b2 in K[b1],
                    "Guests {!s} and {!s} seated together, and know each other".format(
                        b1,
                        b2
                    )
                )


if __name__ == '__main__':
    unittest.main()
