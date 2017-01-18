### repeated substring patterns ###

def repeat(string):

#determine the length of the string
#divide by even or odds, depending on length
#determine if there's a pattern at all 
#recursion somewhere? 
#create a list of each of those divisions
#does each item in the list equal all other items? 
### does the first item equal each next item? 
#if yes, return True

    new = []
    if len(string) % 2 == 0:
        
    new.append(list(string))


print repeat("abab")
#>>> True
print repeat("abcabcabc")
#>>> True
print repeat("aba")
#>>> False
