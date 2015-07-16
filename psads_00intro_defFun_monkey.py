# -*- coding: utf-8 -*-
import random

"""
python function as monkey with a typewriter:

How long do you think it would take for a Python function to generate just one 
sentence of Shakespeare? The sentence we’ll shoot for is:
"methinks it is like a weasel"

write a function that generates a string that is 27**** characters long by 
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

def generate_string():

	possible_char_string = "abcdefghijklmnopqrstuvwxyz "
	rand_28_char_string = ""

	while len(rand_28_char_string) < 29:
		rand_28_char_string = rand_28_char_string + random.choice(possible_char_string)

	return rand_28_char_string

def score_string(rand_str):

	"""
	1 point for every char correct -- in any position
	"""

	score = 28

	goal_string = "methinks it is like a weasel"

	if rand_str == goal_string:
		return score
	else:
		for i in range(0,(len(rand_str) - 1)):
			if rand_str[i] != goal_string[i]:
				score -= 1
		return score


def monkey():


	def tries_x1000():

		tries = 0
		match_goal = False
		score = 0
		best_string = ""


		while tries <1001:
		# while tries <1001 and match_goal==False:
			curr_string = generate_string()
			curr_score = score_string(curr_string)
			# print debug
			# print "current string: " + curr_string
			# print "current score: " + str(curr_score)

			if curr_score == 28:
				match_goal = True
				break
			else:
				if curr_score > score:
					score = curr_score
					best_string = curr_string	
				tries += 1
				# print debug
				# print "current try: " + str(tries)
			
		if match_goal == False:
			print "the best string in 1000 tries is: " + best_string + \
				"\n and its score is: " + str(curr_score)
			tries = 0
			tries_x1000()

		else:
			# print debug
			print "final string: " + curr_string
			print "It's a match!"
			return

	tries_x1000()

monkey()


