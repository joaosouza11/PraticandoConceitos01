from datetime import date

year = date.today().year
nasc = int(input("Ano de nascimento: "))

#Calculando a idade
idade = year - nasc
print("O atleta tem {} anos".format(idade))

if idade <= 9:
  print("Classificação: MIRIM")
elif idade <= 14:
  print("Classificação: INFANTIL")
elif idade <= 19:
  print("Classificação: JÚNIOR")
elif idade <= 25:
  print("Classificação: SÊNIOR")
elif idade > 25:
  print("Classificação: MASTER")
