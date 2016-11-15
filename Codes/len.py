
"""print("Lista ")
lista = [1,2,3,44,56,78,44,2,122,4]
print(lista)
print("")
print("Numero de elementos na Lista ")
print(len(lista))
print("")
print("redefinindo elemetos")
lista = []
print(len(lista))
print("Somando elementos")
lista = lista + [1,2,3,4,6]
print(lista)
lista = lista + [1,2,3,4,6,55555555]
print(lista)
"""
import random
lista =[]
num = int(input("Digite um número da sequência: "))
while num != -1:
    lista.append(num)
    num = int(input("Digite um número da sequência: "))


elemento = int(input("Digite o elemento a ser procurado: "))

cont = 0
for i in range(len(lista)):
    if lista[i] == elemento:
        cont += 1
print("O elemeto {} aparece {} vezes na sequencia.".format(elemento, cont))

# mesmo resultado usando o count
print("O elemeto {} aparece {} vezes na sequencia.".format(elemento, lista.count(elemento)))


# procurando diretamente o elemento
print("# procurando diretamente o elemento")
lista2 = [2,3,4,5,6]
a = lista2.count(2)
print(a)

print("Jogo de dados")
vetor = []
n = int(input("Digite o número de lançamentos: "))
for x in range(n):
    vetor.append(random.randint(1, 6))

for x in range(1, 7):
    """print("A face %i apareceu %i vezes."%(x, vetor.count(x)))
    print("A face {} apareceu {} vezes.".format(x, vetor.count(x)))
    print("Porcetagem")
    """
    print("A face {} apareceu {}% vezes.".format(x, 100*vetor.count(x)/n))
