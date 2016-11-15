"""
Aprendizado em Python
"""

print("Custo operacional dos servidor")

custo_hora = 1
custo_dia = 24 * custo_hora
custo_mes = 30 * custo_dia

custo_vinte_servers_dia = 20 * custo_dia
custo_vinte_servers_mes = 30 * custo_vinte_servers_dia

orcamento = 50000

print("Custo operacional dos servidor/dia ", custo_vinte_servers_dia)
print('Custo operacional dos servidor/Mes R${:.2f}'.format(custo_vinte_servers_mes))
print('Tempo de operação com o orcamento {:.2f}.'.format(orcamento / custo_vinte_servers_dia))
liberado = True
total = float('{:.2f}'.format(orcamento / custo_vinte_servers_dia))
print("total ", total)
if orcamento / custo_vinte_servers_dia < 0:
    print('We need a bigger budget')
    liberado = True
    print('Situação ', + liberado)
elif total > 104.17 :
    print('Right on!')
    Liberado = False
    print('Situação ', + liberado)
else:
    print('Its ok')




