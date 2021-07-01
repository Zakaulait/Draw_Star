import turtle
from turtle import *

taille_etoile = int(input ("Entrez la taille de l'étoile:  "))
unite_graphique= 25
right(36)


def Draw_Star():
    if  taille_etoile == 0:
        print ("veuillez entrez une valeur supérieure à 0.")
        exit()
        
    for k in range(5):
        forward( taille_etoile * unite_graphique )
        left(144)
    
    
    
Draw_Star()
exitonclick()