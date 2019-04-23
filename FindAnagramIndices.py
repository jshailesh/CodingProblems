'''
Given a word 'w' and a string 's', find all the starting indices in 's' which
are the starting locations of the anagrams of 'w'.
'''

from collections import defaultdict

def delete_if_count_zero(word_char_map, char):
    if word_char_map[char] == 0:
        del word_char_map[char]

def anagram_indices(word, s):

    results = []

    # Get the initial character map of the word and the initial window
    # of the size of the word in the string
    char_map = defaultdict(int)
    for char in word:
        char_map[char] += 1

    # Check if the initial window in the string is an anagram
    for char in s[: len(word)]:
        char_map[char] -= 1
        delete_if_count_zero(char_map, char)

    # The character map will be empty, if the initial window is an anagram
    if not char_map:
        results.append(0)

    # Now traverse the rest of the string
    for i in range(len(word), len(s)):
        start_char, end_char = s[i - len(word)], s[i]

        char_map[start_char] += 1
        delete_if_count_zero(char_map, start_char)

        char_map[end_char] -= 1
        delete_if_count_zero(char_map, end_char)

        if not char_map:
            beginning_index = i - len(word) + 1
            results.append(beginning_index)

    return results
