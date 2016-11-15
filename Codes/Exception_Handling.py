animals = ['man', 'bear', 'pig']
print("Procurando o item bear na list ['man', 'bear', 'pig'] \n")
bear_index = animals.index('bear')
print(bear_index)

print("Caso não encontre o item na lista, irá aparecer um erro \n por isso precisamos tratar erros \n")

print("Procurando na lista ['man', 'bear', 'pig'] o item cat \n")

try:
    cat_index = animals.index('cat')
except:
    cat_index = 'No cats found.'
print(cat_index)