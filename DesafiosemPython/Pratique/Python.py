# nome = input("Qual eh o seu nome: ")
# idade = input("Qual eh a sua idade: ")
# cidade = input('Qual eh a sua cidade: ')
# print('O ' + nome + " tem " + str(idade) + ' anos de idade e mora em ' + cidade + '.')

# ano_nascimento = input('Em que ano vc naceu? ')
# print(type(ano_nascimento))
# idade = 2023 - int(ano_nascimento)
# print(type(idade))
# print(idade)

# printar = 'Eu adoro comida caseira'
# print(printar.lower())
# printars = 'Eu adoro comida caseira'
# print(printars.upper())
# printars = 'Eu adoro comida caseira'
# print(printars.capitalize())
# printars = 'Eu adoro comida caseira'
# print(printars.find('c'))
# printars = 'Eu adoro comida caseira'
# print(printars.replace('a', 'e'))
# printars = '      Eu adoro comida caseira'
# print(printars.strip())

# for letra in 'Google':
#     print(letra)

# linha = 10
# coluna = 10
# simbolo = '$'
# for i in range(linha):
#     for j in range(coluna):
#         print(simbolo, end='')
#     print()

#lista
# cidades = []
# cidades.append('Santa Catarina')
# cidades.insert(1, 'Goais')
# print(cidades)
# cidades.sort()
# print(cidades)

# produtos = ['arroz', 'feijão', 'laranja', 'banana']

# # Tuple
# produtos_list = ['arroz', 'feijão', 'laranja', 'banana']
# produtos_tuple = ('arroz', 'feijão', 'laranja', 'banana')

# print(type(produtos_list))
# print(type(produtos_tuple))

#Array

# criando Set

# list1 = [10, 30, 40, 80, 80, 50, 30]
# list2 = [10, 30, 40, 80, 80, 50]
# num1 = set(list1)
# num2 = set(list2)

# # print(num1)
# # print(num2)

# print(num1 | num2) # union
# print(num1 - num2) # difference
# print(num1 ^ num2) # symmetric difference
# print(num1 & num2)
# print(len(num1))

# Dicionario

# aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovado': True}
# print(aluno)
# print(aluno['idade'])
# print(aluno.get('endedf'))

# for keys, values in aluno.items():
#     print(keys, values)

# Função Lambda

# def somar(x):
#     return x + 10
# print(somar(2))

# somar10 = lambda x: x + 10
# print(somar(2))

# somar10 = lambda x,y: x + y + 10
# print(somar10(2,3))

# def somar(x):
#     return x * 4

# print(somar(2))

# def somar(x):
#     func2 = lambda y: y + 4
#     return  func2(4) * 4 

# print(somar(2))


# Map

# lista1 = [1, 2, 3, 4]

# def multi(x):
#     return x * 2

# lista3 = map(multi, lista1)
# print(list(lista3))


# # lista2 = map(lambda x: x *2, lista1)
# print(list(map(lambda x: x *2, lista1)))

# print(list(filter(lambda x: x > 2, lista1)))

# list comprension

# frutas1 = ['abcate', 'banana', 'morango', 'kiwi', 'abacaixi']

# frutas2 = [iten for iten in frutas1 if 'n' in iten]
# print(frutas2)

# from sys import getsizeof

# valores = [ x * 10 for x in range(10)]
# print(type(valores))
# print(valores)
# print(getsizeof(valores))

# valores = ( x * 10 for x in range(10))
# print(type(valores))
# print(list(valores))
# print(getsizeof(valores))

# Erros

# try:
#     letras = ['a', 'b', 'c']
#     print(letras[3])
# except IndexError:
#     print('Index não existe')

# try:
#     Valor = int(input("Digite um valor: "))
#     print(Valor)
# except ValueError:
#     print('Favor digitar um valor em numero')
# finally:
#     print('Pedaço de codigo ok')

# else:
#     print('Valor Correto')
#     resul = Valor *231412
#     print(resul)

# print('Mais codigo abaixo')

# frutas = ["maçã", "morango", "uva"]
# for i in frutas:
#     print(f"Eu gosto de {i}")
# for i in range(1,11):
#     print(i)

# frutas = ["maçã", "morango", "uva", "maçã", "maçã"]
# cont = 0
# for i in frutas:
#     if (i == 'maçã'):
#         cont += 1
# print(cont)

# carro = ["BMW X6", "BMW I5", "BMW I8"]
# inputUser = str(input("Digite o nome do carro: "))
# inputUser = inputUser.lower()
# aux = 0
# for i in carro:
#     if i.lower() == inputUser:
#         aux = 1
# if aux == 1:
#     print("Este carro está disponível")
# else :
#     print("Este carro não está dispnivel. Infelizmente!")

# carro = ("BMW X6", "BMW I5", "BMW I8")
# i = input()
# if i.upper in carro:
#     print('sim')
# else :
#     print('Não')

# carro = {
#     'Brasil' : 'Brasilia',
#     'Haiti' : 'Porto Principe',
#     'Peru' : 'Lima',
#     'Canada' : 'Ottawa'
# }

# pais = str(input("Digite uma pais: "))

# if pais in carro:
#     print(carro[pais])

# n = int(input())

# def fatorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * fatorial(n-1)

# print(fatorial(n))
# import math
# x = int(input())
# cubo = lambda x: pow(x,3) 
# print(cubo(x))

# doinum = lambda x, y: x * y
# x = int(input())
# y = int(input())
# print(doinum(x,y))
# num = [1, 2, 3, 4, 5, 56]
# resultado = []
# quadrado = lambda x: x**2
# x = int(input())

