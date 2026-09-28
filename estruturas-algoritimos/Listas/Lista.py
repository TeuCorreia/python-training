class Fila:
    def __init__(self):
        #Inicializar a fila vazia
        self.fila = []

    def enfileirar(self,item):
        #Adiciona no final -> Complexidade O(n)
        self.item.append(item)

    def desenfileirar(self):
        #Remove do inicio -> Complexidade O(n)
        if self.esta_vazia():
            print("Fila vazia!")
            return None

        #Pop(0) remove o elemento do índice 0 e desloca todos os outros
        return self.itens.pop(0)

    def esta_vazia(self):
        return len(self.ittens)
    
    def tamanho(self):
        return len(self.itens)

    