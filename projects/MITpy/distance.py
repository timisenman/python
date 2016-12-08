# # Distance

# # distance = root((x2-x1)**2+(y2-y1)**2)
# import math

# def distance(x1,y1, x2, y2):
#     dx = (x2 - x1)
#     dy = (y2 - y1)
#     dsquared = dx**2 + dy**2
#     print "dx is", dx
#     print "dy is", dy
#     result = math.sqrt(dsquared)
#     print result
#     return result

# distance(1,2,4,6)

# def my_area(xc,yc,xp,yp):
#     return area(distance(xc,yc,xp,yp))
#     # or 
#     # radius = distance(xc,yc,xp,yp)
#     # result = area(radius)
#     # return result

# print my_area(1,2,4,6)
import math

x = 1.0
while x < 10.0:
    print x, '\t', math.log(x)
    x = x + 1.0