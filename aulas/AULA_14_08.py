#Aula For e Funções

'''
for i in range(1,11):
   print(f"Tabuada do {i}")
   for j in range(1,11):
       print(f"{i}*{j} = {i*j}")
   print()'''

'''lista = [3,'danilo',0.5,True]
for i in range(len(lista)):
   print(f"lista[{i}] = {lista[i]}")

for elem in lista:
   print(elem)'''

'''lista = [4,1,5,7,3,6,9,2,10,8]
soma = 0
for i in range(len(lista)):
   soma += lista[i]
   i += 1
   print(soma)
media = soma/len(lista)
print(media)'''

'''lista = []
print(lista)
lista.append(1)
print(lista)'''

'''def verifica_numero(msg):
   num = input(msg)
   while not num.isnumeric():
       num = input(msg)
   num = int(num)
   return num


qnt = verifica_numero("Quantos números você quer na lista?\n->")
lista = []
i = 1


for i in range(qnt):
   num = verifica_numero(f"Diga o {i +1} número:")
   lista.append(num)


pares = 0
for num in lista:
   if num % 2 == 0:
       pares += 1
impar = len(lista) - pares
print(f"Listas: {lista}\nPares: {pares}\nImpares: {impar}")'''

'''def acha_media(lista):
   soma = 0
   for num in numeros:
       soma += num
   media = soma/len(numeros)
   return media


numeros = [1,5,2,621,78,154,8]
media = acha_media(numeros)
print(media)
media = acha_media([10,2,7,4])
print(media)'''
'''


lista = [3,1,2]
def local_maior(lista):
   indice_maior = 0
   maior = lista[indice_maior]
   for i in range(len(lista)):
       if lista[i] > maior:
           indice_maior = i
           maior = lista[indice_maior]
   return indice_maior


def local_menor(lista):
   indice_menor = 0
   menor = lista[indice_menor]
   for i in range(len(lista)):
       if lista[i] < menor:
           indice_menor = i
           menor = lista[indice_menor]
   return indice_menor


def verifica_numero(msg):
   num = input(msg)
   while not num.isnumeric():
       num = input(msg)
   num = int(num)
   return num'''

'''def forca_escolha(msg,lista_opcoes):
   opcoes = '\n'.join(lista_opcoes)
   escolha = input(f"{msg}\n{opcoes}\n->")
   while escolha not in lista_opcoes:
       escolha = input(f"{msg}\n{opcoes}\n->")
   return escolha
def acha_indice(elem,lista):
   for i in range(len(lista)):
       if lista [i] == elem:
           return i


carros = ['up','gol','polinho turbão manual','uno']
precos = [10,20,1000000,100]
#s_ou_n = ['sim', 'não']
#continuar = forca_escolha("Você quer continuar? ",s_ou_n)
carro = forca_escolha("Qual carro você quer? " , carros)
indice_carro = acha_indice(carro,carros)
print(f"O {carros[indice_carro]} custa R${precos[indice_carro]}")
indice_mais_caro: local_maior(precos)
print(f"O carro mais caro é o {carros[indice_mais_caro]} e custa R${precos[indice_mais_caro]}")'''
