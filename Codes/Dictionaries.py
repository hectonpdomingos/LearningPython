
print("Declaring the dictionary \n")
contact = {'Jason': '555-0123', 'Hecton': '8419-9539'}
print("Setting variables to key to dictionary index. \n")
hecton_phone = contact['Hecton']
jason_phone = contact['Jason']
print("Calling to result \n")
print ('Dial {} to call Jason.'.format(jason_phone))

print ('Dial {} to call Hecton.'.format(hecton_phone))

print(" Printing the whole dictionary \n")

print(contact)
print("Printing the lengh of the dictionary \n")
print(len(contact))


print("Adding more index on dictionary \n")
contact['Tony'] = '555-666'

print("Printing the new values \n")
print(contact)

print("Deleting items from dictionary \n")
del contact['Tony']

print("After deleted \n")
print(contact)


print("\n")


print("You also can store data this way \n ")

contact_two = {
    'Domingos': ['111-1111', '888-9999'],
    'Joao': '222-2222'
}

print('Domingos:')
print(contact_two['Domingos'])

print('Joao:')
print(contact_two['Joao'])



print('')
print('')
print("Acces values with for loop \n")
for numbers in contact_two['Domingos']:
    print('Phone: {}'.format(numbers))



print('')
print('')
print("Acces values with for loop \n")
for numbers in contact_two:
    print('Phone: {}'.format(contact_two[numbers]))



print("If you want know if there is particular key on the list \n")
if 'Domingos' in contact_two.keys():
    print("Domingo phone numbere is: \n")
    print(contact_two['Domingos'][1])


    print("Searching in differente way \n")
    print('222-2222' in contact_two.values())

    print("2 Searching in differente way \n")
    print(['111-1111', '888-9999'] in contact_two.values())

    print("3 Searching in differente way \n")
    print(['888-9999'] in contact_two.values('Domingos'))
