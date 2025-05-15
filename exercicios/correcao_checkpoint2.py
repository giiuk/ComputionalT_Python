ano = input("Diga seu ano de nascimento: ")
while not ano.isnumeric():
    ano = input("Diga seu ano de nascimento: ")
ano = int(ano)

vinho1 = 'Pérgola'
vinho2 = 'Sangue de Boi'
vinho3 = 'Cantinho do Vale'

preco1 = 10
preco2 = 20
preco3 = 30

qnt1 = 0
qnt2 = 0
qnt3 = 0

idade = 2025 - ano
if idade < 18:
    print("Que feiooo, vô contar p sua mãe!!")
else:
    endereco = input("Diga seu endereço: ")
    while True:
        escolha = input(f"Essas são nossas opções:\n{vinho1} - {preco1}\n"
                        f"{vinho2} - {preco2}\n{vinho3} - {preco3}\nQual você quer?")
        while not (escolha == vinho1 or escolha == vinho2 or escolha == vinho3):
            escolha = input(f"Essas são nossas opções:\n{vinho1} - {preco1}\n"
                            f"{vinho2} - {preco2}\n{vinho3} - {preco3}\nQual você quer?")

        qnt = input(f"Quantas garrafas de {escolha} você quer?\n->")
        while not qnt.isnumeric():
            print("Inválido")
            qnt = input(f"Quantas garrafas de {escolha} você quer?\n->")
        qnt = int(qnt)
        if escolha == vinho1:
            preco = preco1
            qnt1 += qnt
        elif escolha == vinho2:
            preco = preco2
            qnt2 += qnt
        else:
            preco = preco3
            qnt3 += qnt
        valor_total = qnt*preco
        continuar = input("Você quer continuar comprando? S/N\n->")
        while not(continuar == 's' or continuar == 'n'):
            continuar = input("Você quer continuar comprando? S/N\n->")
        if continuar == 'n':
            break
    frete = 10
    if valor_total >= 500:
        print("Frete Grátis!")
        frete = 0
    print(f"Obrigado por comprar aqui! Você comprou:\n{qnt1} - {vinho1}\n{qnt2} - {vinho2}\n{qnt3} - {vinho3}\nTotalizando R${valor_total:.2f}"
          f"\ne seu pedido será entregue em {endereco}")





