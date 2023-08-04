import math
altura = float(input("Qual é a sua altura em cm? ")) / 100
peso = float(input("Qual é o seu peso em kg? "))

imc = peso / pow(altura, 2)
print(imc)
if  imc < 18.5:
    print("Magreza")
elif 18.5 < imc <= 24.9:
    print("Normal")
elif 24.9 < imc <= 29.9:
    print('Sobrepeso')
elif 29.9 < imc <= 39.9:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Grave')