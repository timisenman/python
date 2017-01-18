def reverse(s):
    new = list(s)
    rev = []
    for i in range(len(new)):
        rev.append(new.pop())
    return ''.join(rev)

print reverse("hello")
print reverse('reverse')