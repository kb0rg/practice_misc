"""

Description:

Your task is to sort a given string. Each word in the String will contain a 
single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input 
String will only contain valid consecutive numbers.

Example:
For an input: "is2 Thi1s T4est 3a" the function should return:
"Thi1s is2 3a T4est"

"""

import unittest
import re

def order(sentence):
  sent_list = sentence.split()
  reorder = ['foo'] * (len(sent_list)+1)
  for word in sent_list:
      i = int(re.search(r'\d+', word).group())
      reorder[i] = word

  return ' '.join(reorder[1:])

class TestOrder(unittest.TestCase):
    def test_base_case(self):
        input_str = "is2 Thi1s T4est 3a"
        self.assertEqual(order(input_str), "Thi1s is2 3a T4est")

if __name__ == "__main__":

    unittest.main()
