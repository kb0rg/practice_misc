import unittest

"""
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""

trans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return trans[s]
        prev = s[-1]
        num = trans[prev]
        for c in s[-2::-1]:
            if trans[c] >= trans[prev]:
                num += trans[c]
            else:
                num -= trans[c]
            prev = c
        return num


class Tests(unittest.TestCase):

    sol = Solution()

    def test_min(self):
        self.assertEqual(self.sol.romanToInt('I'), 1)

    def test_eleven(self):
        self.assertEqual(self.sol.romanToInt('XI'), 11)

    def test_thirty(self):
        self.assertEqual(self.sol.romanToInt('XXX'), 30)

    def test_forty_nine(self):
        self.assertEqual(self.sol.romanToInt('XLIX'), 49)

    def test_max(self):
        self.assertEqual(self.sol.romanToInt('MMMCMXCIX'), 3999)

if __name__ == '__main__':
    unittest.main()