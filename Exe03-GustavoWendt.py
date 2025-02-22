#EXE 003 - Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma lista. Depois de inserir os três nomes, pergunte se deseja 
# adicionar outro. Se o fizer, permita que adicione mais nomes até responder "não". Quando ele responder "não", mostre quantas pessoas ele convidou para a festa, uma vez que o 
# usuário tenha completado sua lista de nomes, exiba a lista completa e peça que ele digite um dos nomes da lista. Exiba a posição desse nome na lista. Pergunte ao usuário se ele 
# ainda deseja que essa pessoa venha à festa. Se ele responder "não", exclua essa entrada da lista e exiba a lista novamente.
convidados=[]
contagem=0
convidados.append(input("Digite os nomes de três convidados: "))
contagem+=3
pergunta=input("Deseja convidar mais alguem?: ".lower())
while pergunta =='sim':
    convidados.append(input("Digite o nome do convidado(a): "))
    contagem+=1
    pergunta=input("Deseja convidar mais alguem?: ").lower()
print(convidados)
print("Você convidou {} pessoas!".format(contagem))
procura=input("Digite o nome da pessoa que quer procurar: ")
if procura in convidados:
    indice=convidados.index(procura)
    print("A pessoa é: ",indice)
else:
    print("Pessoa não encontrada")
remover=input("Deseja remover essa pessoa da lista de convidados?: ").lower()
if remover == 'sim':
    convidados.remove(procura)
    print("Convidado(a) removida com sucesso! ")
else:
    print("Pessoa não encomtrada! ")
print(convidados)
print("Gustavo Wendt")