from palavra import palavras

letras_usuario=[]
chances=3
ganhou=False

#Apresentação
print('\n\t\t\t ... Jogo da forca nomes,doce,fruta,animal ou carboigratos...\n\n')
while True:
    for letra in palavras:
         if letra.lower() in letras_usuario:
                print(letra, end = " ")
         else:
                print("_",end= " ")

    print(f'Voce tem {chances} chances!')

    tentativas=input('Escolha uma letra:')
    letras_usuario.append(tentativas.lower())
    if tentativas not  in palavras :
        chances -= 1
    ganhou=True

    for letra in palavras:
        if letra.lower() not in letras_usuario:
            ganhou=False
    if chances == 0 or ganhou:
            break
    if ganhou:
        # encerra o jogo
        print(f'Parabens!Você ganhlou,a palavra é {palavras}')
    else:
    #encerra o jogo
        print(f'Você perdeu!,a palavra era {palavras}')



