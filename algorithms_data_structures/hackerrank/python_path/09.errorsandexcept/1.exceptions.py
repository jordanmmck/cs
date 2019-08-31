# Code
# try:
#     print 1/0
# except ZeroDivisionError as e:
# print "Error Code:",e

T = int(input())
for i in range(T):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print(str('Error Code: ' + e.args[0]))
