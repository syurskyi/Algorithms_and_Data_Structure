#!/usr/bin/env python

"""Problem 126: Cuboid layers"""


def main():

    def ncubes(x, y, z, l):
        return 2*(x*y+x*z+y*z) + 4*(x+y+z)*(l-1) + 4*(l-1)*(l-2)

    lim = 20000
    cn = [0]*(lim+1)

    for x in range(1, lim):
        if ncubes(x, 1, 1, 1) > lim:
            break
        for y in range(x, lim):
            if ncubes(x, y, 1, 1) > lim:
                break
            for z in range(y, lim):
                if ncubes(x, y, z, 1) > lim:
                    break
                for n in range(1, lim):
                    c = ncubes(x, y, z, n)
                    if c > lim:
                        break
                    cn[c] += 1

    for i, v in enumerate(cn):
        if v == 1000:
            return i


if __name__ == "__main__":
    print(main())
