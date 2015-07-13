"""
 create the function nato that takes a word and returns a string spells the word 
 using the NATO phonetic alphabet.

There should be a space between each word in the returned string, and the first 
letter of each word should be capitalized.

"""
letters =  {
    "A": "Alpha",  "B": "Bravo",   "C": "Charlie",
    "D": "Delta",  "E": "Echo",    "F": "Foxtrot",
    "G": "Golf",   "H": "Hotel",   "I": "India",
    "J": "Juliett","K": "Kilo",    "L": "Lima",
    "M": "Mike",   "N": "November","O": "Oscar",
    "P": "Papa",   "Q": "Quebec",  "R": "Romeo",
    "S": "Sierra", "T": "Tango",   "U": "Uniform",
    "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu"
  }
  
def nato(word):
    
    natoized_word_list = []
    
    for char in word:
        char = char.upper()
        natoized_word_list.append(letters[char])
    
    return " ".join(natoized_word_list)