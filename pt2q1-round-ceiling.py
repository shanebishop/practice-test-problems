# Takes a floating point number and rounds it up to the nearest integer, and returns
# this result as an integer
def round_up(x):
	# If the number is already an integer, simply return the number
	if x == int(x):
		return int(x // 1)
	# Otherwise, truncate the number, then add one
	else:
		return int(x // 1 + 1)

# Tests
print(round_up(5))
print(round_up(6.0))
print(round_up(5.1))
print(round_up(5.01))
print(round_up(5.5))
print(round_up(5.50))
print(round_up(5.99))