def minpathsum(triangle):
    s = 0
    for i in triangle:
        s = s + min(i)
    return s

print minpathsum([[1],[2,3],[4,5,6]])
print minpathsum([[2],[3,4],[6,5,7],[4,1,8,3]])