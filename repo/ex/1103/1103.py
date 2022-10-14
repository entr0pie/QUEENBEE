""" BEECROWN: https://github.com/entr0pie/QUEENBEE """
# Date: 2022-10-13
# Source: https://www.beecrowd.com.br/judge/pt/problems/view/1103
# Author: entr0pie
# Contact: <https://github.com/entr0pie>
# Name: BEE 1103


while True:
    data = input("").strip()
    
    if data == "0 0 0 0":
        break

    data = data.split(" ")
    
    for n in range(4):
        data[n] = int(data[n])

    tempoInicial = data[0] * 60 + data[1]
    tempoFinal = data[2] * 60 + data[3]

    if tempoFinal < tempoInicial:
        tempoFinal += 1440 # ADICIONA A DIFERENÇA DE UM DIA

    print(tempoFinal - tempoInicial)