def length(str):
# Split by space and converting
	# String to list and
	lis = list(str.split(" "))
	return len(lis[-1])


# Driver code
str = "45&29 8*6^4"
print("The length of last word is",
	length(str))

# This code is contributed by vikkycirus
