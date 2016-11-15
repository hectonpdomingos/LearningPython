import random

#random.ranrange(start, stop[, step])
print("#random.randrange\n")
for i in range(10):
    x = random.randrange(1, 7)
    print(x)


for i in range(10):
    x = random.randrange(1, 7, 2)
    print(x)


#randomint
#retorna um numero inteiro tal forma que a <= N
#<=b
#Tal como randrange(a, b+1)
print("#randomint\n")
for i in range(10):
    x = random.randint(1, 7)
    print(x)

print("#random.choice\n")
#random.choice

for i in range(10):
    x = random.choice([1, 2, 3, 4, 5, 6])
    x = random.choice(range(1, 7))
    print(x)


print("random.random - retorna numero entre real 0.0 e 1.0 \n")

for i in range(10):
    print(random.random())


print("Random.uniforme (a, b)\n")


for i in range(10):
    x = random.uniform(1, 7)
    #x = random.uniform(7, 1)
    print(x)


print("Programa escolha a porta")

testes = int(input("Digite o número de testes: "))
trocar = 0

for i in range(testes):
    porta = random.randrange(1, 4)
    premio = random.randint(1, 3)

    if porta != premio:
        trocar += 1
print("É vantajoso trocar em %.3g %% as vezes"%(trocar*100/testes))
print("Não é vantajoso trocar em %.3g %% as vezes"% ((1 - trocar/testes)*100))



print("Jogo de dados")
vetor = []
for i in range(100):
    vetor.append(random.randint(1,6))

for i in range(1, 7):
    print("A face %i apareceu %i vezes."(i, vetor.count(i)))
    print("A face {} apareceu {} vezes.".format(i, vetor.count(i)))
