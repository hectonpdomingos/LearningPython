"""a = 0

while a == 0:
    opcao = int(input("Digite 2 para cadastro, 1 para sair"))
    if opcao == 2:
        print("Cadastro de Cliente")
    if opcao == 1:
        a = 1
        print("saindo do programa")


b = 0

while b <= 10:
    print ("Numero: ", b)
    b = b + 1

"""
#exerc encontrar fatorial
n = int(input("Digite um numero: \n"))
fatorial = n
cont = n -1
while cont > 1:
    fatorial = fatorial * cont
    cont = cont - 1

print(n, "! =", fatorial )



# iprima o numero e seu quadrado

n = int(input("Digite o primeiro numero: "))
while n != 0:
    print(n, "ao quadrado =", n*n)
    n = int(input("Digite o próximo numero: "))