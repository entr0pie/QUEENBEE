""" QUEENBEE: github.com/entr0pie/QUEENBEE """
# Date: 2022-10-15
# Source: https://www.beecrowd.com.br/judge/pt/problems/view/2242
# Author: entr0pie
# Contact: <github.com/entr0pie>
# Name: BEE 2242

risada = input("")
vogais = ""

for char in risada:
    if char in ("a", "e", "i", "o", "u"):
        vogais += char

vogaisInvertidas = vogais[::-1]

if vogais == vogaisInvertidas:
    print("S")

else:
    print("N")
