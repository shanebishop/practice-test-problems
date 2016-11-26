from random import randint

# Returns a two dimensional list of integers with y rows and z cols
# Assumes every element is one greater than the previous element, or else each element 
# is one less than the following element
def two_dimensional_list_of_ints(x, y, z):
	# Intialize the return value to an empty list
	retval = []
	
	# Remove the space at the end of x
	x = x.strip()
	
	# Convert the string into a list, borrowing the initial variable name
	x = x.split(",")
	
	# Convert the list of strings to a list of ints
	for i in range(len(x)):
		x[i] = int(x[i])
	
	# This was not necessary - I could have continued to use the variable x
	list_of_ints = x[:]
	
	# Make y rows
	for row in range(y):
		# Initlaize an empty list to store the row's elements
		new_row = []
		
		# Make z cols
		for col in range(z):
			# Initialzie an int to store a new pseudorandom int
			random_int = -1
			
			# We only want to keep ints that are even numbers
			while random_int % 2 != 0:
				# Generate a random number between the smallest and largest elements
				# in the list
				random_int = randint(list_of_ints[0], list_of_ints[len(list_of_ints)-1])
			
			# Appends this new even int to new_row
			new_row.append(random_int)
		
		# Appends this new row to the return value
		retval.append(new_row)
	
	# Return retval
	return retval

# Retrieve input from the user
x = input("String (x): ")       # List
y = int(input("Integer (y): ")) # Rows
z = int(input("Integer (z): ")) # Elements per row (cols)

# Print out output
print(two_dimensional_list_of_ints(x, y, z))