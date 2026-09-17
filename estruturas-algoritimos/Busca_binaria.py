def busca_binaria(lista,alvo):
    esquerda = 0
    direita = len(lista) -1

    while esquerda <= direita:
        meio = (esquerda + direita) //2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

numeros = [1,2,3,4,5,6,7,8,9]
resultado = (busca_binaria(numeros,1))

print(resultado)