peso = float(input("Seu peso (kg): "))
altura = float(input("Sua altura (m): "))

#Calculando IMC
imc = peso / (altura ** 2)

print("Seu IMC é de {:.1f}".format(imc))
if imc < 18.5:
  print("Você está abaixo do peso")
elif imc <= 25:
  print("Você está no peso ideal")
elif imc <= 30:
  print("Você está com sobrepeso")
elif imc <= 40:
  print("Você está com obesidade")
elif imc > 40:
  print("Você está com obesidade mórbida")
