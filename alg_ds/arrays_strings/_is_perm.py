# is one string a permutation of another

# if they differ in length, then not perms

def is_perm(s1, s2):
    if len(s1) != len(s2):
        return False


s1 = 'abc'
s2 = 'def'
s3 = 'bac'

print(is_perm(s1, s2))
print(is_perm(s1, s3))
