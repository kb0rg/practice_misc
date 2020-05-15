"""
299. Bulls and Cows
https://leetcode.com/problems/bulls-and-cows/

You are playing the following Bulls and Cows game with your friend: You write
down a number and ask your friend to guess what the number is. Each time your
friend makes a guess, you provide a hint that indicates how many digits in said
guess match your secret number exactly in both digit and position (called
"bulls") and how many digits match the secret number but locate in the wrong
position (called "cows"). Your friend will use successive guesses and hints to
eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's
guess, use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate
digits.

Note: You may assume that the secret number and your friend's guess only
contain digits, and their lengths are always equal.
"""
import unittest

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        indexes_to_remove = set()
        secret_char = {}

        for i, char in enumerate(secret):
            secret_char[char] = secret_char.get(char, set())
            secret_char[char].add(i)

        for loc, char in enumerate(guess):
            if char in secret_char:
                if loc in secret_char[char]:
                    bulls += 1
                    secret_char[char].remove(loc)
                    indexes_to_remove.add(loc)

        for loc, char in enumerate(guess):
            if loc not in indexes_to_remove and char in secret_char:
                    if len(secret_char[char]) > 0:
                        cows += 1
                        secret_char[char].pop()

        return "{}A{}B".format(bulls, cows)

class Tests(unittest.TestCase):

    sol = Solution()

    def test_example_1(self):
        # Explanation:
        # 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
        secret = "1807"
        guess = "7810"
        self.assertEqual(self.sol.getHint(secret, guess), "1A3B")

    def test_example_2(self):
        # Explanation:
        # The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
        secret = "1123"
        guess = "0111"
        self.assertEqual(self.sol.getHint(secret, guess), "1A1B")

    def test_example_3(self):
        # Explanation:
        secret = "011"
        guess = "110"
        self.assertEqual(self.sol.getHint(secret, guess), "1A2B")

    def test_example_4(self):
        # Explanation:
        secret = "1122"
        guess = "2211"
        self.assertEqual(self.sol.getHint(secret, guess), "0A4B")

    def test_one_and_zero(self):
        secret = "11"
        guess = "10"
        self.assertEqual(self.sol.getHint(secret, guess), "1A0B")


if __name__ == '__main__':
    unittest.main()