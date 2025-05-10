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



'''#Exercicio 14
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

while True:
    num = input("Digite um número: ")
    while not num.isnumeric():
        print("Inválido")
        num = input("Digite um número: ")
    num = int(num)
    if num <= 25:
        intervalo1 += 1
    elif num <= 50:
        intervalo2 += 1
    elif num <= 75:
        intervalo3 += 1
    elif num <= 100:
        intervalo4 += 1
    else:
        print("O número precisa ser de 0 até 100")
    proxima = input("Você deseja continuar? S/N\n")
    while not (proxima == 's' or proxima == 'n'):
        proxima = input("Você deseja continuar? S/N\n")
    if proxima == 'n':
        break
print(f"[0-25] - {intervalo1}\n[26-50] - {intervalo2}\n"
      f"[51-75] - {intervalo3}\n[76-100] - {intervalo4}")'''



'''#Exercicio 15
candidato1 = 'João'
candidato2 = 'Roberto'
candidato3 = 'Maria'
candidato4 = 'José'
brancos = 'brancos'
nulos = 'nulos'

total = 0
voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
votoB = 0
votoN = 0

while True:
    opcao = input(f"Escolha:\n{candidato1}\n{candidato2}"
                  f"\n{candidato3}\n{candidato4}"
                  f"\n{brancos}\n{nulos}\n->")
    if not (opcao == candidato1 or opcao == candidato2 or opcao == candidato3 or opcao == candidato4 or opcao == nulos or opcao == brancos):
        print("Opção inválida.")
        opcao = input(f"Escolha:\n{candidato1}\n{candidato2}"
                  f"\n{candidato3}\n{candidato4}"
                  f"\n{brancos}\n{nulos}\n->")
    if opcao == candidato1:
        voto1 += 1
    elif opcao == candidato2:
        voto2 += 1
    elif opcao == candidato3:
        voto3 += 1
    elif opcao == brancos:
        votoB += 1
    else:
        votoN += 1
    total += 1
    proxima = input("Deseja continuar? [S/N]")
    while not (proxima == 's' or proxima == 'n'):
        proxima = input("Deseja continuar? [S/N]")
    if proxima == 'n':
        break
print(f"{candidato1} - {voto1}\n{candidato2} - {voto2}"
      f"\n{candidato3} - `{voto3}\n{candidato4} - {voto3}\n"
      f"{brancos} - {votoB}\n{nulos} - {votoN}")
print(f"Porcentagem de votos nulos sobre o total: {votoN *100/total:.2f}")
print(f"A porcentagem de brancos sobre o total: {votoB *100/total:.2f}")'''