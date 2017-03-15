"""

Description:
Write function makeParts that will take an array as argument and the size of 
the chunk.

Example: if an array of size 123 is given and chunk size is 10 there will be 
13 parts, 12 of size 10 and 1 of size 3.

"""
import unittest

def makeParts(arr, chunkSize):

    return []


class TestOrder(unittest.TestCase):
    def test_base_case01(self):
        self.assertEqual(makeParts([1,2,3,4,5], 2), [[1,2],[3,4],[5]])

    def test_base_case02(self):
        self.assertEqual(makeParts([1,2,3], 1), [[1],[2],[3]])

    def test_base_case03(self):
        self.assertEqual(makeParts([1,2,3,4,5], 10), [[1,2,3,4,5]])

if __name__ == "__main__":
    
    unittest.main()
