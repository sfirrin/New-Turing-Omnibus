# Defining other binary logic operations in terms of NAND

def NAND(x, y):
    return not (x and y)

def AND(x, y):
    return NAND(NAND(x, y), NAND(x, y))

def NOT(x):
    return NAND(x, x)

def OR(x, y):
    return NOT(AND(NOT(x), NOT(y)))

def XOR(x, y):
    return AND(OR(x, y), OR(NOT(x), NOT(y)))

def XNOR(x, y):
    return NOT(XOR(x, y))

def IMPLY(x, y):
    return OR(NOT(x), y)

def NOR(x, y):
    return NOT(OR(x, y))