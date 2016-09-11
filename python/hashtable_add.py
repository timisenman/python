def hashtable_add(htable,key,value):
    # your code here
    hashtable_get_bucket(htable, key).append([key, value]) 
    
    
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]
    #table requested in its table form, and hash_string value: [#of tables]
    #the [#of tables] is defined by the keyword, and the length of the table (len(htable)). 

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out #creates number in which to place strings

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table #creates something like [[],[],[]]

table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]], 
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

