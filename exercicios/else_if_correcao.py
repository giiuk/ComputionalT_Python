#EXERCICIOS ELSE e IF CORRIGIDOS

'''#EXERCICIO 1 💖
#Primeira maneira
num_a = int(input("Diga um numero: "))
num_b = int(input("Diga outro numero: "))
if num_a > num_b:
    print(f"{num_a} é o maior")
else:
    print(f"{num_b} é o maior")

#Segunda maneira
num_a = int(input("Diga um numero: "))
num_b = int(input("Diga outro numero: "))
if num_a > num_b:
    print(f"{num_a} é o maior")
elif num_b > num_a:
    print(f"{num_b} é o maior")
else:
    print("Os valores deveriam ter sido diferentes entre si.")'''


'''#EXERCICIO 2 🐱‍🐉
ano = int(input("Diga seu ano de nascimento: "))
idade = 2025 - ano
if idade < 16:
    print("Sai catarrento")
elif idade < 18 or idade >= 70:
    print("Pode votar (opcional)!")
else:
    print("Voto obrigatório")'''

'''#EXERCICIO 3‍🐱‍👤
senha = 1234
tentativa = (input("Digite sua senha:\n->"))
if senha == tentativa:
   print("ACESSO PERMITIDO")
else:
   print("SAI HACKER")'''

'''#EXERCICIO 4 🙌
quantidade = int(input("Diga a quantidade de maçãs: "))
preco = 0.3
if quantidade >= 12:
   preco = 0.25
total = quantidade * preco
print(f"Você pagará R${preco:.2f} por maça, totalizando {total}")'''

'''#EXERCICIO 5 💋
#Primeira maneira
a = int(input("Diga o primeiro valor: "))
b = int(input("Diga o segundo valor: "))
c = int(input("Diga o terceiro valor: "))
if a > b and a > c:
   aux = a
   a = c
   c = aux
elif b > c:
   aux = b
   b = c
   c = aux
if b < a:
   aux = a
   a = b
   b = aux
   
print(a,b,c)

#Segunda Maneira 
a = int(input("Diga o primeiro valor: "))
b = int(input("Diga o segundo valor: "))
c = int(input("Diga o terceiro valor: "))
maior = a
if b > maior:
   maior = b
if c > maior:
   maior = c


menor = a
if b < menor:
   menor = b
if c < menor:
   menor = c


meio = a + b + c - menor - maior
print(menor,meio,maior)'''

'''#EXERCICIO 6 😎
altura = float(input("Diga a sua altura:\n->"))
genero = input("Digite 'masculino' ou 'feminino':\n->")
peso_ideal = 62.1 * altura - 44.7
if genero == 'masculino':
   peso_ideal = 72.7 * altura - 58
print(f"O peso ideal para pessoas do genero {genero} e altura de {altura} é {peso_ideal:.2f}kg")
'''

'''#EXERCICIOS 7 e 8 ✨
lados = int(input("Diga a qtd de lados: "))
medida = float(input("Diga a medida do lado: "))
if lados < 3:
    print("Não é um polígono!!")
elif lados == 3:
    perimetro = lados*medida
    print(f"Triângulo de perímetro {perimetro}")
elif lados == 4:
    perimetro = lados * medida
    print(f"Quadrado de perímetro {perimetro}")
elif lados == 5:
    perimetro = lados * medida
    print(f"Pentágono de perímetro {perimetro}")
else:
    print("Polígono não identificado!")
    
    
#Segunda maneira
lados = int(input("Diga a qtd de lados: "))
if lados < 3:
    print("Não é um polígono!!")
elif lados > 5:
    print("Polígono não identificado!")
else:
    medida = float(input("Diga a medida do lado: "))
    perimetro = lados * medida
    if lados == 3:
        forma = 'Triangulo'
    elif lados == 4:
        forma = "Quadrado"
    else:
        forma = "Pentágono"
    print(f"{forma} de perímetro {perimetro}")'''


'''#EXERCICIO 9 🎨
a = int(input("Diga o primeiro valor: "))
b = int(input("Diga o segundo valor: "))
c = int(input("Diga o terceiro valor: "))
if a > b and a > c:
   print(f"O {a} é o maior")
elif b > c:
   print(f"o {b} é o maior")
else:
   print(f"O {c} é o maior")'''


'''#EXERCICIO 10 🍟
lado1 = int(input("Diga o primeiro lado:"))
lado2 = int(input("Diga o segundo lado:"))
lado3 = int(input("Diga o terceiro lado:"))
if lado1 == lado2 and lado1 == lado3:
   print("Esse triângulo é equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
   print("Esse triângulo é isóceles")
else:
   print("Escaleno")'''

'''#EXERCICIO 11 🍙
ang1 = int(input("Diga o primeiro angulo:\n->"))
ang2 = int(input("Diga o segundo angulo:\n->"))
ang3 = int(input("Diga o terceiro angulo:\n->"))
if ang1 + ang2 + ang3 == 180:
    if ang1 == 90 or ang2 == 90 or ang3 == 90:
        print("É um triângulo RETÂNGULO!")
    elif ang1 > 90 or ang2 > 90 or ang3 > 90:
        print("É um triângulo OBTUSO!")
    else:
        print("É um triângulo AGUDO!")

else:
    print("Esses angulos não formam um triangulo!!!!!!!!!")
'''