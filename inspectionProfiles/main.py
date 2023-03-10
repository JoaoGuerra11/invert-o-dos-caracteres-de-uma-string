# Definindo a string a ser invertida
string = "Hello, world!"

# Convertendo a string em uma lista de caracteres
lista_caracteres = list(string)

# Invertendo a ordem dos caracteres na lista
lista_invertida = []
for i in range(len(lista_caracteres)):
    lista_invertida.append(lista_caracteres[len(lista_caracteres)-1-i])

# Convertendo a lista invertida de caracteres de volta para uma string
string_invertida = "".join(lista_invertida)

# Imprimindo a string invertida
print(string_invertida)

