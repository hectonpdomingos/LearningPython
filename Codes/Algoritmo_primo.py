n = int(input("Digite o valor de N: "))
div = 0
for i in range(1, n+1):
    primo = True
    for j in range(2, i):
        j = 2
        while j < i and primo:
          if i % j == 0:
            primo = False
        j += 1

    if primo:
        print(i)
print("Fez %i divisões"%div)

