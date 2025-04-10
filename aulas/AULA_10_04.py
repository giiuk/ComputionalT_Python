#While

'''
i = 0
pares = 0
num = int(input(f"Diga o {i+1}° número:\n->"))
if num%2 == 0:
   pares = pares + 1
i = i + 1


num = int(input(f"Diga o {i+1}° número:\n->"))
if num%2 == 0:
   pares = pares + 1
i = i + 1


num = int(input(f"Diga o {i+1}° número:\n->"))
if num%2 == 0:
   pares = pares + 1
i = i + 1


num = int(input(f"Diga o {i+1}° número:\n->"))
if num%2 == 0:
   pares = pares + 1
i = i + 1


num = int(input(f"Diga o {i+1}° número:\n->"))
if num%2 == 0:
   pares = pares + 1
i = i + 1


print(f"Você digitou {pares} números pares e {i - pares} números ímpares")
'''

'''
i = 0
pares = 0


while i < 5:
   num = int(input(f"Diga o {i+1}° número:\n->"))
   if num%2 == 0:
       pares = pares + 1
   i = i + 1
print(f"Você digitou {pares} números pares e {i - pares} números ímpares")'''


senha = '1234'
tentativas = 1
acesso = input("Digite sua senha:\n->")
while acesso != senha and tentativas < 3:
   print(f"Você errou! Somente {3 -tentativas} tentativas restantes")
   acesso = input(f"Digite sua senha:\n->")
   tentativas = tentativas + 1

if acesso == senha:
   print("Acesso Liberado")
else:
   print("SAI HACKER!!!!!🤬🤬")

'''genero = input("Digite 'masculino' ou 'feminino':\n-> ")
while genero != 'masculino' and genero != 'feminino':
   print("Inválido")
   genero = input("Digite 'masculino' ou 'feminino':\n-> ")
print(f"Você é do genêro: {genero}")'''

'''genero = input("Digite 'masculino' ou 'feminino':\n-> ")
while not (genero == 'masculino' or genero == 'feminino'):
   print("Inválido")
   genero = input("Digite 'masculino' ou 'feminino':\n-> ")
print(f"Você é do genêro: {genero}")'''

'''
print('dkmks'.isnumeric())
print('18291eje'.isnumeric())
print('1829'.isnumeric())'''

'''num = input("Digite um número:\n->")
while not num.isnumeric():
   print("Você deve digitar um número!!!")
   num = input("Digite um número:\n->")'''

'''i = 0
pares = 0


while i < 5:
   num = int(input(f"Diga o {i+1}º número: "))
   if num%2 == 0:
       pares += 1 #pares = pares + 1
   print(i)
   i += 1 # i = i + 1
print(f"Você digitou {pares} números pares e {i - pares} números ímpares")'''
