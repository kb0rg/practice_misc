"""
953. Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly they also use english lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of
lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted
lexicographicaly in this alien language.

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
from typing import List
import unittest


class Solution:
    def compare_words(self, word_a, word_b, order_indexes):
        for i in range(len(word_a)):
            if i < len(word_b):
                char_a = word_a[i]
                char_b = word_b[i]
                if order_indexes[char_a] < order_indexes[char_b]:
                    return True
                if order_indexes[char_a] > order_indexes[char_b]:
                    return False
        if len(word_a) < len(word_b):
            return True
        return False

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True

        order_indexes = {}
        for i, char in enumerate(order):
            order_indexes[char] = i
        for i, word in enumerate(words):
            # check against next word
            if i < len(words) -1:
                next_word = words[i+1]
                if not self.compare_words(word, next_word, order_indexes):
                    return False
        return True


class TestSelfDividingNumber(unittest.TestCase):

    sol = Solution()

    def test_example_1(self):
        """
        Explanation: As 'h' comes before 'l' in this language, then the
        sequence is sorted.
        """
        self.assertEqual(
            self.sol.isAlienSorted(
                ["hello","leetcode"],
                "hlabcdefgijkmnopqrstuvwxyz"),
            True)


    def test_example_2(self):
        """
        Explanation: As 'd' comes after 'l' in this language, then
        words[0] > words[1], hence the sequence is unsorted.
        """
        self.assertEqual(
            self.sol.isAlienSorted(
                ["word","world","row"],
                "worldabcefghijkmnpqstuvxyz"),
            False)


    def test_example_3(self):
        """
        Explanation: The first three characters "app" match, and the second
        string is shorter (in size.) According to lexicographical rules
        "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank
        character which is less than any other character (More info).
        """
        self.assertEqual(
            self.sol.isAlienSorted(
                ["apple","app"],
                "abcdefghijklmnopqrstuvwxyz"),
            False)

if __name__ == '__main__':

    unittest.main()
