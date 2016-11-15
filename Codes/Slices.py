animals = ['man', 'bear', 'pig', 'cow', 'duck','horse']
some_animals = animals[1:4]
print("Lista original")
print('Some animals: {}'.format(some_animals))


print("Usando slices com lista, extraindo dois primeiros itens")
first_two = animals[0:2]
print('First two animals: {}'.format(first_two))

first_two_again = animals[:2]
print('First two animals: {}'.format(first_two_again))


#Segundo exemplo

print("Usando slices com lista, extraindo dois ultimos itens")
last_two = animals[4:6]
print('Last two: {}'.format(last_two))

last_two_again = animals[-2:]
print('Last two again {}'.format(last_two_again))


#sTRINGS
print("Usando slices com strings")
part_of_horse = 'horse'[1:3]
print(part_of_horse)