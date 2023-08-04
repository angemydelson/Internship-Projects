temperatura = int(input("Digite a temperatura: "))
if temperatura <= 48:
    print('Rare (Selada)')
elif 48 < temperatura <= 54:
    print('Medium rare (Ao ponto para o mal)')
elif 54 < temperatura <= 60:
    print('Medium (Ao ponto)')
elif 60 < temperatura <= 71:
    print ('Well done (Bem Passada)')