numero = int(input('Digite um número inteiro na base 10: '))
base = int(input('Digite a base selecionada (2, 8 ou 16): '))

convertido = []

if (base == 16):
    if numero % base == 10:
        convertido.append('A')
    if numero % base == 11:
        convertido.append('B')
    if numero % base == 12:
        convertido.append('C')
    if numero % base == 13:
        convertido.append('D')
    if numero % base == 14:
        convertido.append('E')
    if numero % base == 15:
        convertido.append('F')
else:
    convertido.append(numero % base)

while True:
    numero = int(numero / base)
    if (base == 16):
        if numero % base == 10:
            convertido.append('A')
        if numero % base == 11:
            convertido.append('B')
        if numero % base == 12:
            convertido.append('C')
        if numero % base == 13:
            convertido.append('D')
        if numero % base == 14:
            convertido.append('E')
        if numero % base == 15:
            convertido.append('F')
    else:
        convertido.append(numero % base)
    if (numero == 1 or numero == 0):
        break

indice = len(convertido) - 1
numero_convertido = []

while (indice >= 0):
    numero_convertido.append(str(convertido[indice]))
    indice = indice - 1

string_convertido = "".join(numero_convertido)
print(f'O número no sistema escolhido é : {string_convertido}')