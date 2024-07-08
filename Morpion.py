
import random as random
import os
from presentation import *



def plate(size):

    tab = [['.','.', '.'], ['.','.', '.'], ['.','.', '.']]

    for i in range(len(tab)):
        print(tab[i])

    return tab


def play(plate):

    a = 'N'
    x =0
    y = 0
    nb_tour =9
    values =['o','x']

    while nb_tour > 0:
        sayHi()
        if nb_tour%2 == 0:

            print('Joueur 2 vous jouez les x:')
            print('Ligne = ')
            x = int(input())
            print('Colonne = ')
            y = int(input())

            if plate[x][y] in values :
                print('Case déjà occupée choisissez un autre emplacement !')
                nb_tour = nb_tour+1
            else:

                os.system('cls')
                plate[x][y] = 'x'
                for i in range(len(plate)):
                    print(plate[i])
                nb_tour = verif(plate,2, nb_tour)
            print('OK')
        else:

            plate = computer_play(plate, values, nb_tour)

            os.system('cls')
            for i in range(len(plate)):
                print(plate[i])


#            print('Joueur 1 :')
#            print('Ligne = ')
#            x = int(input())
#            print('Colonne = ')
#            y = int(input())
#
#            if plate[x][y] in values :
#                print('Case déjà occupée choisissez un autre emplacement !')
#                nb_tour = nb_tour +1
#            else:
#                clear_output(wait=True)
#                plate[x][y] = 'o'
#                for i in range(len(plate)):
#                    print(plate[i])
#                nb_tour = verif(plate,1, nb_tour)

        nb_tour = nb_tour -1

    if nb_tour != -3:
        print('Match nul !')




def verif(plate, joueur, nb_tour):
    values =['o','x']

    for i in range(len(plate)):

        if(plate[i][0] == plate [i][1] == plate[i][2] in values):
            print( 'Le joueur ', joueur,' gagne la partie ! PAR LIGNES')
            nb_tour = -2
            return nb_tour

    for j in range(len(plate)):

        if(plate[0][j] == plate [1][j] == plate[2][j]in values ):
            print( 'Le joueur ', joueur,' gagne la partie ! PAR COLONNES')
            nb_tour = -2
            return nb_tour

    if(plate[0][0] == plate [1][1] == plate[2][2] in values or plate[0][2] == plate [1][1] == plate[2][0] in values):
        print( 'Le joueur ', joueur,' gagne la partie ! PAR DIAGONALE')
        nb_tour = -2
        return nb_tour



    return nb_tour


def jouer_coin( game, values):

    x = random.choice([0,2])
    y = random.choice([0,2])

    while game[x][y] in values:

        x = random.choice([0,2])
        y = random.choice([0,2])

    game[x][y] = 'o'

    return game


def computer_play(game, values, nb_coup):

    if nb_coup >7 :
        game = jouer_coin(game, values)
        return game

    x = random.randint(0,2)
    y = random.randint(0,2)

    while game[x][y] in values:

        x = random.randint(0,2)
        y = random.randint(0,2)

    game[x][y] = 'o'

    return game


TAB = plate(3)
play(TAB)
print('End')
