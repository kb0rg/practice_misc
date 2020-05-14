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
        guessed = set()
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                if not guess[i] in guessed:
                    if guess[i] in secret:
                        cows += 1
                        guessed.add(guess[i])
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

if __name__ == '__main__':
    unittest.main()