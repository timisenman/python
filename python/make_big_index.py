

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword: #where all entries look like [keyword, [url]], entry[0] = keyword
            entry[1].append(url)
            return
    index.append([keyword,[url]]) #the argument in append one new value of "i"


def lookup(index,keyword):
  for entry in index:
    if entry[0] == keyword:
      return entry[1]
  return None

def make_string(p):
  s=''
  for e in p:
    s=s+e
  return s

def make_big_index(size):
    index = []
    letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index, word, 'fake')
        for i in range(len(letters) - 1, 0, -1): 
            if letters[i] < 'z':
                  letters[i] = chr(ord(letters[i]) + 1)
                  break
            else:
                   letters[i] = 'a'
    return index

def hash_string(keyword, buckets):
  h = 0
    for i in keyword:
        h = (h + ord(i)) % buckets
    return h 

#print make_big_index(10)

def make_hash(nbuckets):
  i = 0
  table = []
  while i < nbuckets:
    table.append([])
    i=+1
  return table

print make_hash(3)

















