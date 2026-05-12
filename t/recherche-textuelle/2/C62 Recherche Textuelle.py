#####################################################
#            C62 Recherche Textuelle 2              #
#      De l'algorithme naïf à l'algorithme MP       #
#####################################################

import time

def timer(f):
    """ Décorateur python
        Calcule et affiche le temps d'exécution d'une fonction """
    def fonctionModifiee(x,y):
        debut = time.time()
        valeur = f(x,y)
        fin = time.time()
        print(f"Durée : {fin - debut}  secs")
        return valeur
    return fonctionModifiee

@timer #le @timer est un décorateur qui permet de modifier la fonction suivante. Ici, il s'agit d'ajouter l'affichage du temps d'exécution de la foncton algoNaif à chaque appel de cette fonction.
def algoNaif(texte,motif):
    """ Comparaison caractère après caractère du texte et du motif.
        En cas de non correspondance de caractère (=mismatch), on fait glisser la fenêtre du motif d'un cran  """
    t,m = len(texte),len(motif)
    occurence = []
    for i in range (t - m + 1): # Parcours de tous les caractères du texte
        j = 0 # On se place au début du motif
        while j < m and texte[i+j] == motif[j]: # les caractères du texte et du motif correspondent mais on n'a pas encore parcouru tout le motif
            j += 1
        if j == m: # motif trouvé dans le texte
            occurence.append(i)
    if occurence :
        return "le motif a été trouvé en position(s) : " + str(occurence)
    return "le motif est absent du texte"


def preTraitement(motif) :
    """ Renvoie un tableau qui contient, pour chaque caractère du motif repéré par son indice, la position à partir de laquelle reprendre la recherche en cas de non-correspondance  """
    pass

@timer
def rechercheMP(texte,motif):
    """ Algorithme de Morris Pratt"""
    pass



def ouvrirFichierTxt(nomFichier): # ouverture d'un fichier txt
    """ Ouvre un fichier texte et recopie les caractères dans une liste
    de caractères """
    f = open (nomFichier,"r")
    texte = f.read()
    f.close()
    return texte

''' Quelques tests '''

# T1 = 'aacabacabaabaaa'
# T2 = 'abaa'
# M = 'abaa'
# print ("algo Naïf :",algoNaif(T1,M))
# print ("algo Naïf :",algoNaif(T2,M))
# print ("algo KMP :",rechercheMP(T1,M))
# print ("algo KMP :",rechercheMP(T2,M))

''' Recherche de gènes présents dans le génome du SARS-CoV-2 '''

# texte = ouvrirFichierTxt('Genome_SARS_CoV_2.txt')
# motif = ouvrirFichierTxt('Gene_ASP.txt')
# motif = ouvrirFichierTxt('Gene_ORF6.txt')
# motif = ouvrirFichierTxt('Gene_HIV2gp3.txt')
# motif = ouvrirFichierTxt('Gene_S.txt')
# print (rechercheMP(texte,motif))

''' pour comparer la vitesse d'exécution des deux algos '''

# texte = ouvrirFichierTxt('zero.txt')
# motif = '000000000000000000000000001'
# print("algo MP :")
# rechercheMP(texte,motif)
# print("algo naïf :")
# algoNaif(texte,motif)


