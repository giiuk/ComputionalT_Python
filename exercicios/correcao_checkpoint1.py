#Correção CheckPoint 1

print("Seja bem vindo/a à Vinheria Agnello!!!!")
ano = int(input("Diga seu ano de nascimento: "))
endereco = input("Diga seu endereço:  ")
idade = 2025 - ano
if idade < 18:
   print("QUE FEIO!! VO CONTAR P SUA MÃE😡🤬")
else:
   vinho1 = 'Pérbola'
   vinho2 = 'Sangue de Boi'
   vinho3 = 'Cantinho do Vale'
   preco1 = 50
   preco2 = 30
   preco3 = 10
   escolha = input(f"Esses são os nossos vinhos:\n{vinho1} - {preco1}"
                   f"\n{vinho2} - {preco2}"
                   f"\n{vinho3} - {preco3}\n->")
   qnt = int(input(f"Quantas garrafas de {escolha} você quer?\n->"))
   if escolha == vinho1:
       preco = preco1
   elif escolha == vinho2:
       preco = preco2
   else:
       preco = preco3
   total = qnt*preco
   frete = 10
   if total > 100:
       frete = 0
       print("Frete Grátis!!!!!")
   total += frete
   print(f"Obrigado por comprar conosco, você gastou R${total} e será entregue em: {endereco}")

