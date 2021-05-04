#Leer informacion de un archivo caracter por caracter

archivo = open(input("Dame el nombre del archivo: "), 'r')

cont = 0
caracter = archivo.read(1)#Va leyendo de caracter en caracter

while caracter != "":
    cont += 1
    caracter = archivo.read(1)
    print(caracter)

archivo.close()

print(cont)#Imprime el numero de caracteres del archivo
