#Busca binaria existe ou não?
def busca_binaria_existe(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return True
        elif alvo < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return False

lista = [10, 20, 30, 40, 50]
alvo = 40

print(busca_binaria_existe(lista, alvo))
