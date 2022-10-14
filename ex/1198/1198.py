""" BEECROWN: github.com/entr0pie/QUEENBEE """
# Date: 2022-10-14
# Source: https://www.beecrowd.com.br/judge/pt/problems/view/1198
# Author: entr0pie
# Contact: <github.com/entr0pie>
# Name: BEE 1198


while True:
    try:
        soldados = input("")
    
    except EOFError:
        break

    soldados = soldados.split(" ")
    hashmat, oponente = int(soldados[0]), int(soldados[1])
    
    diference = int(((hashmat - oponente) ** 2) ** 0.5)
    print(diference)
