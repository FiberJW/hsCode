# Write a function that takes a string input and 
# tells the user how many vowels are in the string.

def vowels_in(string):
	"Returns the number of vowels in the provided string as an integer"

	vowels = list('aeiou')
	vowel_count = 0
	for char in string:
		if char in vowels:
			vowel_count += 1

	return vowel_count

