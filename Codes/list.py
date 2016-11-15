"""
# INDEX
print ("Em um index conento valores ['Zero', 'Um', 'Dois', 'Três']\n")
Exemplo_index = ['Zero', 'Um', 'Dois', 'Três']
print ("Mostrando primeiro item, na posição 0\n")
print (Exemplo_index[0])
print ("Mostrando o ultimo item do index\n")
print (Exemplo_index[-1])

#aDICIONANDO ITEM NO FIM DA LIST
print ("Adicionando mais um item no fim do index, usando a função .append\n")
Exemplo_index.append('Quatro')
print ("Mostrando o ultimo item do index após a adição\n")
print (Exemplo_index[-1])

#Criando um segundo list

Exemplo_dois_index = ['Cinco', 'Seis', 'Sete', 'Oito']
print ("Mostrando todo Index Exemplo_dois-Index\n")
print (Exemplo_dois_index)

#Extendendo a lista Exemplo_index com o Exemplo_dois_index
print ("Extendendo a lista Exemplo_index com o Exemplo_dois_index\n")
Exemplo_index.extend(Exemplo_dois_index)

print("mostrando a união das listas\n")
print(Exemplo_index)



print("Listas com diferentes tipos de dados\n")
lista = [1.6, 4, 8.0]
print(lista)

print("Uma lista dentro de outra lista\n")
lista_interna = [[1,2],3]
#reverse
print("")
print("Imprimindo na ordem inversa da ordem lida")
idades =  []
alturas = []
for i in range(1, 6):
    idade = int(input("Digite a idade da pessoa %i de 5: "%i))
    altura = float(input("Digite a altura(m) da pessoa %i de 5: "%i))

    idades.append(idade)
    alturas.append(altura)



print("")

print("Imprimindo na ordem inversa da ordem lida - usando slices")

idades_invertida = idades[::-1]
alturas_invertida = alturas[::-1]

for i in range(5):
    print("Idade %i: %i"%(5 - i, idades_invertida[i]))
    print("Altur %i: %.2f"%(5 - i, alturas_invertida[i]))



print("")
print("Imprimindo na ordem inversa da ordem lida - usando Range")

for i in range(4, -1, -1):
    print("Idade %i: %i"%(i+1, idades[i]))
    print("Altura %i: %.2f"%(i+1, alturas[1]))


#Usando reverse
print("")
print("Imprimindo na ordem inversa da ordem lida - usando Reverse")

idades.reverse()
alturas.reverse()
for i in range(5):
    print("Idade %i: %i"%(5 -1, idades[i]))
    print ("Altura: %i %.2f"%(5- i, alturas[i]))


print("")
print("Removendo itens na lista usando POP")
nova_lista = [1,2,3,4,5,6,7,8,9,10]
print(nova_lista)

indice = int(input("Digite o indice de 0 até %i do elemendo a ser removido: "))
print("Elemento:", nova_lista.pop(indice))
print(nova_lista)

print("")
print("")




print("")
print("Verificando o item pelo index da lista: ")
lista_index = [1,2,3,4,5,6,7,8,9,10]
print(lista_index)
verificar = int(input("Qual o item vc deseja ver o index: \n "))
print("O index do item: ", lista_index.index(verificar))

print("")
print("")


print("")
print("Verificando e adicionando o item pelo index da lista: ")
lista_inserir = [1,2,3,4,5,6,7,8,9,10]
print(lista_inserir)

pos = int(input("Digite a posição: "))
ele = int(input("Digite o elemento: "))

lista_aux = []

for i in range(len(lista_inserir)):
    if i == pos:
        lista_aux.append(ele)

    lista_aux.append(lista_inserir[i])
lista_inserir = lista_aux

print("Lista =", lista_inserir)


print("")
print("Verificando e adicionando o item pelo index da lista usando INSERT: ")
lista_inserir = [1,2,3,4,5,6,7,8,9,10]
print(lista_inserir)

pos = int(input("Digite a posição: "))
ele = int(input("Digite o elemento: "))

lista_inserir.insert(pos, ele)
print("")

"""




