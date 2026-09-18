#Busca linear para descobrir quantas vezes foi realizado a contagem de elementos
def contar_elementos(lista, alvo):
    contador = 0
    for elemento in lista:
        if elemento == alvo:
            contador += 1
    return contador

numeros = [1, 2, 3, 2, 4, 2, 5, 2]
alvo = 2
print(contar_elementos(numeros, alvo))