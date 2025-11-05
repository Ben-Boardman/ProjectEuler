'''
https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

# list of the digits
digits = ["0","1","2","3","4","5","6","7","8","9"]

# permutation number index
global perm_pos
perm_pos = 0

# recurrsive search to find the permutation
def perm_search(num_comb: str, digits: list) -> str:

    # base exit case
    if len(num_comb) == 10:
        global perm_pos
        perm_pos += 1
        return num_comb

    # recurrsive case lesser
    min_str = num_comb + digits[0]
    return perm_search(min_str, digits[1:])

    # recurssice case greater
    mid_str = num_comb + digits[1]


