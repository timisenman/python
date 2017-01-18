def fizzBuzz(n):
    fizzy = []
    for i in range(1,n+1):
        if i % 5 == 0 and i % 3 == 0:
            fizzy.append("FizzBuzz")
        elif i % 5 == 0:
            fizzy.append("Buzz")
        elif i % 3 == 0:
            fizzy.append("Fizz")
        else:
            fizzy.append(str(i)) 
    print fizzy

fizzBuzz(100)
