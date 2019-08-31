import calendar
import time

for i in range(int(input())):
    tinput1 = input().split()
    tinput2 = input().split()
    timezone1 = tinput1[-1]
    timezone2 = tinput2[-1]
    tinput1 = ' '.join(tinput1[:-1])
    tinput2 = ' '.join(tinput2[:-1])

    if int(timezone1) < 0:
        h1, m1 = divmod(-int(timezone1), 100)
        h1 = h1 * -1
        m1 = m1 * -1
    else:
        h1, m1 = divmod(int(timezone1), 100)

    if int(timezone2) < 0:
        h2, m2 = divmod(-int(timezone2), 100)
        h2 = h2 * -1
        m2 = m2 * -1
    else:
        h2, m2 = divmod(int(timezone2), 100)

    # Sun 10 May 2015 13:54:36 -0700
    t1 = time.strptime(tinput1, "%a %d %b %Y %H:%M:%S")
    t2 = time.strptime(tinput2, "%a %d %b %Y %H:%M:%S")
    timesec1 = calendar.timegm(t1)
    timesec2 = calendar.timegm(t2)

    timesec1 -= (h1 * 3600 + m1 * 60)
    timesec2 -= (h2 * 3600 + m2 * 60)
    print(abs(timesec1 - timesec2))
