from math import *

# Get sum of divisors of a number
def get_sum_of_d(number) -> int:
    total = 0
    for i in range(1,ceil(number/2)+1):
        if number % i == 0:
            total += i
    return total

def make_dict(start :int, end: int) -> dict:
    dictionary = {}
    for i in range(start, end):
        dictionary[i] = get_sum_of_d(i)
    return dictionary

def get_amicables(dictionary:dict) -> int:
    total = 0
    item = list(dictionary.keys())[0]
    while item < len(dictionary):
        for i in range(0,len(dictionary)):
            if item == dictionary[i]:
                total += item + dictionary[item]
                dictionary.pop(item)
        """
        if dictionary[item] in dictionary:
            total += item + dictionary[item]
            #dictionary.pop(item)
        """
        item += 1
    return total


sum_per_num = make_dict(0,10000)
print(get_amicables(sum_per_num))

