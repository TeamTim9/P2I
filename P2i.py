##Bibli
from itertools import product
import random
##Définition plateau et piece
def init_plateau ():
    plateau = [[None]*4 for k in range(4)]
    for k in range (4):
        for n in range (4):
            plateau[n][k]=[0,0,0,0]
    return plateau



def creer_piece():
    valeurs_possibles = [1, 2]
    toutes_combinaisons = list(product(valeurs_possibles, repeat=4))
    tableaux = [list(combinaison) for combinaison in toutes_combinaisons]
    return tableaux

def afficher_plateau(plateau, piece=[]):
    for n in range (4):
        print(plateau[n][0],plateau[n][1],plateau[n][2],plateau[n][3])
    n=0
    if not (plateau==[]):
        while(n<(int(len(piece)))):
            a=0
            while (a<4 and n<(int(len(piece)))):
                print(piece[n],end='')
                a+=1
                n+=1
            print()
    return


Pieces=creer_piece()
print (len(Pieces))
print(Pieces[15])
print(Pieces[0])
plateau=init_plateau()
afficher_plateau(plateau, Pieces)

##Initialiser plateau
Pieces=creer_piece()
plateau=init_plateau()

##Fonction de placement

#print(len(plateau))
def placer_pions(plateau, pion,coordonnees,Pieces):
    stop=0
    if (plateau[coordonnees[0]-1][coordonnees[1]-1] == [0, 0, 0, 0]) and stop==0 :
        plateau[coordonnees[0]-1][coordonnees[1]-1]=pion
    else:
        print ("case déja occupé")
        stop=1
    if not pion in Pieces and stop==0 :
        if not (pion in Pieces):
            print("pion déja en jeu")
        plateau[coordonnees[0]-1][coordonnees[1]-1] = [0, 0, 0, 0]
    else:
        Pieces.remove(pion)
    return



placer_pions(plateau,[1,1,2,1], [1,4],Pieces)

afficher_plateau(plateau, Pieces)

##Verification de victoire



def victoire (plateau):    #pas de vertical pour l'instant
    for i in range (4):
        count1=0
        count2=0
        for k in range (4):
            if (count1==k):
                if (plateau[i][k] != [0,0,0,0]):
                    count1+=1
            if (count2==k):
                if (plateau[k][i] != [0,0,0,0]):
                    count2+=1
        if (count2==4):
            print ("4 pieces alignéz en vertical")
        if (count1==4):
            print ("4 pieces alignér à l'horizontal")
    return

def victoiretour (plateau, coordonnee,pion):   #pas de vertical pour l'instant
    test1=0
    test2=0
    test3=0
    test4=0
    testf=0
    for k in range (4):
        if (test1==k):
            if (plateau[coordonnee[0]][k][0]==pion[0]):
                test1+=1
        if (test2==k):
            if (plateau[coordonnee[0]][k][1]==pion[1]):
                test2+=1
        if (test3==k):
            if (plateau[coordonnee[0]][k][2]==pion[2]):
                test3+=1
        if (test4==k):
            if (plateau[coordonnee[0]][k][3]==pion[3]):
                test4+=1
    if (test1==4 or test2==4 or test3==4 or test4==4):
        testf=1
    if not (testf==1):
        test1=0
        test2=0
        test3=0
        test4=0
        for k in range (4):
            if (test1==k):
                if (plateau[k][coordonnee[1]][0]==pion[0]):
                    test1+=1
            if (test2==k):
                if (plateau[k][coordonnee[1]][1]==pion[1]):
                    test2+=1
            if (test3==k):
                if (plateau[k][coordonnee[1]][2]==pion[2]):
                    test3+=1
            if (test4==k):
                if (plateau[k][coordonnee[1]][3]==pion[3]):
                    test4+=1
    if (test1==4 or test2==4 or test3==4 or test4==4):
        testf=1
    if not (testf==1):
        test1=0
        test2=0
        test3=0
        test4=0
        if (coordonnee[1]==coordonnee[0]):
            for k in range (4):
                if (test1==k):
                    if (plateau[k][k][0]==pion[0]):
                        test1+=1
                if (test2==k):
                    if (plateau[k][k][1]==pion[0]):
                        test2+=1
                if (test3==k):
                    if (plateau[k][k][2]==pion[0]):
                        test3+=1
                if (test4==k):
                    if (plateau[k][k][3]==pion[0]):
                        test4+=1
        if (coordonnee[1]+coordonnee[0]==3):
            for k in range (4):
                if (test1==k):
                    if (plateau[k][3-k][0]==pion[0]):
                        test1+=1
                if (test2==k):
                    if (plateau[k][3-k][1]==pion[0]):
                        test2+=1
                if (test3==k):
                    if (plateau[k][3-k][2]==pion[0]):
                        test3+=1
                if (test4==k):
                    if (plateau[k][3-k][3]==pion[0]):
                        test4+=1
    if (test1==4 or test2==4 or test3==4 or test4==4):
        testf=1
    if (testf==1):
        print ("Victoire !!")
        return True
    else :
        print ("Continuez à jouer")
        return False

    return

