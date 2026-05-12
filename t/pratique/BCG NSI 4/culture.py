#############################################################################
# Jeux de données fournis                                                   #
#############################################################################
from plantes import Plante, plantes
from mesures import mesures

#############################################################################
# Écrire le code de la fonction croissance_moyenne de la question 1         #
#############################################################################


def croissance_moyenne(plantes):
    if len(plantes) == 0:
        return None

    croissances = 0

    for plante in plantes:
        croissances += plante.croissance

    return croissances / len(plantes)

#############################################################################
# Écrire le code de la fonction dictionnaire_mesure de la question 2      #
#############################################################################


def dictionnaire_mesure(plantes, mesures):
    if len(plantes) == 0 or len(mesures) == 0:
        return None

    dic = {}

    for plante in plantes:
        dic[plante.nom] = []

    for mesure in mesures:
        nom = mesure["plante"]
        dic[nom].append(mesure)

    return dic


#############################################################################
# Fonction défaillante à analyser et corriger pour les questions 3 et 4     #
#############################################################################

def purger_mesures_extremes(liste_mesures):
    """
    Supprime de la liste toutes les mesures dont la température 
    n'est pas comprise entre 20 et 25°C inclus.
    """
    lst = []

    for mesure in liste_mesures:
        if mesure['temperature'] < 20 or mesure['temperature'] > 25:
            lst.append(mesure)

    return lst


def test_purger():
    mesures_test = [
        {'jour': 1, 'plante': 'Basilic', 'temperature': 18.0},
        {'jour': 2, 'plante': 'Basilic', 'temperature': 19.0},
        {'jour': 3, 'plante': 'Basilic', 'temperature': 22.0},
        {'jour': 4, 'plante': 'Basilic', 'temperature': 28.0},
        {'jour': 5, 'plante': 'Basilic', 'temperature': 29.0}
    ]

    purger_mesures_extremes(mesures_test)

    print("Résultat après la purge :")
    for m in mesures_test:
        print(f"Jour {m['jour']} : {m['temperature']}°C")


print(croissance_moyenne([
    Plante("Basilic", "Ocimum basilicum", 60, 40, "plein soleil"),
    Plante("Tomate", "Solanum lycopersicum", 80, 100, "plein soleil"),
    Plante("Menthe", "Mentha spicata", 80, 50, "mi-ombre"),
    Plante("Tournesol", "Helianthus annuus", 85, 200, "plein soleil"),
    Plante("Fougère", "Dryopteris filix-mas", 90, 80, "ombre")
]))

print(dictionnaire_mesure(plantes, mesures))
