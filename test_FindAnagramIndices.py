import pytest

from FindAnagramIndices import anagram_indices

def verify_results(word, s, expected):
    result = anagram_indices(word, s)
    assert result == expected
    
class TestAnagramIndices(object):

    def test_general_case(self):
        word = 'ab'
        s = 'abxaba'
        expected_indices = [0, 3, 4]
        verify_results(word, s, expected_indices)

    def test_no_anagram(self):
        word = 'ab'
        s = 'doesnotexist'
        expected_indices = []
        verify_results(word, s, expected_indices)

    def test_half_word(self):
        word = 'ab'
        s = 'accaac'
        expected_indices = []
        verify_results(word, s, expected_indices)

    def test_long_string(self):
        word = 'abra'
        s = 'abracadabra'
        expected_indices = [0, 7]
        verify_results(word, s, expected_indices)
