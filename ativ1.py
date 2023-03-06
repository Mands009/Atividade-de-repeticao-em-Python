# O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de dez caixas. Para agilizar o cálculo de quanto cada cliente deve pagar, ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Dessa forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o Programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

#Lojas Quase Dois
#-Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98 •
#... 
#50 - R$ 99.50

x = 1
valor = 1.99

print("\nLojas Quase Dois - Tabelas de preços\n")

while x <= 50:
    print("%02.d - R$ %.2f"%(x,x*valor))
    x += 1