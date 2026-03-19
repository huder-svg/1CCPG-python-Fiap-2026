print('ola mundo')
print(7+4)
print("7"+"4") #concatenando strings

#comentario de 1 linha
'''
    cometarios de 
    múltiplas 
    linhas 

'''
#VÁRIAVEIS

nome = "Alexandre" #str
idade = 26 #int
peso = 70.2 #float
print("nome \n", nome, idade, peso) #barra n pula linha
print(f"Olá, {nome}!!!")
#input -- simulação de forms no cmd
nome = input("Digite o seu nome: ")
idade = int(input("Digite o seu nome: "))
peso = float(input("digite o seu peso: "))

print(nome, idade, peso)
print(idade + 1)

ano_nascimento =  1999
ano_atual = 2026

idade = ano_nascimento - ano_atual

print(f"sua idade é: {idade}") #quando for colocar a variavel em uma string é necessario colocar o f para informar a variavel