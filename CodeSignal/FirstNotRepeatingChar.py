# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it.
# If there is no such character, return '_'.

# Example

# For s = "abacabad", the output should be
# first_not_repeating_character(s) = 'c'.

# There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

# For s = "abacabaabacaba", the output should be
# first_not_repeating_character(s) = '_'.

# There are no characters in this string that do not repeat.

# [execution time limit] 4 seconds (py3)

# [input] string s

# A string that contains only lowercase English letters.

# [output] char

# The first non-repeating character in s of '_' if there are no characters that do not repeat.

import queue


def first_not_repeating_character(s):
    # first we have an array to store the order of our characters as they appear
    # and a table for the frequency of which they appear
    order = []
    frequency = {}

    # add the char in the string to the table if we have not seen it, as well as order. Otherwise increment its frequency
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            order.append(char)
    # now we check if the characters in order only appear once in frequency
    for char in order:
        if frequency[char] == 1:
            return char
    return "_"
