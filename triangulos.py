s1 = int(input("Segmento 1: "))
s2 = int(input("Segmento 2: "))
s3 = int(input("Segmento 3: "))

#Verificando se pode formar triângulo
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
  print("Os segmentos podem formar um triângulo", end=" ")

  #Todos os lados iguais
  if s1 == s2 == s3:
    print("EQUILÁTERO")

  #Todos os lados diferentes
  elif s1 != s2 != s3 != s1:
    print("ESCALENO")

  else:
    print("ISÓSCELES")
    
else:
  print("Os segmentos não podem formar um triângulo")
