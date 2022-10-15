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
