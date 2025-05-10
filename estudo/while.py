'''c = 0
while c < 10:
    print(c)
    c = c + 1
print('Fim')
'''

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input("Quer continuar? [S/N]")).upper()
print('Fim')'''

'''n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n%2 == 0:
            par = par + 1
        else: impar = impar + 1
print(f'Voce digitou {par} números pares e {impar} números impares!')'''


'''sexo = str(input("Digite 'M' para Masculino ou 'F' para feminino:\n")).upper()
while not (sexo == 'M' or sexo == 'F'):
    sexo = str(input("Digite 'M' para Masculino ou 'F' para feminino:\n")).upper()
print(f"Seu sexo é: {sexo}")'''


'''
#Exercicio Gen/Sex
sexo = str(input("Digite 'M' para Masculino ou 'F' para feminino:\n")).upper()
while sexo != 'M' and sexo != 'F':
    print("Inválido")
    sexo = str(input("Digite 'M' para Masculino ou 'F' para feminino:\n")).upper()
print(f"Seu sexo é: {sexo}")'''

'''
#Adivinhar número
import random
numero_aleatorio = random.randint(1,10)
print(numero_aleatorio)
i = 1
palpite = int(input("Adivinhe qual o numero.\nDigite um número de 1 a 10\n->"))
while palpite != numero_aleatorio:
    print("ERROU!")
    palpite = int(input("Digite novamente um número de 1 a 10\n->"))
    i = i + 1
print(f"Você acertou!\nSuas tentativas foram: {i}")'''


'''#Exercicio Calculadora
print("Bem vindo(a) a calculadora!")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
menu = 0
while menu != 5 and menu < 5:
    print("[1]SOMA\n[2]MULTIPLICAÇÃO\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA\n")
    menu = int(input("Qual operação vc quer fazer?\n->"))
    if menu == 1:
        soma = num1 + num2
        print(f"A soma entre {num1} e {num2} é igual a {soma}")
    elif menu == 2:
        mult = num1 * num2
        print(f"A multiplicação entre {num1} e {num2} é igual a {mult}")
    elif menu == 3:
        if num1 > num2:
            maior = num1

        else:
            maior = num2
        print(f"O maior número é: {maior}")
    elif menu == 4:
        print("Informe os números novamente: ")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    elif menu == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente")
    print("=-=" * 10)
print("Fim do programa! Volte sempre!")'''

'''
#Exercicio Fatorial
n = int(input("Digite um número para calcular Fatorial: "))
contador = n
fatorial = 1
print(f"Calculando {n}! = ", end='')
while contador > 0:
    print(f'{contador} ', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador -= 1

print(f"{fatorial}")'''

'''
#Exercicio Gerador de PA
print("Gerador de PA")
print('=-=' * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
contador = 1
while contador <= 10:
    print(f"{termo} -> ", end='')
    termo += razao
    contador += 1
print("FIM.")'''

'''
#Exercicio Fibonacci
print("Sequência de Fibonacci")
n = int(input('Quantos termos você quer mostrar?\n:'))
termo1 = 0
termo2 = 1
print(termo1," -> ",termo2, end='')
contador = 3
while contador <= n:
    termo3 = termo1 + termo2
    print(' -> ', termo3, end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print(" -> FIM ")'''


#Exercicio  2

#a
nome = input("Digite seu nome: ")
while len(nome) < 3:
    print("Inválido")
    nome = input("Digite seu nome: ")

#b
while True:
    idade = input("Digite sua idade: ")
    while not idade.isnumeric():
        print("Inválido!!")
        idade = input("Digite sua idade: ")
    idade = int(idade)
    if idade > 0 and idade < 150:
        break
    else:
        print("Precisa ter até 150 anos")

#c
while True:
    salario = input("Digite seu salário: ")
    while not salario.isnumeric():
        print("Inválido!!")
        salario = input("Digite seu salário: ")
    salario = int(salario)
    if salario > 0:
        break
    else:
        print("Digite um valor maior que 0")

#d
sexo = input("Digite seu sexo:\n[F] - Feminino\n[M] - Masculino\n->")
while sexo != 'f' and sexo != 'm':
    print("Inválido.")
    sexo = input("Digite seu sexo:\n[F] - Feminino\n[M] - Masculino\n->")


