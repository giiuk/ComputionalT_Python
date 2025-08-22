#Revisão de Lista de Exercícios e For

'''#Exercicio 4
qnt = int(input("Quantas maças você comprou?\n->"))
preco = 0.30
if qnt >= 12:
   preco = 0.25
total = qnt * preco
print(f"Você pagará R${preco:.2f} por maça, totalizando R${total}")'''

'''#Exercicio 5
num_1 = int(input("Digite o primeiro número:\n->"))
num_2 = int(input("Digite o segundo número:\n->"))
num_3 = int(input("Digite o terceiro número:\n->"))


maior = num_1
if num_2 > maior:
   maior = num_2
if num_3 > maior:
   maior = num_3


menor = num_1
if num_2 < menor:
   menor = num_2
if num_3 < menor:
   menor = num_3


meio = num_1 + num_2 + num_3 - menor - maior
print(menor, meio, maior)'''

'''#Exercicio 6
altura = float(input("Digite sua altura:\n->"))
genero = input("Digite 'masculino' ou 'feminino'\n->")
peso_ideal = 62.1 * altura - 44.7
if genero == 'masculino':
   peso_ideal = 72.7 * altura - 58
print(f"O peso ideal para pessoas do gênero: {genero} é de {peso_ideal:.2f}")'''

'''#Exercicio 7 e 8
qnt_lados = int(input("Quantos lados possui o polígono?\n->"))
medida_lado = float(input("Qual a medida do lado (em cm)?\n->"))
perimetro = qnt_lados * medida_lado
if qnt_lados == 3:
   print(f"É um triângulo!\nO valor do perímetro é: {perimetro}")
elif qnt_lados == 4:
   print(f"É um quadrado!\nO valor do perímetro é: {perimetro}")
elif qnt_lados == 5:
   print(f"É um pentagono!\nO valor do perímetro é: {perimetro}")
elif qnt_lados < 3:
   print("Não é um polígono!!!!!!!!")
else:
   print("Polígono não identificado.")'''

'''#Exercicio 9
a = int(input("Digite o primeiro número:\n->"))
b = int(input("Digite o segundo número:\n->"))
c = int(input("Digite o terceiro número:\n->"))


if a > b and a > c:
   print(f"O maior número é {a}")
elif b > c:
   print(f"O maior número é {b}")
else:
   print(f"O maior número é {c}")'''

# Correção
# 4
'''qnt = int(input("Diga a qnt de maças:"))
if qnt > 12:
   preco = 0.25
else:
   preco = 0.30
print(f"Vai custar R${qnt+preco:.2f}")'''

'''#6
sexo = input("Diga 1 para feminino e 2 para masculino: ")
altura = float(input("Digite sua altura: "))
if sexo == '1':
   peso = 62.1 * altura - 47
else:
   peso = 72.7 * altura - 58
print(f"Peso é {peso}kg")
'''

'''#7 e 8
lados = int(input("Diga quantos lados: "))


if lados < 3:
   print("Não é um polígono")
elif lados > 5:
   print("Polígono não identificado")
else:
   medida = int(input("Diga a medida: "))
   if lados == 3:
       print(f"Triângulo")
   elif lados == 4:
       print("Quadrado")
   else:
       print("Pentagono")
   perimetro = lados*medida
   print(perimetro)'''

'''#9
a = int(input("Diga um número: "))
b = int(input("Diga um número: "))
c = int(input("Diga um número: "))


if a > b and a > c:
   print(f"Maior número é {a}")
elif b > c:
   print(f"Maior número é {b}")
else:
   print(f"Maior número é {c}")

##
maior = a
if b > maior:
   maior = b
if c > b:
   maior = c
print(maior)'''

'''#5
a = int(input("Diga um número: "))
b = int(input("Diga um número: "))
c = int(input("Diga um número: "))


maior = a
if b > maior:
   maior = b
if c > b:
   maior = c




menor = a
if b < menor:
   menor = b
if c < menor:
   c = menor


meio = a + b + c - maior - menor
print(menor, meio, maior)'''

'''a = int(input("Diga um número: "))
b = int(input("Diga um número: "))
c = int(input("Diga um número: "))


if a>b and a>c:
   aux = a
   a = c
   c = aux
elif b>c:
   aux = b
   b = c
   c = aux
if a > b:
   aux = a
   a = b
   b = aux


print(a,b,c)'''

# Lista loop
'''#Exercicio 2
nome = input("Digite seu nome: ")
while len(nome) < 3:
   nome = input("Digite seu nome: ")


while True:
   idade = input("Digite sua idade: ")
   if idade.isnumeric():
       idade = int(idade)
       if idade > 0 and idade < 150:
           break
       print("A idade digitada está fora do intervalo")
   else:
       print("Deve ser digitado um número")


salario = input("Diga seu salário: ")
while not salario.isnumeric():
   print("Tem que ser número!")
   salario = input("Diga seu salário: ")


sexo = input("Digite 'f' para feminino e 'm' para masculino:\n-> ")
while (sexo != 'f' and sexo != 'm'):
   print("Inválido")
   sexo = input("Digite 'f' para feminino e 'm' para masculino:\n-> ")


#while not so para or e ==


civil = input("Qual o seu estado civil?\n->[C]Casado(a)\n->[V]Viuvo(a)\n->[S]Solteiro(a)\n->[D]Divorciado(a)\n->")
while not (civil == 'c' or civil == 'v' or civil == 'd' or civil == 's'):
   print("Inválido")
   civil = input("Qual o seu estado civil?\n->[C]Casado(a)\n->[V]Viuvo(a)\n->[S]Solteiro(a)\n[D]Divorciado(a)\n->")'''

'''#Exercicio 3
a = 80
b = 200
t = 0
while a < b:
   a *= 1.033
   b *= 1.015
   t += 1
print(t)


#Exercicio 6
nome = input("Cadastre seu usuário: ")
senha = input("Cadastre sua senha: ")
while senha == nome:
   print("Senha e nome de usuário não podem ser iguais!")
   senha = input("Cadastre sua senha: ")


senha_cadastrada = '1234'
tentativa = 1
senha = input("Digite sua senha: ")


while senha != senha_cadastrada and tentativa < 3:
   print("Você é hacker??????")
   tentativa += 1
if senha == senha_cadastrada:
   print("Acesso liberado!")
else:
   print("Acesso negado")'''

# Exercicio 7
'''i = 2
while i < 11:
   print(f"Tabuada do {i}")
   j = 1
   while j < 11:
       print(f"{i}*{j} = {i*j}")
       j += 1
   i += 1
   print()'''

for i in range(1, 11):
    print(f"Tabuada do {i}: ")
    for j in range(1, 11):
        print(f"{i}*{j} = {i * j}")
    print()

