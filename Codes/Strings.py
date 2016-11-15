print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")



word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5
word[-1]  # last character
word[-2]  # second-last character



word[0:2]  # characters from position 0 (included) to 2 (excluded)
#'Py'
word[2:5]  # characters from position 2 (included) to 5 (excluded)
#'tho'

word[:2]   # character from the beginning to position 2 (excluded)
#'Py'
word[4:]   # characters from position 4 (included) to the end
#'on'
word[-2:]  # characters from the second-last (included) to the end
#'on'


