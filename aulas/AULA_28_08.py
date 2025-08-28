import matplotlib.pyplot as plt
#print(matriz[0])
#print(type(matriz[0]))
#print(matriz[0][2])
#print(matriz[2][1])


def elementos_matriz(matriz):
   for i in range (len(matriz)):
       for j in range (len(matriz[0])):
           print(f"matriz[{i}][{j}] = {matriz[i][j]}")
   return


def mostra_matriz(matriz):
   for linha in matriz:
       print(linha)
   return

def cria_matriz(linhas,colunas):
   matriz = []
   for i in range (linhas):
       lista = []
       for j in range (colunas):
           lista.append(0)
       matriz.append(lista)
   return matriz


def plotar_matriz(matriz):
   plt.imshow(matriz)
   plt.colorbar()
   plt.show()
   return


#imagem = cria_matriz(10,10)
#mostra_matriz(imagem)
#plotar_matriz(imagem)


def diagonal_ruim(matriz):
   for i in range (len(matriz)):
       for j in range(len(matriz[0])):
           if i == j:
               matriz[i][j] = 1


def diagonal_bom(matriz):
   for i in range (len(matriz)):
       matriz[i][i] = 1


#plotar_matriz(matriz)


def contra_diagonal_ruim(matriz):
   matriz = cria_matriz(10,10)
   for i in range(len(matriz)):
       for j in range(len(matriz[0])):
           if j == len(matriz[j])-1-i:
               matriz[i][j] = 1


def contra_diagonal_bom(matriz):
   for i in range(len(matriz)):
       j = len(matriz) - i - 1
       matriz[i][j] = 1
   return


#i + j = len(matriz) - 1
#j = len(matriz)-1 - i
#i = linhas, j = colunas


#Xadrez
xadrez = cria_matriz(8,8)
def xadrez_ruim(xadrez):
   for i in range(len(xadrez)):
       for j in range(len(xadrez[0])):
           if i %2 == 0:
               if j%2 ==0:
                   xadrez[i][j] = 0
               else:
                   xadrez [i][j] = 1
           else:
               if j%2==0:
                   xadrez[i][j] = 1
               else:
                   xadrez[i][j] = 0
   return


def xadrez_bom(xadrez):
   for i in range(len(xadrez)):
       for j in range(len(xadrez[0])):
           if i%2 == j%2:
               xadrez [i][j] = 0
           else:
               xadrez [i][j] = 1
   return


#plotar_matriz(xadrez)


matri = cria_matriz(10,10)
for i in range(len(matri)):
   for j in range(len(matri[0])):
       if j>i:
           matri[i][j] = 1
       elif j ==i:
           matri[i][j] = 2
plotar_matriz(matri)




#Matriz Transposta: matriz[i][j] <-> matriz [j][i]


'''#Aux
a = 2
b = 3


a = b
b = a


print(a,b)


a = 2
b = 3


aux = a
a = b
b = aux


print(a,b)'''




def superior_ruim(matriz):
   for i in range(len(matriz)):
       for j in range(len(matriz[0])):
           if j>i:
               matriz[i][j] = 1
   return


def superior_bom(matriz):
   for i in range(len(matriz)):
       for j in range(i+1,len(matriz[0])):
           matriz [i][j]= 1
   return


lista = ['t','i','a','c','e']
def inverte_lista(lista):
   ultimo = len(lista) - 1
   for i in range (len(lista)//2):
       aux = lista[i]
       lista[i] = lista[ultimo - i]
       lista[ultimo - i] = aux
       print(lista)
   return lista


def transposta_matriz_ruim(matriz):
   for i in range(len(matriz)):
       for j in range(len(matriz)):
           if j>i:
               aux = matriz[i][j]
               matriz [i][j] = matriz [j][i]
               matriz [j][i] = aux
   return


def transposta_matriz_bom(matriz):
   for i in range(len(matriz)):
       for j in range(i):
           aux = matriz[i][j]
           matriz [i][j] = matriz [j][i]
           matriz [j][i] = aux
   return






