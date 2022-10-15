""" QUEENBEE: github.com/entr0pie/QUEENBEE """
# Date: 2022-10-15
# Source: https://www.beecrowd.com.br/judge/pt/problems/view/2234
# Author: entr0pie
# Contact: <github.com/entr0pie>
# Name: BEE 2234

factors = input("").strip().split(" ")

H, P = int(factors[0]), int(factors[1])

average = H / P 

print("{:.2f}".format(average))