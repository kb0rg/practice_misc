"""
Write a function that takes a list comprised of other lists of integers 
and returns the sum of all numbers that appear in two or more lists in the input
list. Now that might have sounded confusing, it isn't:

"""
import unittest

def repeat_sum(list_of_lists):

	list_sets = [set(l) for l in list_of_lists]
	print 'list_sets', list_sets
	repeats = []
	for i in range(len(list_sets)-2):
		repeats.append(list_sets[i] & list_sets[i+1])
	print 'repeats', repeats
	# print 'set(repeats)', set(repeats)
	# return sum(int(i) for i in set(repeats))

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

if __name__ == "__main__":

    unittest.main()