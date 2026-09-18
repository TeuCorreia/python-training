#Busca linear tradicional
def busca_linear(lista, alvo):
    #cria a sequência de elementos e percorre a lista
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

# enumerado do 0 a 4
numeros = [5, 3, 8, 1, 9]
resultado = busca_linear(numeros, 8)

if resultado != -1:
    print(f"Elemento encontrado no índice: {resultado}")
else:
    print("Elemento não encontrado na lista")