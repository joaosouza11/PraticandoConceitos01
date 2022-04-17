from datetime import date

genero = int(input("""[1] Homem
[2] Mulher
Você se identifica como: """))

if genero == 1:
  atual = date.today().year
  nasc = int(input("Ano de nascimento: "))
  idade = atual - nasc
  print("Quem nasceu em {} fará {} anos em 2022".format(nasc, idade))

  #Para descobrir se é maior de 18
  data_alist = nasc + 18
  if data_alist > atual:
    print("Você terá que se alistar daqui {} anos".format(data_alist-atual))
    print("Seu alistamento será em {}".format(data_alist))
  elif data_alist == atual:
    print("Você terá que se alistar esse ano!")
  else:
    print("Você deveria ter se alistado há {} anos".format(atual-data_alist))
    print("Seu alistamento foi em {}".format(data_alist))
else:
  print("Você não precisa se alistar!")
