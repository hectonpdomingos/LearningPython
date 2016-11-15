area = int(input("Type the area to paint: "))

# // means that you want just int result
litros = area//3
if area % 3 > 0:
    litros = litros + 1

latas = litros//18
if litros % 18 > 0:
    latas = latas + 1

print(litros)
print(latas)
print(latas + 18)


######################3

idade = int(input("Digite sua idade: "))
if idade >= 18:
    if idade < 70:
        print("Você pode receber o benefício")
    else:
        print("VocÊ não pode receber o benefício")
else:
    print("Você não pode receber o benefício")


############################