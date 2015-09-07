"""
Write a function that will encrypt a given sentence into International Morse 
Code, both the input and out puts will be strings.

Characters should be separated by a single space. Words should be separated by 
a triple space.

For example, "HELLO WORLD" should return -> 
".... . .-.. .-.. --- .-- --- .-. .-.. -.."

To find out more about Morse Code follow this link: 
https://en.wikipedia.org/wiki/Morse_code

A preloaded object/dictionary/hash called CHAR_TO_MORSE will be provided to 
help convert characters to Morse Code.


>>> encryption("HELLO WORLD")
'.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
>>> encryption("SOS")
'... --- ...'
>>> encryption("1836")
'.---- ---.. ...-- -....'
>>> encryption("THE QUICK BROWN FOX")
'- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-'
>>> encryption("JUMPED OVER THE")
'.--- ..- -- .--. . -..   --- ...- . .-.   - .... .'
"""


CHAR_TO_MORSE = {'0': '-----', '2': '..---', '4': '....-', '6': '-....', 
					'8': '---..', 'B': '-...', 'D': '-..', 'F': '..-.', 
					'H': '....', 'J': '.---', 'L': '.-..', 'N': '-.', 
					'P': '.--.', 'R': '.-.', 'T': '-', 'V': '...-', 'X': '-..-', 
					'Z': '--..', 'b': '-...', 'd': '-..', 'f': '..-.', 
					'h': '....', 'j': '.---', 'l': '.-..', 'n': '-.', 
					'p': '.--.', 'r': '.-.', 't': '-', 'v': '...-', 'x': '-..-', 
					'z': '--..', '1': '.----', '3': '...--', '5': '.....', 
					'7': '--...', '9': '----.', 'A': '.-', 'C': '-.-.', 
					'E': '.', 'G': '--.', 'I': '..', 'K': '-.-', 'M': '--', 
					'O': '---', 'Q': '--.-', 'S': '...', 'U': '..-', 
					'W': '.--', 'Y': '-.--', 'a': '.-', 'c': '-.-.', 'e': '.', 
					'g': '--.', 'i': '..', 'k': '-.-', 'm': '--', 'o': '---', 
					'q': '--.-', 's': '...', 'u': '..-', 'w': '.--', 'y': '-.--'}

def encryption(string):

	morse_string = ""

	if len(string) < 1:
		return morse_string

	for char in string[:-1]:
		if char.isalpha() or char.isdigit():
			morse_string += CHAR_TO_MORSE[char] + " "
		else:
			morse_string += char + " "

	if string[-1].isalpha() or string[-1].isdigit():
		morse_string += CHAR_TO_MORSE[string[-1]]
	else:
		morse_string += string[-1]

	return morse_string

if __name__ == "__main__":

	import doctest
	doctest.testmod()
