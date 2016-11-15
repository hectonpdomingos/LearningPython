n = int(input("Digite o tamanho da sequência: "))
ant = int(input("Digite o numero 1: "))
cont = seg = segMAX = 1
while cont < n:
    prox = int(input("Digite o numero %i: "%(cont+1)))
    if prox > ant:
        seg += 1
    else:
        seg = 1
        if seg > segMAX:
            segMAX = seg
            cont += 1
            ant = prox
            print("O maior segmento crescente da sequência é", segMAX)
