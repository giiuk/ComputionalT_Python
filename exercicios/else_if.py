#Exercicios Pyhton - ELSE e IF

'''#Exercício 1 🎆
num1 = float(input("Digite um número:\n-> "))
num2 = float(input("Digite outro número:\n-> "))
if num1 > num2:
  print(f"{num1} é maior que {num2}")
elif num1 == num2:
  print(f"{num1} e {num2} são iguais!!!!!")
else:
  print(f"{num2} é maior que {num1}")'''


'''#Exercício 2 🎁
ano = int(input("Digite seu ano de nascimento:\n->"))
if ano <= 2007:
  print("Você pode votar esse ano!")
else:
  print("Você ainda não pode votar!")'''


'''#Exercício 3 🎨
senha = int(input("Digite sua senha:\n->"))
if senha == 1234:
  print("ACESSO PERMITIDO")
else:
  print("ACESSO NEGADO")'''


'''#Exercício 4 🧧
maça = 0
valor = int(input("Quantas maças você pegou?\n->"))
if valor < 12:
  total = valor * 0.30
  print(f"Você pegou {valor}, o total da compra fica: {total}")
else:
  total = valor * 0.25
  print(f"Você pegou {valor}, o total da compra fica: {total}")
'''


'''#Exercício 5 😜
num1 = int(input("Digite o primeiro número:\n->"))
num2 = int(input("Digite o segundo número:\n->"))
num3 = int(input("Digite o terceiro número:\n->"))
if num1 < num2 and num1 < num3:
  if num2 < num3:
     print(f"Os números em ordem crescente são: {num1}, {num2} e {num3}")
  else:
     print(f"Os números em ordem crescente são: {num1}, {num3} e {num2}")
elif num2 < num1 and num2 < num3:
  if num1< num3:
     print(f"Os números em ordem crescente são: {num2}, {num1},{num3}")
  else:
     print(f"Os números em ordem crescente são: {num2}, {num3},{num1}")
else:
  if num1 < num2:
     print(f"Os números em ordem crescente são: {num3}, {num1},{num2}")
  else:
     print(f"Os números em ordem crescente são: {num3}, {num2},{num1}")'''



'''#Exercício 6 🥾
altura = float(input("Digite a sua altura:\n->"))
sexo = float(input("Qual o seu sexo?\n 1- Feminino\n 2- Masculino\n->"))
if sexo == 1:
  conta = 62.1 * altura - 44.7
  print(f"Seu peso ideal é {conta}")
else:
  conta = 72.7 * altura - 58
  print(f"Seu peso ideal é {conta}")'''


'''#Exercício 7 ✨
lado = int(input("Quantos lados possui o polígono regular?\n->"))
medida = float(input("Qual a medida do lado em centímetros?\n->"))
if lado == 3:
  perimetroT = medida * 3
  print(f"O polígono é um TRIÂNGULO\nO valor do perimetro é: {perimetroT} cm²")
elif lado == 4:
  perimetroQ = medida * 4
  print(f"O polígono é QUADRADO\nO valor da área é {perimetroQ} cm² ")
elif lado == 5:
    perimetroP = medida * 5 
    print(f"O polígono é um PENTÁGONO\nO valor do perimetro é: {perimetroP}")
'''


'''#Exercicio 7 - 8 😎
lado = int(input("Quantos lados possui o polígono regular?\n->"))
if lado < 3:
 print("NÃO É UM POLÍGONO")
elif lado == 3 or lado == 4 or lado == 5:
 medida = float(input("Qual a medida dos lados em centímetros?\n->"))
 if lado == 3:
    perimetroT = medida * 3
    print(f"O polígono é um TRIÂNGULO\nO valor do perímetro é: {perimetroT} cm²")
 elif lado == 4:
    perimetroQ = medida * 4
    print(f"O polígono é QUADRADO\nO valor do perímetro é {perimetroQ} cm² ")
 elif lado == 5:
     perimetroP = medida * 5
     print(f"O polígono é um PENTÁGONO\n O valor do perímetro é {perimetroP}")
else:
 print("POLÍGONO NÃO IDENTIFICADO")'''


'''#Exercicio 9 ✔✔
num1 = int(input("Digite o primeiro número:\n->"))
num2 = int(input("Digite o segundo número:\n-> "))
num3 = int(input("Digite o terceiro número:\n->"))
if num1 < num2 and num1 < num3:
  if num2 < num3:
     print(f"O maior número é: {num3}")
  else:
     print(f"O maior número é: {num2}")
elif num2 < num1 and num2 < num3:
  if num1 < num3:
     print(f"O maior número é: {num3}")
  else:
     print(f"O maior número é: {num1}")
else:
  if num1 < num2:
     print(f"O maior número é: {num2}")
  else:
     print(f"O maior número é: {num1}")'''


'''#Exercicio 10 🐱‍👓
lado1 = float(input("Digite o valor do primeiro lado do triângulo:\n->"))
lado2 = float(input("Digite o valor do segundo lado do triângulo:\n->"))
lado3 = float(input("Digite o valor do terceiro lado do triângulo:\n->"))
if lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
  print("É um triângulo EQUILÁTERO")
elif lado1 != lado2 and lado3 == lado1 or lado3 != lado1 and lado2 == lado1 or lado3 == lado2:
  print("É um triângulo ISÓCELES")
else:
  print("É um triângulo ESCALENO")'''


'''#Exercício 11 🌹🎂- ???
ang1 = float(input("Digite o valor do primeiro ângulo do triângulo:\n->"))
ang2 = float(input("Digite o valor do segundo ângulo do triângulo:\n->"))
ang3 = float(input("Digite o valor do terceiro ângulo do triângulo:\n->"))
if ang1 == 90 or ang2 == 90 or ang3 == 90:
  print("É UM TRIÂNGULO RETÂNGULO")
elif ang1 > 90 or ang2 > 90 or ang3 > 90:
  print("É UM TRIÂNGULO OBTUSÂNGULO")
elif ang1 < 90 or ang2 < 90 or ang3 < 90:
  print("É UM TRIÂNGULO ACUTÂNGULO")
else:
  print("A soma dos ângulos não é válida como um triângulo")'''


