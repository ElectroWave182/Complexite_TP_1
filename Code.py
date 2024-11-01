def indiceMax (tableau, indiceFin):

    # Calculons l'indice du maximum absolu restant
    indiceMax = 0
    for indice in range (indiceFin):
        
        entier = tableau[indice]
        entierMax = tableau[indiceMax]
        
        if abs (entier) > abs (entierMax):
            indiceMax = indice
    
    return indiceMax


def retourner (tableau, indiceFin):
    
    # Nous retournons la pile et prenons les opposés
    tableau[: indiceFin] = list (map (lambda x: -x, tableau[: indiceFin]))
    tableau[: indiceFin] = reversed (tableau[: indiceFin])


def rangerRec (tableau, indiceFin):

    taille = len (tableau)

    # Cas récursif
    if indiceFin != 0:
    
        indice = indiceMax (tableau, indiceFin)
    
        if tableau[indice] < 0:
            retourner (tableau, indiceFin)
            
        indice = indiceMax (tableau, indiceFin)

        retourner (tableau, indice + 1)
        retourner (tableau, indiceFin)
        
        # Appel
        rangerRec (tableau, indiceFin - 1)


def ranger (tableau):

    rangerRec (tableau, len (tableau))


# Tests
def main ():

    tableau = [-1]
    print (tableau)
    ranger (tableau)
    print (tableau)
    print ()

    tableau = [4, -6, 7, -2, 1, 5, -3]
    print (tableau)
    ranger (tableau)
    print (tableau)
    print ()


main ()