print("{:=^30}".format(" LOJÃO DO JOÃO "))
preco = float(input("Preço das compras: R$"))
print("""\nFORMAS DE PAGEMENTO
[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
""")

opcao = int(input("Qual é a opção? "))

#10% de desconto
if opcao == 1:
  total = preco - (preco * 10 / 100)

#5% de desconto
elif opcao == 2:
  total = preco - (preco * 5 / 100)

#Parcelas 2x sem juros
elif opcao == 3:
  total = preco
  parcela = total / 2
  print("Sua compra será parcelada em 2x de {:.2f} SEM JUROS".format(parcela))

#Parcelas 3x com juros de 20%
elif opcao == 4:
  total = preco + (preco * 20 / 100)
  tparcela = int(input("Quantidade de parcelas: "))
  parcela = total / tparcela
  print("Sua compra será parcelada em {}x de {:.2f} COM JUROS".format(tparcela, parcela))

#Opção inválida
else:
  print("Opção inválida de pagamento!")

print("Sua compra de R${:.2f} vai ficar R${:.2f} no final!".format(preco, total))
