nums = [118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106]
vowels = {
	ord("a"): 'a'
	ord("e"): 'e'
	ord("i"): 'i'
	ord("o"): 'o'
	ord("u"): 'u'
	ord("y"): 'y'
	}

i = 0

for x in inp:
	if x in vowels:
		inp[i] = vowels[x]
	i += 1
return inp
