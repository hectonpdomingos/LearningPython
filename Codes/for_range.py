n = 7
for cont in range(n):
    print("cont: ", cont)



for i in range(2, 6):
    print("i: ", i)


for j in range(2, 12, 2):
    print("j: ", j)



for w in range(10, 0, -2):
    print("w: ", w)

#fatorial

n = int(input("Digite o valor de n: "))
fatorial = 1

for fator in range(2, n+1):
    fatorial *= fator
print("%i! é igual a %i"%(n, fatorial))


#numeros triangulares

for m in range(5, 51, 5):
    triangular = m*(m+1)//2
    print("o número {} e sua triangular {}".format(m, triangular))