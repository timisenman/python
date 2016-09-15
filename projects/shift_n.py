# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    if letter == 'z':
        letter = '`'
    next = ord(letter)+n
    if next > 122:
        next = ((next - 122)+96)
    return chr(next)

#TO DO
#If going backwards from a ('a', -1), return 'z'

print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i