##Don de pion

def Choix_Pion(Pieces):
    while True:
        print("Choisissez une piece :")
        for index, element in enumerate(Pieces, start=1):
            print(f"{index}. {element}")

        try:
            choix = int(input("Votre choix (entrez le numéro de l'élément) : "))
            if 1 <= choix <= len(Pieces):
                return Pieces[choix - 1]
            else:
                print("Veuillez entrer un numéro valide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")


##Fonction Systeme Expert
def Choix_Pion_SE(pieces,plateau):
    pion=random.choice(pieces)
    return pion

def Placer_Pion_SE(plateau,pion):
    cases_vides = [(i, j) for i, ligne in enumerate(plateau) for j, colonne in enumerate(ligne) if colonne == [0, 0, 0, 0]]


    if cases_vides:
        coordonnees = random.choice(cases_vides)
        ligne, colonne = coordonnees
        return [ligne+1, colonne+1]
    else:
        print("Aucune case vide disponible.")
        return None

##Jeu en 1V1
def jeu_quarto():
    plateau = init_plateau()
    pieces = creer_piece()
    Fin=0

    joueur_actuel = 1
    print("\nJoueur {joueur_actuel}, selectionnez une piece à donner a votre adversaire :")
    piece_selectionnee = Choix_Pion(pieces)
    joueur_actuel = 2

    while (Fin==0):
        afficher_plateau(plateau,pieces)
        print(f"\nJoueur {joueur_actuel}, voici votre pièce : {piece_selectionnee}")
        coord_x = int(input("Entrez la ligne (1-4) où vous voulez placer la pièce : "))
        coord_y = int(input("Entrez la colonne (1-4) où vous voulez placer la pièce : "))

        placer_pions(plateau, piece_selectionnee, [coord_x, coord_y],pieces)

        if victoiretour(plateau, [coord_x-1, coord_y-1], piece_selectionnee):
            afficher_plateau(plateau)
            print(f"\nLe Joueur {joueur_actuel} a gagné !")
            Fin=1
        else:
            print(f"\nJoueur {joueur_actuel}, selectionnez une piece à donner a votre adversaire : {piece_selectionnee}")
            piece_selectionnee = Choix_Pion(pieces)
        joueur_actuel = 3 - joueur_actuel

##Jeu SE

