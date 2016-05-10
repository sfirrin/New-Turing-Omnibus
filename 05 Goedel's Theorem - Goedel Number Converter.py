import string
import math

GOEDEL_CODES = {'0':1, 's':2, '+':3, '*':4, '=':5, '(':6, ')':7, ',':8,
               'x': 9, '1':10, '¬':11, '&':12, '∃':13, '∀':14, '→': 15}

class prime_generator:
    def __init__(self):
        self.next = 2
    def get_next(self):
        # I'm certain this could be far more efficient but I wanted to
        # come up with it on my own
        output = self.next
        if self.next == 2:
            self.next = 3
        else:
            i = self.next + 2
            while True:
                prime = True
                for j in range(3, int(math.sqrt(i)+1), 2):
                    if (i%j == 0):
                        prime = False
                        break
                if prime:
                    break
                i += 2
            self.next = i
        return output

def is_int(char):
    try:
        int(char)
        return True
    except ValueError:
        return False

def get_number_starting_at(index, formula):
    # Assumes the element at the index passed to it is an integer
    # Returns the number starting at index as a string
    output = formula[index]
    j = index + 1
    while j < len(formula) and is_int(formula[j]):
        output += formula[j]
    return int(output)

def get_goedel(formula):
    # Returns the Goedel number of a string formula
    formula = str(formula)
    stripped_f = ''
    for char in formula:
        if char not in string.whitespace:
            stripped_f += char
    prime_gen = prime_generator()
    goedel_num = 1
    for i in range(len(stripped_f)):
        if is_int(stripped_f[i]):
            constant = get_number_starting_at(i, stripped_f)
            if constant == 0:
                goedel_num *= prime_gen.get_next() ** GOEDEL_CODES['0']
                continue
            goedel_num *= prime_gen.get_next() ** GOEDEL_CODES['1']
            for i in range(constant-1):
                goedel_num *= prime_gen.get_next() ** GOEDEL_CODES['+']
                goedel_num *= prime_gen.get_next() ** GOEDEL_CODES['1']
        else:
            goedel_num *= prime_gen.get_next() ** GOEDEL_CODES.get(stripped_f[i], 0)
    return goedel_num
