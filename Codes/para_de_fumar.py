""" # Ask for the distance.
distance = input('How far would you like to travel in miles? ')
# Convert the distance to an integer.
distance = int(distance)
# Determine what mode of transport to use.
if distance < 3:
  mode_of_transport = 'walking'
elif distance < 300:
  mode_of_transport = 'driving'
else:     mode_of_transport = 'flying'
# Display the result.
print('I suggest {} to your destination.'.format(mode_of_transport))  """

# INDEX
print ("Em um index conento valores ['Zero', 'Um', 'Dois', 'Três']")
Exemplo_index = ['Zero', 'Um', 'Dois', 'Três']
print ("Mostrando primeiro item, na posição 0")
print (Exemplo_index[0])
print ("Mostrando o ultimo item do index")
print (Exemplo_index[-1])

#aDICIONANDO ITEM NO FIM DA LIST
print ("Adicionando mais um item no fim do index, usando a função .append")
Exemplo_index.append('Quatro')
print ("Mostrando o ultimo item do index após a adição")
print (Exemplo_index[-1])

#Criando um segundo list

Exemplo_dois_index = ['Cinco', 'Seis', 'Sete', 'Oito']
print ("Mostrando todo Index Exemplo_dois-Index")
print (Exemplo_dois_index)

#Extendendo a lista Exemplo_index com o Exemplo_dois_index
print ("Extendendo a lista Exemplo_index com o Exemplo_dois_index")
Exemplo_index.extend(Exemplo_dois_index)

print("mostrando a união das listas")
print(Exemplo_index)
