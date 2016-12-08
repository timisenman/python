#return the length of the shortest word in a string

def find_short(string):
	#split string into list
	#return length of min(list)
	# res = string.split()
	# return len(min(res))

	return min([len(word) for word in string.split()])
	#3
	# return max([len(word) for word in string.split()])
	#7
	# return max([word for word in string.split()])
	#world
	# return [word for word in string.split()]
	# ['bitcoin', 'take', 'over', 'the', 'world', 'maybe', 'who', 'knows', 'perhaps']
	# return min([word for word in string.split()])
	#bitcoin


s = "bitcoin take over the world maybe who knows perhaps"
print find_short(s)