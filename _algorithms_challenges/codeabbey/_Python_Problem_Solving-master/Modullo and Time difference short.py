n = int(input())
for i in range(n):
    d1, h1, m1, s1, d2, h2, m2, s2 = input().split()
    d = (int(d2)-int(d1)) * 24 * 60 * 60
    h = (int(h2)-int(h1)) * 60 * 60
    m = (int(m2)-int(m1)) * 60
    s = int(s2)-int(s1)
    zman = d + h + m + s
   
    d = zman // (24*60*60)
    zman -= d*24*60*60
    h = zman // 3600
    zman -=  h*3600
    m = zman // 60
    s = zman - 60*m
    print('({} {} {} {})'.format(d, h, m, s), end = ' ')