# This is still in progress so there is a decent chance I'm doing this wrong
import string

GODEL_CODES = {'0':1, 's':2, '+':3, '*':4, '=':5, '(':6, ')':7, ',':8,
               'x': 9, '1':10, '¬':11, '&':12, '∃':13, '∀':14, '→': 15}

def get_primes(n):
    # I know this could be a lot more efficient but I wanted to come up
    # with it on my own
    primes = [2]
    i = 3
    while len(primes)<n:
        prime = True
        for j in range(3, i//2, 2):
            if (i%j == 0):
                prime = False
                break
        if prime:
            primes.append(i)
        i += 2
        print(i)
    return primes

def is_int(char):
    try:
        int(char)
        return True
    except ValueError:
        return False

def get_godel(formula):
    length = 0;
    stripped_f = ''
    for char in formula:
        if char not in string.whitespace:
            length += 1
            stripped_f += char
    primes = get_primes(length)
    godel_num = 1
    for i in range(len(stripped_f)):
        if is_int(stripped_f[i]):
