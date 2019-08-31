import itertools
import math

'''
Count greatest depth of a nested list
Count elements in a nested list
Print all elements in list by visiting each
Copy all strings in list into new list
Create new, identical list but with all strings removed
Test x for primality
Generate primes up to n using list comprehension
Generate list of lists [a,b,c] such that a+b+c is odd and a*b*c is even
Turn nested list into a single level list
Count the longest length of any consecutive run of same
elements, no nesting
Return max element in arbirarily nested list
Sort an arbitrarily nested list into a flat list
Reverse list (without L.reverse())
'''

############################################


def levels(L):
    '''
    Count greatest depth of a nested list
    '''
    depth, maxdepth = 1, 1
    for x in L:
        if not isinstance(x, int):
            depth += levels(x)
            if depth > maxdepth:
                maxdepth = depth
                depth = 1
    return maxdepth

############################################


def count(L):
    '''
    Count elements in a nested list
    '''
    sum = 0
    for x in L:
        if isinstance(x, list):
            sum += count(x)
        else:
            sum += 1
    return sum

############################################


def traversal(L):
    '''
    Print all elements in list by visiting each
    '''
    for i, x in enumerate(L):
        if isinstance(x, list):
            traversal(x)
        else:
            print(x)

############################################


def extractstr(L):
    '''
    Copy all strings in list into new list
    '''
    strings = []
    for i, x in enumerate(L):
        if isinstance(x, list):
            strings.extend(extractstr(x))
        if isinstance(x, str):
            strings.append(x)
    return strings

############################################


def removestr(L):
    '''
    Create new, identical list but with all strings removed
    '''
    T = []
    for i, x in enumerate(L):
        if isinstance(x, int):
            T.append(x)
        elif isinstance(x, list):
            T.append(removestr(x))
    return T

############################################


def isprime(x):
    '''
    Test x for primality
    '''
    for i in range(2, (x / 2) + 1):
        if x % i == 0:
            return False
    return True

############################################


def primelist(n):
    '''
    Generate primes up to n using list comprehension
    '''
    return [i for i in range(2, n + 1) if isprime(i)]

############################################


def triples(n):
    '''
    Generate list of lists [a,b,c] such that a+b+c is odd and
    a*b*c is even
    '''
    return [[a, b, c] for a in range(n)
            for b in range(n)
            for c in range(n)
                if a + b + c % 2 == 1 and
            a * b * c % 2 == 0]

############################################


def flatten(L):
    '''
    Turn nested list into a single level list
    '''
    T = []
    for x in L:
        if isinstance(x, list):
            T = T + flatten(x)
        else:
            T = T + [x]
    return T

############################################


def plataeu(L):
    '''
    Count the longest length of any consecutive run of same
    elements, no nesting
    '''
    start, count, maxcount = 0, 1, 0
    for i, x in enumerate(L):
        if x == L[start]:
            count += 1
            if count > maxcount:
                maxcount = count
        else:
            start = i
            count = 1
    return maxcount

############################################


def maxelement(L):
    '''
    Return max element in arbirarily nested list
    '''
    i, maxnum = 0, 0
    while not isinstance(L[i], int):
        i += 1
        maxnum = L[i]
    for x in L:
        if isinstance(x, int):
            if x > maxnum:
                maxnum = x
        elif isinstance(x, list):
            temp = maxelement(x)
            if temp > maxnum:
                maxnum = temp
    return maxnum

############################################


def sortlist(L):
    '''
    Sort an arbitrarily nested list into a flat list
    '''
    T = sorted(flatten(L))
    return T

############################################


def rev(L):
    '''
    Reverse list (without L.reverse())
    '''
    T = []
    for i in range(len(L), 0, -1):
        T.append(i)

    return T


############################################


def perms(L):
    '''
    Produce all permutations of a list
    '''
    return list(itertools.permutations(L))

############################################


def combs(L):
    '''
    Produce combinations of a list
    '''
    for l in range(0, len(L) + 1):
        for subset in itertools.combinations(L, l):
            print(subset)

############################################


Z = [1, 2, 's', ['c', 5, 'q', 5, 'z'], 'fff']
A = [1, 'a', [3, 'z', [4, 5, [99]]], 'c']
F = [1, 2, [3, [4]], 5, [6, [7, [8, [9], 9, 9, 9, 9, 9]]]]
X = [1, 2, 3, [4, 5, 'd']]
Y = [1, 2, 3]
P = [1, 1, 3, 3, 3, 3, 4, 5, 5, 7, 7, 7, 7, 7]
Q = [[7, 5, 34, 3], 10, 11, 12]

print(combs(Y))
