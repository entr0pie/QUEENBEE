""" BEECROWN: https://github.com/entr0pie/QUEENBEE """
# Date: 2022-10-10
# Source: https://www.beecrowd.com.br/judge/en/problems/view/1087
# Author: entr0pie
# Contact: <https://github.com/entr0pie>
# Name: BEE 1087

while True:
    coord = input("").strip(" ").split()
    x0, y0, x, y = int(coord[0]), int(coord[1]), int(coord[2]), int(coord[3])

    if x0 + x + y0 + y == 0:
        break

    elif x0 == x and y0 == y:
        print("0")

    elif x0 == x or y0 == y or x - x0 == y - y0 or x0 - x == y - y0 or x0 - x == y0 - y or x - x0 == y0 - y:
        print("1")

    else:
        print("2")
