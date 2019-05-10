# import json
#
# my_json_obj1 = json.dumps({'id': 1, 'type': 'CCP', 'lengths': [30, 10, 10], 'pause': [20, 20]})
# my_json_obj2 = json.dumps({'id': 2, 'type': 'GDP', 'lengths': [20, 5, 10], 'pause': [10, 20]})
# my_json_obj3 = json.dumps({'id': 3, 'type': 'CCP', 'lengths': [30, 10, 10], 'pause': [20, 20]})
# my_json_obj4 = json.dumps({'id': 4, 'type': 'GDP', 'lengths': [20, 5, 10], 'pause': [10, 20]})
# my_json_obj5 = json.dumps({'id': 5, 'type': 'GDP', 'lengths': [20, 5, 10], 'pause': [10, 20]})
# my_json_obj6 = json.dumps({'id': 6, 'type': 'CCP', 'lengths': [30, 10, 10], 'pause': [20, 20]})
# my_json_obj7 = json.dumps({'id': 7, 'type': 'CCP', 'lengths': [30, 10, 10], 'pause': [20, 20]})
# my_json_obj8 = json.dumps({'id': 8, 'type': 'BBP', 'lengths': [20, 10, 10], 'pause': [10, 10]})
# my_json_obj9 = json.dumps({'id': 9, 'type': 'BPP', 'lengths': [20, 10, 10], 'pause': [10, 10]})
# my_json_obj10 = json.dumps({'id': 10, 'type': 'GDP', 'lengths': [20, 5, 10], 'pause': [10, 20]})
# my_json_obj11 = json.dumps({'id': 11, 'type': 'CCP', 'lengths': [30, 10, 10], 'pause': [20, 20]})
# my_json_obj12 = json.dumps({'id': 12, 'type': 'CCP', 'lengths': [30, 10, 10], 'pause': [20, 20]})
# my_json_obj13 = json.dumps({'id': 13, 'type': 'GDP', 'lengths': [20, 5, 10], 'pause': [10, 20]})
#
#
# y = json.loads(my_json_obj3)
# print(y["lengths"])

import os
import math


#
# Complete the simpleArraySum function below.
# summarize an array
def simpleArraySum(ar):
    total = 0
    for val in ar:
        total += val
    return total


def compareTriplets(a, b):
    alice_points, bob_points = 0, 0
    for alice, bob in zip(a, b):
        if alice > bob:
            alice_points += 1
        elif alice < bob:
            bob_points += 1
        else:
            continue
    print([alice_points, bob_points])


def aVeryBigSum(ar):
    total = 0
    yo = str(ar[0])
    n = int(yo[0])
    number = (str(ar[0])[1:])
    total_length = int(len(number) / n)
    for i in range(total_length):
        gek = number[:total_length]
        number = number[total_length:]
        try:
            total += (int(float(gek)))
        except:
            print(gek)
    return total


def aVeryBigSum2(ar):
    total = 0
    for val in ar:
        total += val
    return total


def diagonalDifference(arr):
    north_east = 0
    north_west = 0
    for y in range(0, len(arr)):
        north_east += arr[y][y]
        north_west += arr[y][len(arr) - y - 1]

    print("North east: " + str(north_east))
    print("North west: " + str(north_west))
    ans = abs(north_east - north_west)
    print("Ans: " + str(ans))

    # sample input:
    # 3
    # 11 2 4
    # 4 5 6
    # 10 8 -12
    # north_east = 0
    # north_west = 0
    # for y in range(0, len(arr)):
    #     north_east += arr[y][y]
    #     north_west += arr[y][len(arr)-y-1]
    #
    # return(abs(north_east - north_west))


# calculates fraction of ho many minus, 0 and positive integers in an array.
def plusMinus(arr):
    zeroes = 0
    negative = 0
    positive = 0
    array_length = len(arr)

    for x in range(0, array_length):
        if arr[x] < 0:
            negative += 1
        elif arr[x] == 0:
            zeroes += 1
        else:
            positive += 1

    print(float(positive) / float(array_length))
    print(float(negative) / float(array_length))
    print(float(zeroes) / float(array_length))


# The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of n =6.
def staircase(n):
    for x in range(0, n):
        a = " " * (n - x - 1)
        c = a + "#" * (x + 1)
        print(c)


def miniMaxSum(arr):
    arr.sort()
    highest = sum(arr[1:])
    lowest = sum(arr[:(len(arr) - 1)])
    print(str(lowest) + " " + str(highest))


# can only blow out the tallest candles, print how many of highest there are
def birthdayCakeCandles(ar):
    if len(ar) == 0:
        return 0
    ar.sort(reverse=True)
    x = ar[:1]
    othersum = 0
    for xx in ar:
        if x[0] == xx:
            othersum += 1
    return othersum


# 07:05:45PM to 19:05:45

