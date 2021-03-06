# -*- coding: utf-8 -*-
import random
"""
from Problem Solving with Algorithms and Data Structures, 
intro chapter, Defining Functions section.
"""

"""
problem: python function as monkey with a typewriter

How long do you think it would take for a Python function to generate just one 
sentence of Shakespeare? The sentence we’ll shoot for is:
"methinks it is like a weasel"

write a function that generates a string that is 27 characters long by 
choosing random letters from the 26 letters in the alphabet plus the space.

We’ll write another function that will score each generated string by comparing 
the randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the 
letters are correct we are done. If the letters are not correct then we will 
generate a whole new string.

To make it easier to follow your program’s progress this third function should 
print out the best string generated so far and its score every 1000 tries.

***kborg note: the goal string is actually 28 char long. revising function.
"""

def generate_string(str_len):

	"""
	generates a string that is str_len characters long by choosing random letters 
	from the 26 letters in the alphabet plus the space.
	"""

	possible_char_str = "abcdefghijklmnopqrstuvwxyz "
	rand_str = ""

	while len(rand_str) < (str_len + 1):
		rand_str = rand_str + random.choice(possible_char_str)

	return rand_str

def score_string(goal_str, test_str):

	"""
	score test string by comparing to the goal string.
	return percent of matching characters
	"""

	num_char_match = 0

	if test_str == goal_str:
		return 100
	else:
		for i in range(0,(len(goal_str) - 1)):
			if test_str[i] == goal_str[i]:
				num_char_match += 1

	# score is returned as percent, as float to two decimal places
	score = num_char_match / float(len(goal_str))
	return float("{0:.2f}".format(score * 100))


"""
implementing non-recursive solution as per video on book's site,
goalstring and goalstring length baked in,
and tries modified to 1 million.
not following book's score format.
"""
def main():

	goal_str = "methinks it is like a weasel"
	new_string = generate_string(28)
	best_score = 0
	new_score = score_string(goal_str, new_string)

	while new_score < 100:
		if new_score > best_score:
			print new_score, new_string
			best_score = new_score
		new_string = generate_string(28)
		new_score = score_string(goal_str, new_string)

main()

"""
recursive attempt below. exceeds max recursion depth.
would like to return to this and try to fix it.
"""

# def monkey(goal_str):


# 	def tries_x1000():

# 		tries = 0
# 		match_goal = False
# 		best_score = 0
# 		best_string = ""


# 		# while tries <1001:
# 		while tries <1001 and match_goal==False:
# 			curr_string = generate_string(len(goal_str))
# 			curr_score = score_string(goal_str, curr_string)
# 			# print debug
# 			# print "current string: " + curr_string
# 			# print "current score: " + str(curr_score)

# 			if curr_score == 100:
# 				match_goal = True
# 				# break
# 			else:
# 				if curr_score >= best_score:
# 					best_score = curr_score
# 					best_string = curr_string	
# 				tries += 1
# 				# print debug
# 				# print "current try: " + str(tries)
			
# 		if match_goal == False:
# 			print "the best string in 1000 tries is: " + best_string + "\n" + \
# 					"and its score is: " + str(curr_score) + "%"
# 			tries = 0
# 			tries_x1000()

# 		else:
# 			# print debug
# 			print "final string: " + curr_string
# 			print "It's a match!"
# 			return

# 	tries_x1000()

# monkey("methinks it is like a weasel")

