import random

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

words=["Bicicleta", "Computadora", "Elefante", "Guitarra", "Hamburguesa", "Internet", "Jirafa", "Lápiz", "Murciélago", "Oso", "Pelota", "Queso", "Robot", "Sándwich", "Teléfono", "Uvas", "Violín", "Xilófono", "Yate", "Zanahoria"]

def comprobador(palabra, incompleta, attempts): #Palabra = lista de la palabra comleta y incompleta es la lista de la palabra incompelta
    palabra_correcta=''
    palabra_incompleta=''
    for c in palabra:
        palabra_correcta+=c
    while attempts!=0:
        print(f'Tienes {attempts} intentos')
        intento=input('Ingresa una letra o palabra\n')
        if len(intento) > 1:
            while len(intento)!=len(palabra_correcta):
                intento=input('La palabra ingresada es de mayor o menor longitud que la que debes adivinar, intenta de nuevo\n')
        if intento == palabra_correcta:
            return print('Has ganado')
        else:
            for n,_ in enumerate(palabra):
                if intento==_:
                    incompleta[n]=intento
            palabra_incompleta=''
            for c in incompleta:
                palabra_incompleta+=c
            print(palabra_incompleta)
            if palabra_incompleta==palabra_correcta:
                return print('Has ganado')
        attempts-=1
    print(f'Has perdido, la palabra era {palabra_correcta}')

def ahorcado():
    print('¡Bienvenido al juego del ahorcado!\n')
    attempts=6
    word=normalize(random.choice(words).lower())
    lista_completa=list(word)
    lista_incompleta=list(word)
    contador=0
    hide=int(len(word)*0.6) #Cantidad máxima de letras que se pueden ocultar
    w=''
    for _ in lista_incompleta:
        while contador!=hide:
            index=random.randrange(0,len(lista_incompleta),1)

            lista_incompleta[index]='_'
            contador+=1
    for c in lista_incompleta:
        w+=c
    print('Tu palabra es:', w)
    comprobador(lista_completa, lista_incompleta, attempts)

ahorcado()