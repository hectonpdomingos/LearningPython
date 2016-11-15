""" A tuble is an immutable list
tubles are ordered
values accessed by index
interation, looping concatenation
use when data should not change

to delete tuple use

del tuple_name

to convert tuple in list use

list ()

tuple_name = list(item_1, item_2)

Lists can be coverted to tuple using

tuple()


"""


days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
Monday = days_of_week[0]
print(Monday)
print()


for day in days_of_week:
    print(day)

print("Looping the tuple \n")

weekend_days = ('Saturday', 'Sunday')
for day in weekend_days:
    print(day)

print(" \n")
print("Using tuples to assign multiples variables at once \n")

weekend_days = ('Saturday', 'Sunday')
(sat, sun) = weekend_days
print(sat)
print(sun)

print(" ")

print("Tuples assign Lists \n ")
contact_info = ['555-0123', 'hectonpdomingos@gmail.com']
(phone, email) = contact_info
print(phone)
print(email)

print("Function to show the highest and lowest number \n")
def high_and_low(numbers):
    """Determine the highest and lowest number"""
    highest = max(numbers)
    lowest = min(numbers)
    return (highest, lowest)
loterry_numbers = [16, 4, 42, 15, 23, 8]
(highest, lowest) = high_and_low(loterry_numbers)
print('The highest number is: {}'.format(highest))
print('The lowest number is:  {}'.format(lowest))


print("for loop to tuple list \n")
contacts = [('Jason', '555-0123'), ('Carl', '555-0987')]
for (name, phone) in contacts:
    print("{}'s phone number is {}.".format(name, phone))