vcasa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento: "))

#Parcela não pode passar de 30% do salário
parcela = vcasa / (anos * 12)
validacao = salario * (30 / 100)
if validacao <= parcela:
  print("Seu pedido de empréstimo foi NEGADO!")
else:
  print("Seu pedido de empréstimo foi ACEITO e a prestação será de R${:.2f}".format(parcela))
