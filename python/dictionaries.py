#Dictionaries
#Sets of <key, value> pairs that are mutable
#organized in { } brackets

dick = {
	‘one’: 1
	‘two’: 2
}

d[‘one’] = z
dick = { ‘one’: z }

#True/False with Dics - You print a key value by doing:
print three in dick
#>>>False
print two in dick
#>>>True

#Reassigning with Dictionary
dick[‘three’] = 1
print dick[’three’]
#>>>1 

#Using a Dictionary list within a Dictionary
elements = {}
elements[‘H’] = {‘name’: ‘Hydrogen’, ‘number’: 1, ‘weight’: 1.00794}
elements[‘He’] = {‘name’: ‘Helium’, ‘number’: 2, ‘weight’: 4.002602, ’noble gas’: True} 
print elements['H']['name']
#>>>Hydrogen

