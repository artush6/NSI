# -*- coding: utf-8 -*-
##########################################################
##                    Séance C33_Arbre5                 ##
##               Fichier ExerciceBilan.py               ##
##                       VERSION ELEVE                  ##      ##########################################################


class File :
    """Classe File"""
    def __init__(self):
        """Constructeur de la classe"""
        self.__file = []
    
    def enfiler(self, x):
        """enfiler l'élement x en queue de la file"""
        self.__file.append(x)
        
    def defiler(self):
        """defile l'élement de tête de la liste et le retourne"""
        return self.__file.pop(0)
    
    def est_vide(self):
        """si la file est vide elle retourne True et False sinon"""
        if len(self.__file) != 0:
            return False
        else:
            return True


class Noeud :
    """classe noeud"""
    def __init__(self, cle):
         """Constructeur de la classe"""
         self.Cle = cle
         
class Arbre:
    """classe Arbre"""
    def __init__(self, cle):
         """Constructeur de la classe"""
         self.Racine = Noeud(cle)
         self.Sag = None
         self.Sad = None
        
    def Taille(self, a):
        """Retourne la taille de l'arbre a"""
        if a == None:
            return 0 
        else: 
            return 1 + self.Taille(a.Sag) + self.Taille(a.Sad)

    
    def ParcoursLargeur(self):
        """Parcours l'arbre en largeur et retourne la liste des clés des noeuds"""
 
    
    def ParcoursPrefixeRec(self, lst, arbre):
        """Parcours l'arbre en préfixe récursivement"""
        
        if arbre is None: 
            return
        
        lst.append(arbre.Racine.Cle)

        self.ParcoursPrefixeRec(lst, arbre.Sag)
        self.ParcoursPrefixeRec(lst, arbre.Sad)
        
        

        
    def ParcoursInfixeRec(self, lst, arbre):
        """Parcours l'arbre en inffixe récursivement"""
        
        if arbre is None:
            return
        
        self.ParcoursInfixeRec(lst, arbre.Sag)
        lst.append(arbre.Racine.Cle)
        self.ParcoursInfixeRec(lst, arbre.Sad)

    
    def ParcoursSuffixeRec(self, lst, arbre):
        """Parcours l'arbre en inffixe récursivement"""
        
        if arbre is None: 
            return
        
        self.ParcoursSuffixeRec(lst, arbre.Sag)
        self.ParcoursSuffixeRec(lst, arbre.Sad)
        lst.append(arbre.Racine.Cle)
        

            

                     
#################### Programme principal #####################################"
arbre = Arbre(37)
arbre.Sag = Arbre(41)
arbre.Sag.Sag = Arbre(13)
arbre.Sag.Sag.Sad= Arbre(3)
arbre.Sag.Sag.Sad.Sag= Arbre(5)
arbre.Sag.Sag.Sad.Sad = Arbre(23)
arbre.Sad = Arbre(2)
arbre.Sad.Sag = Arbre(7)
arbre.Sad.Sad = Arbre(11)
arbre.Sad.Sad.Sag = Arbre(19)

print("Taille : ")
print(arbre.Taille(arbre))
#
#lst_larg = arbre.ParcoursLargeur()
#print("parcours en largeur")
#print(lst_larg)
#
print("parcours en préfixe")
lst_pref= []
arbre.ParcoursPrefixeRec(lst_pref, arbre)
print(lst_pref)

print("parcours en infixe")
lst_pref= []
arbre.ParcoursInfixeRec(lst_pref, arbre)
print(lst_pref)
print("parcours en suffixe")
lst_suf= []
arbre.ParcoursSuffixeRec(lst_suf, arbre)
print(lst_suf)


