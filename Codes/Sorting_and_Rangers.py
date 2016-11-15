animals = ['bear', 'bear', 'pig', 'mouse', 'horse', 'ant']
sorted_animals = sorted(animals)
print('Animals list:  {}'.format(animals))
print('Sorted animals list:   {}'.format(sorted_animals))
animals.sort()

print("Mostrando a lista ordenada alfabeticamente \n")
print('Animals after sort method: {}'.format(animals))


print("Adicionando mais itens na lista e usando o sorting")
more_animals = ['ellefant', 'cow', 'duck', 'olligator', 'dog', 'javali']
more_animals = animals + more_animals
print("    \n")
print("Sem sorting")
print (more_animals)
print("    \n")
print ('Sorting: \n {}'.format(sorted(more_animals)))

print(" Mostrando a quantidade de itens na lista \n")
print(len(more_animals))



print ("Conceito de RANGES   - range(2) \n")
for number in range(2):
    print(number)
print ("  \n")
print ("Conceito de RANGE com Stop  range(0,3)  \n")
for number in range(0, 3):
    print(number)

print ("  \n")
print ("Conceito de RANGE com STOP e Increment range (0, 10, 2) \n")

for number in range(0, 10, 2):
    print(number)


print(" \n")

print(" Usando a função lengh com o Range\n")
letras = ['a', 'b', 'c', 'e', 'f', 'g', 'h', 'i' ]

for item in range(0, len(letras), 2 ):
    print(letras[item])

