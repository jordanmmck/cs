# is one string a permutation of another


def is_perm(s1, s2):
    if len(s1) != len(s2):
        return False
    if set(s1) != set(s2):
        return False
    return True


s1 = 'abc'
s2 = 'def'
s3 = 'bac'

print(is_perm(s1, s2))
print(is_perm(s1, s3))
