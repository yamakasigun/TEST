import random
nombre_magique = random.randint(0, 100)
reponse = None
while reponse != nombre_magique :
     reponse = int(input('Devinez le nombre magique\n'))
     if reponse > nombre_magique :
         print('Veuillez entrer un entier un peu plus petit')
     elif reponse < nombre_magique :
         print('Veuillez entrer un entier un peu plus grand')
     else :
         print('CONGRATULATION YOU HAVE WON')