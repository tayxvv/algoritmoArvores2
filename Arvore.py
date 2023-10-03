class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self.inserirRecursivo(self.raiz, chave)

    def inserirRecursivo(self, raiz, chave):
        if raiz is None:
            return No(chave)

        if chave < raiz.chave:
            raiz.esquerda = self.inserirRecursivo(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self.inserirRecursivo(raiz.direita, chave)

        return raiz

    def imprimirArvore(self):
        self.imprimirArvoreRecursivo(self.raiz)

    def imprimirArvoreRecursivo(self, raiz):
        if raiz:
            self.imprimirArvoreRecursivo(raiz.esquerda)
            print(raiz.chave, end=' ')
            self.imprimirArvoreRecursivo(raiz.direita)

    def imprimirPreOrdem(self):
        self.imprimirPreOrdemRecursivo(self.raiz)

    def imprimirPreOrdemRecursivo(self, raiz):
        if raiz:
            print(raiz.chave, end=' ')
            self.imprimirPreOrdemRecursivo(raiz.esquerda)
            self.imprimirPreOrdemRecursivo(raiz.direita)

    def imprimirPosOrdem(self):
        self.imprimirPosOrdemRecursivo(self.raiz)

    def imprimirPosOrdemRecursivo(self, raiz):
        if raiz:
            self.imprimirPosOrdemRecursivo(raiz.esquerda)
            self.imprimirPosOrdemRecursivo(raiz.direita)
            print(raiz.chave, end=' ')

    def verificarValor(self, valor):
        return self.verificarValorRecursivo(self.raiz, valor)

    def verificarValorRecursivo(self, raiz, valor):
        if raiz is None:
            return False

        if valor == raiz.chave:
            return True
        elif valor < raiz.chave:
            return self.verificarValorRecursivo(raiz.esquerda, valor)
        else:
            return self.verificarValorRecursivo(raiz.direita, valor)
        
    def maiorValor(self):
        return self.maiorValorRecursivo(self.raiz)

    def maiorValorRecursivo(self, raiz):
        if raiz is None:
            return False
        
        atual = self.raiz

        while atual.direita is not None:
            atual = atual.direita

        print(f"Maior valor: {atual.chave}")
    
    def menorValor(self):
        return self.menorValorRecursivo(self.raiz)

    def menorValorRecursivo(self, raiz):
        if raiz is None:
            return False
        
        atual = self.raiz

        while atual.esquerda is not None:
            atual = atual.esquerda

        print(f"Menor valor: {atual.chave}")

    def calcularMedia(self):
        soma, contador = self.calcularMediaRecursivo(self.raiz)
        if contador == 0:
            return None
        print(f"Média {soma / contador}")

    def calcularMediaRecursivo(self, raiz):
        if raiz is None:
            return 0, 0

        soma_esquerda, contador_esquerda = self.calcularMediaRecursivo(raiz.esquerda)
        soma_direita, contador_direita = self.calcularMediaRecursivo(raiz.direita)

        soma_total = soma_esquerda + soma_direita + raiz.chave
        contador_total = contador_esquerda + contador_direita + 1

        return soma_total, contador_total
    
    def calcularSoma(self):
        return self.calcularSomaRecursivo(self.raiz)

    def calcularSomaRecursivo(self, raiz):
        if raiz is None:
            return 0

        soma_esquerda = self.calcularSomaRecursivo(raiz.esquerda)
        soma_direita = self.calcularSomaRecursivo(raiz.direita)

        return soma_esquerda + soma_direita + raiz.chave
        
    def contarNos(self):
        return self.contarNosRecursivamente(self.raiz)

    def contarNosRecursivamente(self, raiz):
        if raiz is None:
            return 0

        nos_esquerda = self.contarNosRecursivamente(raiz.esquerda)
        nos_direita = self.contarNosRecursivamente(raiz.direita)

        return nos_esquerda + nos_direita + 1
    
    def contarFolhas(self):
        return self.contarFolhasRecursivamente(self.raiz)

    def contarFolhasRecursivamente(self, raiz):
        if raiz is None:
            return 0

        if raiz.esquerda is None and raiz.direita is None:
            return 1

        folhas_esquerda = self.contarFolhasRecursivamente(raiz.esquerda)
        folhas_direita = self.contarFolhasRecursivamente(raiz.direita)

        return folhas_esquerda + folhas_direita
    
    def calcularAltura(self):
        return self.calcularAlturaRecursivamente(self.raiz)

    def calcularAlturaRecursivamente(self, raiz):
        if raiz is None:
            return 0

        altura_esquerda = self.calcularAlturaRecursivamente(raiz.esquerda)
        altura_direita = self.calcularAlturaRecursivamente(raiz.direita)

        return max(altura_esquerda, altura_direita) + 1