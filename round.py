# Without using the Python round() function,
# create a function called roundNew() that takes
# a float input and rounds it to the nearest integer.

def roundNew(num):
	"Takes a float number as an argument and rounds it to the nearest integer."

	valid = isinstance(num, float)

	if valid != True:
		return None
	
	return int(num//1 + ((num%1)/0.5)//1)

