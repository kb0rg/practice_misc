# -*- coding: utf-8 -*-
import random

"""
python function as monkey with a typewriter:

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
"""

def generate_string():

	possible_char_string = "abcdefghijklmnopqrstuvwxyz "
	rand_27char_string = ""

	while len(rand_27char_string) < 28:
		rand_27char_string = rand_27char_string + random.choice(possible_char_string)

	return rand_27char_string

def score_string(rand_str):

	"""
	instructions don't say how to score...?
	I initially thought it should return boolean, but third function clearly
	wants me to keep track of measurable scores....

	1 point for every char correct?
	"""

	goal_string = "methinks it is like a weasel"

	if rand_str == goal_string:
		return True

def monkey():

	"""
	tries = 0
	match_goal = False
	score = 0
	best_string = ""

	def tries_x1000():
		while tries <1001 and not match_goal:
			curr_string = generate_string()
			curr_score = score_string(curr_string)
			tries += 1
			if curr_score == 27:
				print "It's a match!"
				return
			else:
				if curr_score > score:
					score = curr_score
					best_string = curr_string
			print "the best string in 1000 tries is: " + best_string

	"""
	pass