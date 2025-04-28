#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ArbreBin.py
#
#  Copyright 2020 andre <andre@andre-OptiPlex-740-Enhanced>
"""Module d'arbre binaire"""
from collections import deque
from tkinter import *


class ArbreBin:
    def __init__(self, eti=None, fg=None, fd=None):
        """Constructeur"""
        self.Et = eti
        self.Fg = fg
        self.Fd = fd
        self.x = 0
        self.y = 0

    def estFeuille(self):
        return self.Fg == None and self.Fd == None

    def creer_table(self, chaine=""):
        """Retourne un dictionnaire qui associe les etiquettes à leur code binaire."""
        dic = {}
        if self.estFeuille():
            dic[self.Et] = chaine
        if self.Fg != None:
            new_chaine = chaine + "0"
            result = self.Fg.creer_table(new_chaine)
            for i in result:
                dic[i] = result[i]

        if self.Fd != None:
            new_chaine = chaine + "1"
            result = self.Fd.creer_table(new_chaine)
            for i in result:
                dic[i] = result[i]
        return dic

    def nbNoeud(self):
        if self.estVide():
            return 0
        elif self.estFeuille():
            return 1  # cas de la feuille
        elif self.Fg == None:
            return 1 + self.Fd.nbNoeud()
        elif self.Fd == None:
            return 1 + self.Fg.nbNoeud()
        else:
            return 1 + self.Fg.nbNoeud() + self.Fd.nbNoeud()

    def estVide(self):
        """Methode testant si un arbre binaire est vide"""
        return self.Et == None and self.Fg == None and self.Fd == None

    ###################GRAPHISME########################################
    def fixeXY(self, Xpere=0, Ypere=-1, sens=True):
        # attribue les coordonnées des noeuds de l arbre.(nombres entiers)
        # xracine fixé à 0
        # sens True : c'est un fils droit
        if self != None:  # il y a au moins une feuille
            if sens:  # ce noeud est un fils droit
                if self.Fg != None:
                    enPlus = self.Fg.nbNoeud()
                else:
                    enPlus = 0
                self.x = Xpere + 1 + enPlus
            else:  # ce noeud est un fils gauche
                if self.Fd != None:
                    enPlus = self.Fd.nbNoeud()
                else:
                    enPlus = 0
                self.x = Xpere - (1 + enPlus)
            self.y = Ypere + 1
            if self.Fd != None:
                self.Fd.fixeXY(self.x, self.y, True)
            if self.Fg != None:
                self.Fg.fixeXY(self.x, self.y, False)

    def joliDessin(self):
        pasX = 50
        pasY = 50
        # methode appelee sur la racine
        f = Tk()
        f.title("un arbre")
        # calculer la taille fenêtre : dépend hauteur et nbre de noeuds
        Flarg = (self.nbNoeud() + 1) * pasX
        Fhaut = (self.hauteur() + 2) * pasY
        taille = str(Flarg) + "x" + str(Fhaut)
        # implique incrément hauteur et largeur. max fenêtre 1000X1000
        f.geometry(taille)
        can1 = Canvas(f, bg="darkgrey", width=Flarg - 10, height=Fhaut - 10)
        can1.grid(padx=5, pady=5)
        self.fixeXY()
        self.AfficheArbre(can1)
        mainloop()

    def AfficheArbre(self, lecanva):
        """parcours en profondeur et affiche l'arbre"""
        pasX = 50
        pasY = 50
        rayon = 16
        if self.filsDroit():
            # trace la branche droite
            lecanva.create_line(
                (self.x) * pasX,
                (self.y + 1) * pasY,
                (self.Fd.x) * pasX,
                (self.Fd.y + 1) * pasY,
                width=2,
            )
            self.Fd.AfficheArbre(lecanva)
        if self.filsGauche():
            # trace la branche gauche
            lecanva.create_line(
                (self.x) * pasX,
                (self.y + 1) * pasY,
                (self.Fg.x) * pasX,
                (self.Fg.y + 1) * pasY,
                width=2,
            )
            self.Fg.AfficheArbre(lecanva)
        # affiche etiquette
        lecanva.create_oval(
            (self.x) * pasX - rayon,
            (self.y + 1) * pasY - rayon,
            (self.x) * pasX + rayon,
            (self.y + 1) * pasY + rayon,
            fill="white",
        )
        placeX = (self.x) * pasX - 0.8 * rayon
        placeY = (self.y + 1) * pasY - 0.5 * rayon
        Label(
            lecanva, bg="white", anchor="center", width=3, padx=0, pady=0, text=self.Et
        ).place(x=placeX, y=placeY)


##########################################################


def testsUnitaires():
    # a=ArbreBin(5,ArbreBin(3),ArbreBin(8,None,ArbreBin(5)))
    a = ArbreBin(
        27,
        ArbreBin(2, ArbreBin(8, ArbreBin(5)), ArbreBin(13, ArbreBin(25), ArbreBin(7))),
        ArbreBin(16, ArbreBin(26), ArbreBin(17)),
    )
    # a=ArbreBin(1 ,ArbreBin(0, ArbreBin(4), ArbreBin(8,ArbreBin(5),ArbreBin(6) ) ), ArbreBin(3))
    print("hauteur : ", a.hauteur())
    print("nb noeud :", a.nbNoeud())
    print("parcours largeur :", a.p_largeur())
    print("parcours prefixe :", a.p_prefixe())
    print("parcours infixe :", a.p_infixe())
    a.joliDessin()
