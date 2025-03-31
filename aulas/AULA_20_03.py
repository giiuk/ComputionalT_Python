#ELSE e IF

'''
a = 2
b = 3
print(f"A operação {a}<{b} and {a}!={b}, ou seja, {a<b} and {a!=b}, resulta {a<b and a!=b}")


idoso = input("Você é idoso??\n->")
cartaozinho = input("Você tem o CARTÃOZINHO?????\n->")
if idoso == 'sim' and cartaozinho == 'sim':
   print("Pode estacionar!!!👌")
else:
   print("Não pode estacionar!!!")



idoso = input("Você é idoso?\n->")
deficiente = input("Você é deficiente?\n->")
if idoso == 'sim' or deficiente == 'sim':
   print("Pode estacionar!!")
else:
   print("Não pode estacionar!!!!")



letra = input("Digite uma letra:\n->")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
   print("É VOGAL!!!")
else:
   print("Não é vogal 👎👎👎")



time = input("Diga para que time você torce: ")
if time == 'São Paulo':
   print("Trimundial, triberta.")
elif time == 'Palmeiras':
   print("Parabéns pelo bi da serie B")
elif time == 'Corinthians':
   print("Parabéns pela série B")
else:
   print("Parabéns pela série B, o pelé é dahora")



salario = float(input("Digite o seu salário:\n->"))
if salario <= 1903.98:
   print("Sem imposto")
elif salario > 1903.99 and salario <= 2826.85:
   calculo = salario * 0.075
   print(f"O total que você deve pagar de imposto é: {calculo}")
elif salario > 2826.86 and salario <= 3751.05:
   calculo = salario * 0.15
   print(f"O total que você deve pagar de imposto é: {calculo}")
elif salario > 3751.06 and salario <= 4665.69:
   calculo = salario * 0.225
   print(f"O total que você deve pagar de imposto é: {calculo}")
else:
   calculo = salario * 0.275
   print(f"O total que você deve pagar de imposto é: {calculo}")



nome= input("Qual o seu nome?")
entrar = input("Você quer fazer contas?")
if entrar == 'sim':
   num1 = int(input("Digite um número:\n->"))
   num2 = int(input("Digite outro número: \n->"))
   selecao = input("Qual conta deseja fazer: multiplicação, divisão, soma ou subtração?\n->")
   if selecao == 'soma':
       conta1 = num1 + num2
       print(f"O resultado da soma de {num1} + {num2} é igual à {conta1}")
   elif selecao == 'subtração':
       conta2 = num1 - num2
       print(f"O resultado da subtração de {num1} - {num2} é igual à {conta2}")
   elif selecao == 'multiplicação':
       conta3 = num1 * num2
       print(f"O resultado da multiplicação de {num1} * {num2} é igual à {conta3}")
   else:
       conta4 = num1/num2
       print(f"O resultado da divisão de {num1}/{num2} é igual à {conta4}")
else:
   print(f"Beleza, {nome}.")'''
