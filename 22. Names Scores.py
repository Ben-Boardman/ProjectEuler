"""
https://projecteuler.net/problem=22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth, is the th name in the list. So, COLIN would obtain a score of

What is the total of all the name scores in the file?
"""

import csv

# Get the name file
file = open("22 names.txt")

# Run the file through a csv reader
reader = csv.reader(file)

# new list
name_list = []

# populate with reader contents
for i in reader:
    name_list.append(i)

# for some reason all the list was in the first index
name_list = name_list[0]

# sort the list alphabetically
name_list.sort()

# make all letters lower case
name_list = [x.lower() for x in name_list]

# create a dict for the values to lookup
letter_values  = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26 
}

def word_value(word) -> int:
    value = 0
    for i in word:
        value += letter_values[i]
    return value

running_total = 0
list_position = 1
for word in name_list:
    word_pos_value = word_value(word) * list_position
    running_total += word_pos_value
    list_position += 1

print(running_total)