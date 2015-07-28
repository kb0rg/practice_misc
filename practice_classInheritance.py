class Pet(object):

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def speak(self):
		return "Hi! My name is %s." % self.name

	def get_older(self):
		self.age += 1

class Dog(Pet):
	
	def speak(self):
		return "Woof!"

class Cat(Pet):

	def speak(self):
		return "Meow!"

class Puppy(Dog):

	def poop(self):
		return "%s just shat on the carpet again" % self.name

"""
when do we need to use "super"? calling puppyname.speak()
returns "Woof" as expected without needing to specify super...
"""