"""
937. Reorder Data in Log Files

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.
Then, either:

Each word after the identifier will consist only of lowercase letters,
or;
Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is
guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier, with the
identifier used in case of ties.  The digit-logs should be put in their
original order.

Return the final order of the logs.


Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""

import unittest

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log.split(" ")[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        # print(letter_logs)
        # print(digit_logs)

        output = sorted(letter_logs, key=lambda x: "".join(x.split(" ")[1:])+ x.split(" ")[0])
        output.extend(digit_logs)
        return output

class Tests(unittest.TestCase):
    sol = Solution()

    def test_example_1(self):
        input = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        expected_output = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

        self.assertEqual(self.sol.reorderLogFiles(input), expected_output)


    def test_same_first_word(self):
        input = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
        expected_output = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

        self.assertEqual(self.sol.reorderLogFiles(input), expected_output)


    def test_spaces(self):
        input = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]
        expected_output = ["5 m w","j mo","t q h","g 07","o 2 0"]

        self.assertEqual(self.sol.reorderLogFiles(input), expected_output)

if __name__ == "__main__":
    unittest.main()
