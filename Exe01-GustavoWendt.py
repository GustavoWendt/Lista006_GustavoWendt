#EXE 001 . - Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.
paises=('Brasil','Turcomenistão','China','Mexico','Alemanha')
print(paises)
escolha=input("Escolha um país: ")
if escolha in paises:
  indice = paises.index(escolha)
  print("O indice do pais é :",indice)
else:
  print("País inválido!")

print("Gustavo Wendt")