def timeConversion(s):
    new_time = s
    new_time_PM_or_AM = new_time[-2:]
    if new_time_PM_or_AM == "PM":
        if int(new_time[:2]) == int(12):
            return new_time[:-2]

        new_hour = str(int(new_time[:2]) + 12)
        new_time = (new_hour + new_time[2:])[:-2]
        return new_time

    elif new_time_PM_or_AM == "AM":
        if int(new_time[:2]) == int(12):
            new_hour = str(int(new_time[:2]) - 12)
            new_time = "0" + (new_hour + new_time[2:])[:-2]
            return new_time

        return new_time[:-2]
    else:
        return new_time


def gradingStudents(grades):
    for grade in range(0, len(grades)):
        if grades[grade] < 38:
            continue
        if grades[grade] >= 38:
            check = (math.ceil(grades[grade] / 5)) * 5
            print(check)
            if check - grades[grade] < 3:
                grades[grade] = (math.ceil(grades[grade] / 5)) * 5
            elif check - grades[grade] == 3:
                grades[grade] = grades[grade]
    return grades


# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    orange_point = 0
    apple_point = 0

    for apple in range(0, len(apples)):
        if s <= (a + apples[apple]) <= t:
            apple_point += 1

    for orange in range(0, len(oranges)):
        if s <= (b + oranges[orange]) <= t:
            orange_point += 1

    print(apple_point)
    print(orange_point)


def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 >= v1:
        return ("NO")
    elif (x1 - x2) % (v2 - v1) == 0:
        return ("YES")
    else:
        return ("NO")


def breakingRecords(scores):
    new_max = 0
    new_low = 0
    current_high = scores[0]
    current_low = scores[0]
    for score in range(1, len(scores)):
        if scores[score] > current_high:
            current_high = scores[score]
            new_max += 1
        if scores[score] < current_low:
            current_low = scores[score]
            new_low += 1

    print(
        type(new_max)
    )
    return ((new_max), (new_low))


def birthday(s, d, m):
    # s = [1, 2, 1, 3, 2]
    ans = 0
    for square in range(0, len(s)):
        if sum(s[square:m + square]) == d and len(s[square:m + square]) == m:
            ans += 1
    return ans


def divisibleSumPairs(n, k, ar):
    ans = 0
    for y in range(0, n):
        for x in range(y + 1, n):
            if (ar[y] + ar[x]) % k == 0:
                # print(ar[y], ar[x])
                ans += 1
    return ans


def migratoryBirds(arr):
    count = [0] * len(arr)
    for t in map(int, arr):
        count[t] += 1
    return count.index(max(count))


def electionWinner(votes):
    dict_of_votes = {}
    try:
        for x in votes:
            if x not in dict_of_votes:
                dict_of_votes[x] = 1
            elif x in dict_of_votes:
                dict_of_votes[x] = dict_of_votes[x] + 1

        return max(zip(dict_of_votes.values(), dict_of_votes.keys()))[1]
    except:
        return "Something went wrong"

    # print(max(dict_of_votes))
    # print(dict_of_votes)
    # print(max(dict_of_votes, key=dict_of_votes.get))
    # print(dict_of_votes.index(max(dict_of_votes)))


if __name__ == '__main__':
    # a = [17, 28, 30]
    # b = [99, 16, 8]
    # compareTriplets(a, b)

    # ar = [510000000011000000002100000000310000000041000000005]

    # print(aVeryBigSum(ar))
    # arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # result = diagonalDifference(arr)

    # arr = [-4, 3, -9, 0, 4, 1]
    # plusMinus(arr)

    # n = 6
    # staircase(n)

    # arr = [2,3,1,6,4]
    # miniMaxSum(arr)

    # ar = [0, 1,3,5,6,6,6,7]
    # result = birthdayCakeCandles(ar)

    # s = "12:05:45PM"
    # p = "07:05:45AM"
    # k = "07:05:45"
    # q = "12:40:22AM"
    # print(timeConversion(s))
    # print(timeConversion(p))
    # print(timeConversion(k))
    # print(timeConversion(q))

    # grades = [73, 67, 38, 33]
    # gradingStudents(grades)

    # countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])

    # x1 = 0
    # v1 = 2
    # x2 = 5
    # v2 = 3
    # kangaroo(x1, v1, x2, v2)

    # [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    # scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    # breakingRecords(scores)

    # s = [1, 2, 1, 3, 2]
    # d = 3
    # m = 2
    # birthday(s, d, m)
    # n = 6
    # k = 3
    # ar = [1, 3, 2, 6, 1, 2]
    # divisibleSumPairs(n, k, ar)

    # arr = [1, 4, 4, 4, 5, 3]
    # arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
    # result = migratoryBirds(arr)

    votes = ["Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary"]
    votes2 = ["Victor", "Veronica", "Ryan", "Dave", "Maria", "Maria", "Farah", "Farah", "Ryan", "Veronica"]
    print(electionWinner(votes2))
