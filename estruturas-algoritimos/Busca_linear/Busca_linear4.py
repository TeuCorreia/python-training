#Busca linear que retorna a ultima vez que o alvo foi encontrado
def busca_linear_ultima_posicao(lista, alvo):
    ultima_posicao = -1
    for i in range(len(lista)):
        if lista[i] == alvo:
            ultima_posicao = i
    return ultima_posicao

lista = [10, 20, 30, 20, 40]
alvo = 20
print(busca_linear_ultima_posicao(lista, alvo))