'''
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns
the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
    
Implement car and cdr.
'''

def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(pair):
    return pair(lambda a,b: a)

def cdr(pair):
    return pair(lambda a,b: b)

'''
Lambda functions can't act on a tuple or a list. Cons is a closure, we can
only return the two individual arguments fed to it as a pair by returning them as
the arguments of its function. Lambda can then act on this result.
'''
