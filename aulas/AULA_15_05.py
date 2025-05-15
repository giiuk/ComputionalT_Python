'''vogais = 0
for char in 'danilo':
    if char in ['a','e','i','o','u']:
        vogais += 1
print(vogais)'''

'''for i in range(10):
    print(i)'''

'''for i in range(1,10,3): #ini, fim, passo
    print(i)'''

'''for i in range (20,10,-2):
    print(i)'''

'''for i in range(1,11):
    print(f"Tabuada do {i}")
    for j in range(1,11):
        print(f"{i}*{j} = {i*j}")


i = 1
while i < 11:
    j = 1
    print(f"Tabuada do {i}")
    while j < 11:
        print(f"{i}*{j} = {i*j}")
        j +=1
    i += 1
    print()'''

'''lista = [3,True,1.5,'danilo',[]]
for elem in lista:
    print(elem)

print() 
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])'''

'''lista = [3,True,1.5,'danilo',[]]
for elem in lista:
    print(elem)
print()

for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")'''

'''profs = ['Danilo', 'André', 'Gabi','Celso','Yan','Lucas','Luis']
materias = ['Python','Storytelling','Sw&TX','Matemática','Edge','Front','Web']

for i in range (len(profs)):
    print(f"O/a prof {profs[i]} dá {materias[i]}")'''

'''alunos = ['Lucas Sena','Rhariel','Sara','Isabella','Lucas Zago']
notas = [8,8.5,6,4,1]

for i in range (len(alunos)):
    if notas[i] >= 6:
        print(f"O/a aluno(a) {alunos[i]} com nota {notas[i]} está aprovado!!")
    else:
        print(f"O/a aluno(a) {alunos[i]} com nota {notas[i]} está reprovado!!")'''

'''#Exercicio 1
pares = 0
numeros = [9,7,3,5,2,1,8,6,0,4]
for i in range (len(numeros)):
    if numeros[i]%2 == 0:
        pares += 1
print(f"O número de números pares é: {pares}")

#Exercicio 2
#V1
soma = 0
numeros = [9,7,3,5,2,1,8,6,0,4]
for num in numeros:
    soma += num
print(soma)

#V2
soma = 0
for i in range(len(numeros)):
    soma += numeros[i]
print(soma)


#Exercicio3
soma = 0
for i in range(len(numeros)):
    soma += numeros[i]
print(soma)
media = soma/len(numeros)
print(media)
'''

'''lista = []
lista.append(349) #Append adiciona um elemento no final da lista
print(lista)
lista.append(67)
print(lista)
lista.append(765)
print(lista)'''

'''lista = []
for i in range(10):
    num = input("Digite um numero: ")
    while not num.isnumeric():
        num = input("Digite um numero: ")
    num = int(num)
    lista.append(num)
    print(lista)'''

'''
lista = [7,3,8,5,2,0,9,6,10,4]
maior = lista[0]
for num in lista:
    print(f"Vou testar se {num} > {maior}")
    if num > maior:
        print(f"Deu certo, vou trocar {maior} por {num}")
        maior = num
print(f"O maior número em {lista} é {maior}")'''

preco = [600, 50, 80, 1000000, 5]
carros = ['Mustang', 'Up', 'Gol', 'Polinho Turbão Manual', 'Uno']
maior = preco[0]
indice_maior = 0
for i in range(len(preco)):
    # print(f"Vou testar se {preco[i]} > {maior}")
    if preco[i] > maior:
        maior = preco[i]
        indice_maior = i
print(f"O carro mais caro é o {carros[indice_maior]}")