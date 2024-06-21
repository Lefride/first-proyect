meme_dict = {'XD': 'Se usa cuando algo es gracioso',
             'POSSER': 'Fan por moda',
             'CHAMBA': 'Trabajar',
             'FANBOY': 'Fan ciego'}

for i in range(5):
    
    word = input('Que palabra quieres entender?').upper()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('Aun faltan agregar elementos al diccionario')