def jeu_quarto_SE(plateau,pieces,joueur_actuel):
    Fin=0

    if (joueur_actuel==0):
        piece_selectionnee = Choix_Pion_SE(pieces,plateau)
        joueur_actuel = 1
    else:
        print(f"\nJoueur {joueur_actuel}, selectionnez une piece à donner a votre adversaire :")
        piece_selectionnee = Choix_Pion(pieces)
        joueur_actuel = 0

    while (Fin==0):
        afficher_plateau(plateau,pieces)
        if (joueur_actuel==0):
            coordonnees=Placer_Pion_SE(plateau, piece_selectionnee)
            placer_pions(plateau, piece_selectionnee, coordonnees,pieces)
            coord_x=coordonnees[0]
            coord_y=coordonnees[1]
            print(f"Le SE a choisit les coordonnees: {coord_x},{coord_y}")
            if victoiretour(plateau, [coord_x-1, coord_y-1],piece_selectionnee):
                afficher_plateau(plateau,pieces)
                print(f"\nLe Joueur {joueur_actuel} a gagné !")
                Fin = 1
            else:
                piece_selectionnee = Choix_Pion_SE(pieces,plateau)
                joueur_actuel = 1

        else:
            print(f"\nJoueur {joueur_actuel}, voici votre pièce : {piece_selectionnee}")
            coord_x = int(input("Entrez la ligne (1-4) où vous voulez placer la pièce : "))
            coord_y = int(input("Entrez la colonne (1-4) où vous voulez placer la pièce : "))

            placer_pions(plateau, piece_selectionnee, [coord_x, coord_y],pieces)

            if victoiretour(plateau, [coord_x-1, coord_y-1], piece_selectionnee):
                afficher_plateau(plateau,pieces)
                print(f"\nLe Joueur {joueur_actuel} a gagné !")
                Fin = 1
            else:
                print(f"\nJoueur {joueur_actuel}, selectionnez une piece à donner a votre adversaire :")
                piece_selectionnee = Choix_Pion(pieces)
                joueur_actuel = 0
        afficher_plateau(plateau,pieces)


##Essai chat


def Placer_Pion_SE(plateau, pion):
    cases_vides = [(i, j) for i, ligne in enumerate(plateau) for j, colonne in enumerate(ligne) if colonne == [0, 0, 0, 0]]


    if cases_vides:
        coordonnees = random.choice(cases_vides)
        ligne, colonne = coordonnees
        return [ligne+1, colonne+1]
    else:
        print("Aucune case vide disponible.")
        return None

# Exemple d'utilisation
mon_plateau = [
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 2, 1]],
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    [[0, 0, 0, 0], [1, 1, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0]]
]

pion_a_placer = [2, 1, 2, 2]

# Appel de la fonction avec le plateau et le pion
coordonnees_assignees = Placer_Pion_SE(mon_plateau, pion_a_placer)
print(f"Pion placé sur le plateau aux coordonnées : {coordonnees_assignees}")

