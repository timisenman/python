#walk = [n,s,e,w, etc.]
def isValidWalk(walk):
	if len(walk) != 10:
		return False
	
	start = [0,0]
	end = [0,0]

	for i in walk:
		if i == "n":
			end[0] = end[0] + 1
		if i == "s":
			end[0] = end[0] - 1
		if i == "e":
			end[1] = end[1] + 1
		if i == "w":
			end[1] = end[1] - 1
	# return end

	# if start == end:
	# 	return True
	# else:
	# 	return False
	return start == end

print isValidWalk(['n', 'n', 'w', 'w', 'w', 'n', 'n', 'w', 'w', 'w'])
print isValidWalk(['n', 's', 'w', 'w', 'w', 'n', 's', 'w', 'w'])
print isValidWalk(['n', 'n', 'w', 'w', 'w', 'n', 'n', 'w', 'w', 'w'])
print isValidWalk(['n', 's', 'w', 'e', 'n', 's', 'w', 'e', 'n', 's'])
# >>>Should return True