'''num = input("Diga um número: ")
while not num.isnumeric():
   num = input("Diga um número: ")
num = int(num)
print(type(num))


while num < 0 or num > 10: #not (num >0 and num < 10)'''

'''#Exercicio 1
while True:
   num = input("Diga um numero: ")
   if num.isnumeric():
       num = int(num)
       if num > 0 and num < 10:
           break'''

'''#Exercicio 2
nome = input("Diga seu nome: ")
while len(nome) < 3:
   nome = input("Diga seu nome: ")




while True:
   idade = input("Diga sua idade: ")
   if idade.isnumeric():
       idade = int(idade)
       if idade > 0 and idade < 150:
           break
       print(f"{idade} está fora do intervalo 0 a 150.")
   else:
       print("Deve ser digitado um número!")



salario = input("Diga seu salario: ")
while not salario.isnumeric():
   salario = input("Diga seu salario: ")
salario = int(salario)




sexo = input("Diga f ou m: ")
while sexo != 'f' and sexo != 'm':
   sexo = input("Diga f ou m: ")



e_civil = input("Diga s,c,v ou d: ")
while not (e_civil == 's' or e_civil == 'c' or e_civil == 'v' or e_civil == 'd'):
   e_civil = input("Diga s,c,v ou d: ")'''

'''#Exercicio 3
a = 80
b = 200
t = 0
while a < b:
   a *= 1.03
   b *= 1.015
   t += 1
print(t)'''

'''#Exercicio 4
i = 0
soma = 0
while i < 5:
   nota = input(f"Diga a {i + 1}° nota:")
   while not nota.isnumeric():
       nota = input(f"Diga a {i + 1} nota:")
   nota = int(nota)
   soma += nota
   i += 1
media = soma/i'''

'''#Exercicio 5
a = input(f"Diga o primeiro numero:")
while not a.isnumeric():
   a = input(f"Diga o primeiro numero: ")
a = int(a)


b = input(f"Diga o primeiro numero:")
while not b.isnumeric():
   b = input(f"Diga o primeiro numero: ")
b = int(b)


if b < a:
   aux = a
   a = b
   b = aux


while a <= b:
   print(a, end=' ')
   a += 1'''

'''#Exercicio 6
senha = '1234'
password = input("Diga sua senha: ")
tentativas = 1
while senha != password and tentativas < 3:
   print(f"Você é hacker? {3 - tentativas} tentativas restantes")
   password = input("Diga sua senha: ")
   tentativas += 1
if password == senha:
   print("Acesso LIBERADO")
else:
   print("Sai hacker")'''

'''#Exercicio 7
num = 1
while num <=10:
   print(f"Tabuada do {num}:")
   mult = 1
   while mult <=10:
       print(f"{num}*{mult} = {num*mult}")
       mult += 1
   print()
   num += 1
'''

'''#Exercicio 8
a = 1
b = 1
print(a,b,end=' ')
i = 2
while i < 10:
   c = a + b
   print(c,end=' ')
   a = b
   b = c
   i += 1
'''

'''#Exercicio 9
i = 0
pares = 0
while i < 10:
   b = input(f"Diga o {i + 1}° primeiro numero:")
   while not b.isnumeric():
       b = input(f"Diga o {i + 1}° primeiro numero:")
   b = int(b)
   if b%2 == 0:
       pares += 1
   i += 1
print(f"Você digitou {pares} pares e {i - pares} ímpares")'''

'''#Exercicio 10
i = 1
fatorial = 1
while i < 5:
   i += 1
   fatorial *= i
print(fatorial)




i = 1
fatorial = 1
num = 5
produto = f"{num}! = "
while i < num:
   produto += f"{i}*"
   i += 1
   fatorial *= i
produto += f"{i} = {fatorial}"
print(produto)'''

'''#Exercicio 11
num = 35
i = 2
while True:
   print(f"{num}%{i} = {num%i}")
   if num %i == 0:
       print("Não é primo!")
       break
   elif i >= num**(1/2):
       print("É primo")
       break
   i += 1
'''

# Exercicio 12 - ver exercício 4


'''#Exercicio 13
salario = 1000
ano = 1995
taxa_inicial = 0.015
while ano < 2005:
   taxa = 1 + taxa_inicial
   taxa_inicial *= 2
   salario *= taxa
   ano +=1
print(salario)'''

# Exercicio 14 - Incompleto
intervalo_1 = 0
intervalo_2 = 0
intervalo_3 = 0
intervalo_4 = 0

while True:
    num = input("Diga um numero: ")
    while not num.isnumeric():
        print("Inválido!")
        num = input("Diga um numero: ")
    num = int(num)
    if num < 25:
        intervalo_1 += 1
    elif num < 50:
        intervalo_1 += 1
    elif num < 75:
        intervalo_1 += 1
    elif num < 100:
        intervalo_1 += 1
    else:
        print("Tem que ser entre 0 e 100!")

    continuar = input("Você quer continuar? (s/n)")

