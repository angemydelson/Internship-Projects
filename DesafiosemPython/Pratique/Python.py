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


# classe em pyhton

# class Funcionarios:
#     nome = "Angemy"
#     sobrenome = "Delson"


# usuario1 = Funcionarios()
# print(usuario1.nome)
# print(usuario1.sobrenome)

# class Funcionarios:
#    pass



# usuario1 = Funcionarios()
# usuario2 = Funcionarios()

# usuario1.nome = 'Angemy'
# usuario1.datansc = 'Delson'
# usuario2.nome = 'Delva'
# usuario2.datanas = 'Saint bert'
# print(usuario1.nome)
# print(usuario1.datansc)

# class Funcionarios:
#     def __init__(self, nome, sobrenome, datanasc):
#       self.nome = nome
#       self.sobrenome = sobrenome
#       self.datanasc = datanasc

#     def nome_completo(self):
#       return self.nome + " " + self.sobrenome


# usuario1 = Funcionarios("Angemy", "Saint Bert", "10/11/2000")
# usuario2 = Funcionarios("Delva", "Saint Bert", "10/23/1972")



# # print(usuario1.nome)
# # print(usuario2.nome)

# print(usuario1.nome_completo())
# print(Funcionarios.nome_completo(usuario1))

# from datetime import datetime
# class Funcionarios:
#     def __init__(self, nome, sobrenome, anonasc):
#       self.nome = nome
#       self.sobrenome = sobrenome
#       self.anonasc = anonasc

#     def nome_completo(self):
#       return self.nome + " " + self.sobrenome
    
#     def idade_funcionario(self):
#        ano_atual = datetime.now().year
#        self.anonasc = int(ano_atual - self.anonasc)
#        return self.anonasc
       


# usuario1 = Funcionarios("Angemy", "Saint Bert", 2000)
# usuario2 = Funcionarios("Delva", "Saint Bert", 1972)



# # print(usuario1.nome)
# # print(usuario2.nome)

# print(usuario1.nome_completo())
# print(Funcionarios.nome_completo(usuario1))
# print(Funcionarios.idade_funcionario(usuario1))
