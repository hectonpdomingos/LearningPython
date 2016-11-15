import re
import fileinput

opcao = 99

while opcao != 0:
    print("Digite 1 para verificar a segurança do sistema ")
    print("Digite 2 para aplicar segurança básica no Firewall")
    print("Digite 3 para aplicar segurança básica no FTP")
    print("Digite 4 para aplicar segurança básica no SHH")
    print("Digite 5 para aplicar segurança básica no GRUB")
    print("Digite 6 para aplicar criptgrafia em uma partição")

    print("Digite 0 para Sair")
    opcao = int(input("\n"))
    if opcao == 1:
            print("Opção escolhida {}".format(opcao))
    if opcao == 2:
        print("Opção escolhida {}".format(opcao))
    if opcao == 3:
        print("Opção escolhida {}".format(opcao))
    if opcao == 4:
        print("Opção escolhida {}".format(opcao))
    if opcao == 5:
        print("Opção escolhida {}".format(opcao))
    if opcao == 6:
        print("Opção escolhida {}".format(opcao))

        fin = open("D:/a.txt")
        fout = open("D:/b.txt", "wt")
        for line in fin:
           fout.write(line.replace('Hecton', '#Hecton'))
        fin.close()
        fout.close()



    if opcao == 7:
        print("Opção escolhida {}".format(opcao))
        opcao = 0