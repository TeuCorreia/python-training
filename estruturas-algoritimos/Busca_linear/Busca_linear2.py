#Busca linear para descobrir maior numero da lista
def encontrar_maior(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

numeros = [1, 6, 9, 10]
print(encontrar_maior(numeros))