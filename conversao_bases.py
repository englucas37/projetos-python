numero = int(input('Digite um número inteiro na base 10: '))
base = int(input('Digite a base selecionada (2, 8 ou 16): '))

if base == 16:
    print(f'O número no sistema escolhido é : {hex(numero).lstrip("0x").rstrip("L").upper()}')

convertido = []

convertido.append(numero % base)

while True:
    numero = int(numero / base)
    convertido.append(numero % base)
    if (numero == 1 or numero == 0):
        break

indice = len(convertido) - 1
numero_convertido = []

while (indice >= 0):
    numero_convertido.append(str(convertido[indice]))
    indice = indice - 1

string_convertido = "".join(numero_convertido)

if base != 16:
    print(f'O número no sistema escolhido é : {string_convertido}')