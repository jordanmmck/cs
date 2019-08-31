# >>> any([1>0,1==0,1<0])
# True
# >>> any([1<0,2<1,3<2])
# False

# >>> all(['a'<'b','b'<'c'])
# True
# >>> all(['a'<'b','c'<'b'])
# False

N = int(input())
l = list(map(int, input().split()))

if(any(i < 0 for i in l)):
    print('False')
else:
    print(any(str(i) == str(i)[::-1] for i in l))
