def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap


print(is_leap(1990))
print(is_leap(2000))
print(is_leap(2400))
