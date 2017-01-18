def course(lis):
    num_courses = len(lis)
    print "Original list:", str(lis) + ".", "Length:", num_courses
    #flatten course list
    courses = []
    for i in lis:
        for j in i:
            courses.append(j)
    print "Flattened list:", courses
    #order classes from smallest to largest
    #create a new list in a range of 0 through len(course)
    courses.sort()
    print "Sorted courses:", courses 
    #remove duplicates by comparing to newly created list 
    for i in courses:
        while courses.count(i) > 1:
            courses.remove(i)
    
    #return order in a single, new list
    print "Ordered courses:", courses
    
# test = [[2,3],[1,3],[6,1],[4,2],[4,4]]
# print course(test)

test2 = [[1,2],[1,2],[1,2],[3,4],[5,6]]
course(test2)
    #>>> 2, [[1,0]]
    #>>> 4, [[1,0],[2,0],[3,1],[3,2]]