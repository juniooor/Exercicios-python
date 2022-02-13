#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('====='*6)
print('     LOJINHA DO DESCONTO')
print('====='*6)
prd=float(input('Digite o valor do produto: '))
escolha=int(input('Escolha: \n [1] Pagamento à vista dinheiro: \n [2]Pagamento à vista Cartão: \n [3]Em até 2x cartão: \n [4]3x ou mais no cartão:'))
if escolha == 1:
    desc=prd*0.1
    total=prd-desc
    print('O desconto é de 10%, você vai pagar R${:.2f}'.format(total))
elif escolha == 2:
    desc=prd*0.05
    total=prd-desc
    print('O desconto é de 5%, Você vai pagar R${:.2f}'.format(total))  
elif escolha == 4:
    desc=prd*0.2
    total=prd+desc
    print('Para compras parceladas no cartão maior que 3x tem juros de 20 %. o Total é R${:.2f}'.format(total))
else:
    print('compras parceladas até 2x não tem desconto. Total de R${}'.format(prd))

