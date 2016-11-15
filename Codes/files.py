"""Input and Output
input() - Accept standard input
print() - Write std output
files are great for storage that lasts beyond
the execution of a program.


open() - built-in function that opens a file and returns a file objet

open(path_to-file)
path_to_file - can be absolute

open('/var/log/messages')
open('log/messages')

##
hosts = open('/etc/hosts')
hosts_file_contents = hosts.read()
print(hosts_file_contents)
##



options

read() - Return the entire file
seek(offset) - Change the current position to offset
seek(0) - Go to beggining of the file
seek(5) - Go to the 5th byte of the file
tell() - Determine the current position of the file



"""


hosts = open('d:/HaxLogs.txt')
hosts_file_contents = hosts.read(9)
print(hosts_file_contents)
print('File closed? {}'.format(hosts.closed))
if not hosts.closed:
    hosts.close()
print('File closed? {}'.format(hosts.closed))

print("  \n")
#print(hosts_file_contents.read(10))
#print(hosts_file_contents.tell())



print("  \n")
print("Read file line by line")

with open('d:/HaxLogs.txt') as the_file:
    for line in the_file:
        print(line)


print("  \n")
print("Read file line by line removing white spaces")

with open('d:/HaxLogs.txt') as the_file:
    for line in the_file:
        print(line.rsplit())

print("  \n")
print("file mode")

with open('d:/HaxLogs.txt') as the_file:
            print(the_file.mode)


print("  \n")
print("file in write mode")

with open('d:/file2.txt', 'w') as the_file:
    the_file.write('This text will be written to the file. \n')
    the_file.write('Here is more text.')

with open('d:/file2.txt') as the_file:
    print(the_file.read())


""" \r carriage Return
    \n New Line
    \n Unix/Linux Mac line ending
    \r\n Windows style line ending
    """
print(" \n ")
""" Exceptions"""
print("  Exceptions \n")
try:
    contacts = open('d:/files2.txt').read(
except:
    contacts = ''
print(len(contacts))




