ligne = int(input("Veuillez saisir la taille de l'étoile: "))            #input le nbr de lignes
col = ligne * 2 - 5                                                      #nombre de colonne 
mid = col//2                                                             #Colonne du milieux


for i in range(0, ligne):                                                #boucle for lignes
    for j in range(0, col):                                              #boucle for Colonnes
        if i == 2 or i == (ligne -3) or i+j == mid or j-i == mid or i-j == 2 or i+j == col+1:
            print("*", end="")                                           #Affichage étoile
        else:
            print(" ", end="")                                           #Affichage vide
    
    
    print()                                                             