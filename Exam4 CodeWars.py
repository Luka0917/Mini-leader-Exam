# 8 kyu

# Expressions Matter

def expression_matter(a, b, c):
    ex1 = a * (b + c)
    ex2 = a * b * c
    ex3 = a + b * c
    ex4 = (a + b) * c
    ex5 = a + b + c
    if (ex1 > ex2 and ex1 > ex3 and ex1 > ex4 and ex1 > ex5):
        return ex1
    elif ex2 > ex1 and ex2 > ex3 and ex2 > ex4 and ex2 > ex5:
        return ex2
    elif (ex3 > ex1 and ex3 > ex2 and ex3 > ex4 and ex3 > ex5):
        return ex3
    elif (ex4 > ex1 and ex4 > ex2 and ex4 > ex3 and ex4 > ex5):
        return ex4
    elif a == b:
        return ex2
    elif a == c:
        return ex1
    elif a == b and a == c:
        return ex5
    
# Passed: 115 Failed: 6