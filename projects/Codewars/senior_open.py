#Senior or Open
#If Age =>55 and hc =< 7, Senior
#else Open

group = [16, 23],[73,1],[56, 20],[1, -1]

def openOrSenior(data):
	lis = []
	for i in data:
		if i[0] >= 55 and i[1] > 7:
			lis.append("Senior")
		else:
			lis.append("Open")
	return lis

print openOrSenior(group)