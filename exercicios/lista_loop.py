#Alguns exercicios resolvidos

'''#Exercício 1
nota = int(input("Digite sua nota:\n->"))
while nota > 10:
    print("INVALIDO")
    nota = int(input("Digite sua nota:\n->"))
print(f"Sua nota é de: {nota}")'''

'''#Modo alternativo de resolver
while True:
    nota = input("Digite sua nota:\n->")
    if nota.isnumeric():
        nota = int(nota)
        if nota > 0 and nota < 10:
            break'''


'''#Exercício 2
print("Informações Pessoais")
print("-" * 20)

nome = input("Digite seu nome: ")
while len(nome) < 3:
    print("Nome inválido")
    nome = input("Digite seu nome: ")

while True:
    idade = input("Digite a sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
        print(f"A idade digitada está fora do intervalo de 0 a 150.")
    else:
        print("Deve ser digitado um número.")

sexo = input("Diga 'f' para feminino e 'm' para masculino: ")
while sexo != 'f' and sexo != 'm':
    print("Inválido.")
    sexo = input("Diga 'f' para feminino e 'm' para masculino: ")

civil = input("Qual seu estado cívil:\n[S]Solteiro(a)\n[C]Casado(a)\n[V]Viuvo(a)\n[D]Divorciado(a)\n->").upper()
while not (civil == 'S' or civil == 'C' or civil == 'V' or civil == 'D'):
    print("Inválido")
    civil = input("Qual seu estado cívil:\n[S]Solteiro(a)\n[C]Casado(a)\n[V]Viuvo(a)\n[D]Divorciado(a)\n->").upper()'''


'''#Exercicio 4
i = 0
soma = 0
while i < 5:
    num = input(f"Digite um valor: ")
    while not num.isnumeric():
        print("Inválido.")
        num = input(f"Digite um valor: \n->")
    num = int(num)
    soma = soma + num
    i = i + 1
media = soma/i
print(soma,media)'''


'''#Exercicio 6
print("Login")
print("~" * 10)
senha = '1234'
tentativa = 1
senha_digitada = input("Digite sua senha: ")
while senha_digitada != senha and tentativa < 3:
    print(f"Senha inválida! Agora você possui {3 - tentativa} tentativas.")
    senha_digitada = input("Digite sua senha: ")
    tentativa += 1
if senha_digitada == senha:
    print("ACESSO LIBERADO")
else:
    print("SAI HACKER")'''



'''#Exercicio 8
termo1 = 0
termo2 = 1
numero = int(input("Deseja gerar a série até qual número?\n"))
print(f"{termo1} -> {termo2}", end='')
contador = 3
while contador <= numero:
        termo3 = termo1 + termo2
        print(f" -> {termo3}", end='')
        termo1 = termo2
        termo2 = termo3
        contador += 1
print(" -> FIM")'''

'''#Exercicio 9
i = 0
par = 0
while i < 10:
    valor = input("Digite um valor: ")
    while not valor.isnumeric():
        print("Inválido")
        valor = input("Digite um valor: ")
    valor = int(valor)
    if valor%2 == 0:
        par += 1
    i += 1

print(f"Você digitou {par} números pares e { i - par} números impares.")'''

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







