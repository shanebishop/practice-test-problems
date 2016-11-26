# Global test dictionary
dictionary = {('...'): 's', ('---'): 'o'}

# Returns the translation of a string of Morse code into a string consisting of 
# Latin characters
def to_morse_code(x):
	# Intialize the return value to an empty string
	retval = ""
	
	# Strip the curly brackets from either end of x
	x = x.strip("{}")
	
	# Store a list of characters in Morse code
	chars = x.split()
	
	# Concatenate each element of chars to the return value
	for i in range(len(chars)):
		retval += dictionary[chars[i]]
	
	# Since this method iterated through every element in chars, return retval
	return retval

# Test
print(to_morse_code("{... --- ...}"))