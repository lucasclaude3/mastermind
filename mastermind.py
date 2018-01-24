#!/usr/bin/env python
# coding: utf-8

import numpy as np

class Game:
    def __init__(self):
        self.couleurs = ['R', 'J', 'B', 'O', 'V', 'N']
        self.nombre_essais = 1
        self.board = []
        print('Bienvenue dans mon petit jeu de Mastermind !')
        print('J\'espere que tu vas t\'enjailler en tentant de résoudre mes énigmes hihihi !')
        raw_input('\nAppuie sur entrer pour continuer !')

        self.combinaison = [self.couleurs[np.random.randint(len(self.couleurs))] for j in range(4)]
        self.couleurs_count = {i: self.combinaison.count(i) for i in self.couleurs}

        print('\nJ\'ai choisi 4 pions en piochant parmi les couleurs suivantes : ' + ', '.join(self.couleurs))
        print('Il peut y avoir autant de pions d\'une meme couleur que possible !')
        print('\nTu as 10 essais pour trouver la bonne combinaison.')
        print('A chaque essai je te dirai le nombre de pions bien placés et le nombre de pions dont la couleur figure dans ma combinaison mais mal placés.')
        print('Sauras tu trouver la bonne combinaison à temps grâce à ces indices ??\n')
        raw_input('Appuie sur entrer pour continuer.')

        print('Allez c\'est parti, donne moi une séquence de 4 couleurs sous la forme R J B O :')
        self.one_turn()

    def one_turn(self):
        trial_list_valid = False
        while not trial_list_valid:
            trial = raw_input()
            trial_list = trial.split(' ')
            trial_list_valid = len(trial_list) == 4 and sum([i in self.couleurs for i in trial_list]) == 4
            if not trial_list_valid:
                print('Tu n\'as pas respecté le format que je t\'avais demandé ! Recommence :')

        raw_input('Ok, c\'est au bon format. Voyons maintenant si tu as vu juste...')
        parfaits, mal_places = self.check_trial(trial_list)
        self.board.append(trial_list + [parfaits, mal_places])
        if parfaits == 4:
            print('\nBravo, c\'est la bonne combinaison, TU AS GAGNE !!')
        elif parfaits < 4 and self.nombre_essais == 10:
            print('\nTu n\'as pas trouvé en 10 coups, c\'est perdu. Dommage...')
            print('Peut être n\'as tu pas l\'étoffe d\'un MASTERMIND...')
            print('La bonne combinaison était ' + ' '.join(self.combinaison))
        elif parfaits < 4 and self.nombre_essais < 10:
            print('Raté ! Mais tu en as parfaitement placé ' + str(parfaits) + ', et ' + str(mal_places) + ' autres sont dans la combinaison mais à un autre endroit.')
            raw_input('Allez, encore un essai ! Appuie pour continuer')
            self.print_board()
            print('\nEntre à nouveau 4 couleurs sous la forme R J B O :')
            self.nombre_essais += 1
            self.one_turn()

    def print_board(self):
        print('Voila où on en est :\n')
        for i, t in enumerate(self.board):
            print('tour ' + str(i+1) + ' / 10 | ' + t[0] + ' ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' | ' + str(t[4]) + ' bien placés et ' + str(t[5]) + ' mal placés' )

    def check_trial(self, trial_list):
        tampon_couleurs_count = self.couleurs_count.copy()
        parfaits = 0
        mal_places = 0
        deja_places = []
        for j in range(len(trial_list)):
            if trial_list[j] == self.combinaison[j] and tampon_couleurs_count[trial_list[j]] > 0:
                deja_places.append(j)
                parfaits += 1
                tampon_couleurs_count[trial_list[j]] -= 1
        for j in range(len(trial_list)):
            # besoin d'un second passage pour les mal places
            # on ne peut pas le faire en meme temps que les parfaits,
            # sinon on risque de se tromper a cause de l'ordre de passage
            if j in deja_places: # pour eviter de recompter les pions deja places
                continue
            if trial_list[j] in self.combinaison and tampon_couleurs_count[trial_list[j]] > 0:
                mal_places += 1
                tampon_couleurs_count[trial_list[j]] -= 1
        return parfaits, mal_places

x = Game()




