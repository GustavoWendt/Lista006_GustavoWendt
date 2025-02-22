#EXE 002 - Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos, solicite ao usuário para digitar um nome de produto e exiba a posição dele, em seguida peça para digitar um numero entre 0 e 9 e exiba o produto da tupla.
produtos=('Iphone','Rolex','Xiome','Mcdounalds','Ford','Luiz Viton','Ferrari','Motorola','Samsung','Diesel')

nome_produto=input("Digite o nome do produto: ")
if nome_produto in produtos:
    indice= produtos.index(nome_produto)
    print("O indice do produto selecionado foi: ",indice)
else:
    print("Esse produto não está cadastrado! ")

num=int(input("Digite um número entre 0 e 9: "))
if num >=0 and num <9:
    
    print("O produto correspondente ao número digitado é:{} ".format(produtos[num]))
else:
    print("Erro número inválido! ")
print("Gustavo Wendt")