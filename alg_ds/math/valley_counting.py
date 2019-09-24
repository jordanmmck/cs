def get_valley_count(n, s):
    elevation = 0
    valley_count = 0
    in_valley = False
    for c in s:
        if c == 'U':
            elevation += 1
            if elevation == 0:
                valley_count += 1
                in_valley = False
        else:
            elevation -= 1
            if elevation < 0:
                in_valley = True
    return valley_count


print(get_valley_count(8, 'UDDDUDUU'))
