def get_avg(a):
    x = 0
    y = 0
    for i in a:
        x += i[0]
        y += i[1]
    return y / x



a = [[2104,399900],[1600,329900],[2400,369000]]
print get_avg(a)

