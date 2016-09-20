import io

result = ''

with io.FileIO("./foobar.txt", "r") as file:
    text = file.readall()
    
    innerResult = []

    for index, item in enumerate(text): 
    	if item == '!':
    		item = '?'

    	innerResult.append(item)

    result = ''.join(innerResult)


with io.FileIO("./foobarResult.txt", "w") as file:
	file.write(result)
