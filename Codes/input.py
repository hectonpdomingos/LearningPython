# todos os dados capturados pelo input são strings
#mas é possivel já passar os dados convertidos



age = int(input("Type your age"))

#setting boolean condition to print False or True
answer = age >=18
if answer == True:
    print("You can drink.\n")
if answer == False:
    print("You can't drink. \n")
print(answer)



#second exemple

if age >= 18:
    print("You can drink\n")
    if age >=21:
        print("You are VIP")
else:
    print("You can drink only soda")


#formatação do print - maior , menor e temperatura media

num = int(input("Digite o numero da temperatura registada:"))
soma = maior = menor = float(input("Digite a temperatura 1:"))
for i in range(2, num+1):
    temp = float(input("dIGITE A TEMPERATURA %d: "%i))

    if temp > maior:
        maior = temp
    if temp < menor:
        menor = temp

    #média da temperatura
    soma += temp

#limitando a saida d print a duas casas decimais - com 6 espaços para valores
print("A maior temperatura é %6.2 ºC"%maior)
print("A menor temperatura é %6.2f ºC"%menor)
print("A média das temperaturas é %6.2f ºC"%(soma/num))

#Para colocar em notação cientifica use %g   ex;  print("%g"%x)