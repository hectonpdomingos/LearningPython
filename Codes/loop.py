#looping through a list
"""
 for item_variable in list_name:
         Code block

         """


print ("for loop \n")
animals = ['man', 'bear', 'pig']
for animals in animals:
    print(animals.upper())



#WHILE LOOP

"""
  while condition:
    Code block

    """

print (" \n")
print ("While loop \n")

animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']

index = 0

while index < len(animals):
    print(animals[index])
    index +=1

