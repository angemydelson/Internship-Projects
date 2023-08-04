# Criar um programa que calcula a quantidade de tinta necessária para
# pintar uma parede. O usuário deverá fornecer as seguintes
# informações: Rendimento, altura e largura.
# O programa deve mostrar na tela 'VoÇẽ precisa de x latas de tinta' 

rendimento = int(input("Qual é o rendimento da lata? "))
altura = float(input("Qual é a altura da parede? "))
largura = float(input("Qual é a largura da parede? "))

def calculo_tinta(rendimento, altura, largura):
    surfaceParede = altura * largura
    quantidadeTintas = surfaceParede / rendimento
    print(f"Voçê precisa de {quantidadeTintas} lata de tinta.")

calculo_tinta(rendimento, altura, largura)