def busca_binaria(lista,alvo):
    esquerda = 0
    direita = len(lista) -1
    passos = 0

    while esquerda <= direita:
        meio = (esquerda + direita) //2
        passos += 1
        if lista[meio] == alvo:
            return passos
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return passos

numeros = [1,2,3,4,5,6,7,8,9]
resultado = (busca_binaria(numeros,6))

print(resultado)