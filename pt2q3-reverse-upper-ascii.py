# Takes a linear list of characters and returns a new list with the ASCII codes of every 
# uppercase character in the reverse of their order in the original list
def reverse_upper_ascii(x):
	# Initialize the return value to an empty list
	retval = []
	
	# Reverse the passed list
	# x.reverse()
	
	# For each element in the passed list ...
	for i in range(len(x) - 1, -1, -1):
		# If the element is an uppercase character, append the element to retval
		if x[i].isupper():
			retval.append(ord(x[i]))
	
	# Since the method iterated through all of x, return retval
	return retval

# Test
print(reverse_upper_ascii(['H', 'e', 'l', 'L', 'o', 'W', 'o', 'r', 'l', 'D']))