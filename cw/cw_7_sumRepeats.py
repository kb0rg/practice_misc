"""
Write a function that takes a list comprised of other lists of integers 
and returns the sum of all numbers that appear in two or more lists in the input
list. Now that might have sounded confusing, it isn't:

"""
import unittest

def repeat_sum(list_of_lists):
	
	if len(list_of_lists)<2:
		return 0

	list_sets = [set(l) for l in list_of_lists]
	repeats = set()
	for i in range(len(list_sets)-1):
		list_sets[i].intersection(list_sets[i+1])

	return sum(repeats)

class TestPrintRepeatSum(unittest.TestCase):
    def test_base_case(self):
        input_list = [[1, 2, 3],[2, 8, 9],[7, 123, 8]]
		# sum of [2, 8]
        self.assertEqual(repeat_sum(input_list), 10)
    def test_no_repeat(self):
        input_list = [[1], [2], [3, 4, 4, 4], [123456789]]
        # sum of []
        self.assertEqual(repeat_sum(input_list), 0)
    def test_multi_repeat(self):
        input_list = [[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]
        # sum of [1,8]
        self.assertEqual(repeat_sum(input_list), 9)
    def test_single_list(self):
        input_list = [[1]]
        # sum of []
        self.assertEqual(repeat_sum(input_list), 0)

if __name__ == "__main__":

    unittest.main()