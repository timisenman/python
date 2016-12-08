# Replace T with U

def dna(string):
    # return string.replace('T', 'U')
    new = []
    for i in string:
        if i == 'T':
            new.append('U')
        else:
            new.append(i)
    return ''.join(new)
        

print dna("GCAT")

