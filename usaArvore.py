from Arvore import Arvore

raiz = None
arvore = Arvore()
valores = [50, 30, 70, 20, 40, 60, 80]

for valor in valores:
    arvore.inserir(valor)

valor_a_procurar = 40
if arvore.verificarValor(valor_a_procurar):
    print(f"O valor {valor_a_procurar} está na árvore.")
else:
    print(f"O valor {valor_a_procurar} não está na árvore.")

print("\n")

print("Resultado:")
print("\n")
arvore.imprimirArvore()
print("\n")
arvore.imprimirPreOrdem()
print("\n")
arvore.imprimirPosOrdem()

print("\n")

arvore.maiorValor()

print("\n")

arvore.menorValor()

print("\n")

arvore.calcularMedia()

print("\n")

soma = arvore.calcularSoma()
print("Soma dos nós: " + str(soma))

print("\n")

numeroNos = arvore.contarNos()
print("Número de nós: " + str(numeroNos))

print("\n")

numeroFolhas = arvore.contarFolhas()
print("Número de folhas: " + str(numeroFolhas))

print("\n")

altura = arvore.calcularAltura()
print("Altura: " + str(altura))