##Création environnement
##Victoire ou non défaite en un coup
#[1,2,1,2] et [2,1,1,1], par exemple, donnent la victoire en [3,1]
Environnement11 = [[[1, 1, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[1, 1, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

#[1,2,1,2] et [2,1,1,1], par exemple, donnent la victoire en [1,4]
Environnement12 = [[[1, 1, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

#[2,1,1,1] et [1,2,2,2] par exemple, donnent la victoire en [3,3]
Environnement13 = [[[1, 1, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 2, 1]]]

#[1,2,1,2] et [2,1,1,1], par exemple, donnent la victoire en [3,1]
Environnement21 = [[[1, 1, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 2, 2]], [[1, 1, 2, 1], [0, 0, 0, 0], [2, 2, 1, 1], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 2], [1, 2, 1, 1]]]

#[1,2,1,2], par exemple, donne la victoire en [1,4]
Environnement22 = [[[1, 2, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 1, 1], [0, 0, 0, 0]], [[0, 0, 0, 0], [1, 2, 2, 2], [2, 2, 2, 2], [2, 1, 1, 2]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 1, 1]]]

#[2,1,1,1], par exemple, donne la victoire en [3,3]
Environnement23 = [[[2, 1, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 1, 2]], [[0, 0, 0, 0], [1, 1, 1, 1], [1, 2, 1, 1], [2, 2, 2, 2]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[2, 1, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 2, 1]]]

##Victoire ou non défaite en 2 coup pas sur
#dans l'ordre: 1= petit, jaune, rond, plein

#Solution: Donner [2,1,1,1]
Environnement31 = [[[0, 0, 0, 0], [2, 2, 2, 1], [0, 0, 0, 0], [1, 2, 2, 1]], [[1, 1, 2, 1], [1, 1, 1, 1], [1, 2, 1, 2], [2, 2, 1, 1]], [[2, 1, 2, 2], [1, 1, 2, 2], [1, 2, 1, 1], [2, 1, 1, 2]], [[0, 0, 0, 0], [2, 1, 2, 1], [0, 0, 0, 0], [2, 2, 2, 2]]]
Pieces31 = [[2,1,1,1],[2,2,1,2],[1,1,1,2],[1,2,2,2]]

##Victoire en 2 coup simple
#dans l'ordre: 1= petit, uni, triangle, plein

Environnement32 = [[[2, 1, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                  [[1, 1, 2, 1], [1, 2, 2, 1], [1, 2, 1, 2], [2, 1, 1, 1]],
                  [[2, 1, 2, 1], [2, 1, 1, 2], [1, 1, 2, 2], [1, 2, 1, 1]],
                  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
Pieces32= [[1,1,1,1],[1,1,1,2],[1,2,2,2],[2,2,2,2],[2,2,2,1],[2,2,1,2],[2,2,1,1]]

#Scénario: On donne la pieces [2,2,1,2] à jouer au SE, il doit le placer en [1,2]/[1,3]/[4,2]/[4,3] et donner la piece [2,2,1,1]. Victoir à son prochain tour.

##Victoire
Environnement41 =[[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 1, 1]],
                 [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 2, 1], [1, 2, 1, 2]],
                 [[1, 1, 2, 1], [2, 2, 2, 2], [2, 1, 2, 2], [2, 1, 1, 1]],
                 [[2, 1, 2, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
Pieces41= [[2,2,1,2],[2,1,1,2],[2,2,1,1],[1,1,1,2],[1,1,1,1],[1,1,2,2],[1,2,2,2],[1,2,2,1]]

#Scénario: On donne la piece [1,2,2,1] à placer au SE, il la place en [2,2] et donne la piece [1,1,2,2]. On place ensuite cette piece au seul endroit qui ne fais pas automatiquement perdre:[4,4] et on donne une pieces qui ne fais pas automatiquement perdre au SE: [2,1,1,2]/[1,1,1,2]/[1,1,1,1]. Il place cette piece en [1,3] et donne un des deux restant parmis [2,1,1,2]/[1,1,1,2]/[1,1,1,1]. Victoire au prochain tour.

## Fonction Environnement
def Verif_Doublons(lst):
    ensembles_tuples = set(tuple(subliste) for subliste in lst)

    return len(ensembles_tuples) == len(lst)

def memes_elements(liste1, liste2):
    # Convertir chaque liste interne en ensemble de tuples
    ensemble1 = set(tuple(subliste) for subliste in liste1)
    ensemble2 = set(tuple(subliste) for subliste in liste2)

    # Vérifier si les ensembles sont égaux
    return ensemble1 == ensemble2

def pieces_manquantes(liste1, liste2):
    # Convertir chaque liste interne en ensemble de tuples
    ensemble1 = set(tuple(subliste) for subliste in liste1)
    ensemble2 = set(tuple(subliste) for subliste in liste2)

    # Trouver les éléments manquants dans chaque liste
    manquants_liste1 = ensemble2 - ensemble1
    manquants_liste2 = ensemble1 - ensemble2

    # Afficher les éléments manquants
    if manquants_liste1:
        print("Il manque les éléments", manquants_liste1, "dans la liste 1.")
    if manquants_liste2:
        print("Il manque les éléments", manquants_liste2, "dans la liste 2.")
    return not (manquants_liste1 or manquants_liste2)



def Verif_Complet (pieces,Environnement=[]):
    TotPieces = creer_piece()
    verif=[]
    if not (Environnement==[]):
        for n in range (4):
            for k in Environnement[n]:
                if not (k ==[0,0,0,0]):
                    for l in TotPieces:
                        if (l==k):
                            verif.append(l)
    for k in pieces:
        if not (k==[0,0,0,0]):
            for l in TotPieces:
                if (l==k):
                    verif.append(l)
    if (Verif_Doublons(verif)):
        test=creer_piece()
        if (pieces_manquantes(verif, test)):
            print ("envirronement valide")
        else:
            print ("manque de pieces")
    else :
        print ("pieces en double")
    return

