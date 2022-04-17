num = int(input("Digite um número inteiro: "))

print("""Você gostaria de converter este número para qual base?
[1] Binário
[2] Octal
[3] Hexadecimal""")

opcao = int(input("Escolha sua opção: "))
if opcao == 1:
  print("{} convertido para BINÁRIO fica {}".format(num, bin(num)[2:]))
elif opcao == 2:
  print("{} convertido para OCTAL fica {}".format(num, oct(num)[2:]))
elif opcao == 3:
  print("{} convertido para HEXADECIMAL fica {}".format(num, hex(num)[2:]))
else:
  print("Esse não é um número válido!")
