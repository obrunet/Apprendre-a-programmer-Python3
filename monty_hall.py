from enum import Enum
import numpy as np


class Strategie(Enum):
    "Définition d'une sous-classe de Enum, qui contiendra les stratégies possibles."
    CHANGER = 1
    GARDER = 2


def play_several_games(strategie, nb_tours):
    """Fonction simulant plusieurs parties du jeu Monty Hall.
    Args:
        strategie (Strategie): La strategie du joueur
        nb_tours (int): Nombre de tours  
    Returns:
        tableau_gains: résultats sous forme d'un tableau des gains du joueur (suite de 1 ou 0)
    """
    tableau_gains = np.array([], dtype = int)
    
    for i in range(nb_tours):                                   # simulation d'une partie du jeu Monty Hall:
        
        portes = np.array([0, 1, 2])
        bonne_porte = np.random.randint(3, size = 1)            # Choix de la bonne porte au hasard entre 0 et 2 inclus
        premier_choix = np.random.randint(3, size = 1)          # Choix du joueur au hasard entre 0 et 2 inclus 
        portes = np.delete(portes, premier_choix)               # Le présentateur élimine une porte : il reste deux portes
        
        if premier_choix == bonne_porte:                        # si le joueur choisit la bonne porte
            portes = np.delete(portes, np.random.randint(2, size = 1))  # le présentateur éliminte 1 des deux 2 restantes au hasard
        else:                                                   # sinon le présentateur retire la mauvaise portes parmi les deux restantes
            portes = bonne_porte                                # dans les portes restantes il n'y a plus que la bonne
        
        deuxieme_choix = 0                                      # Le deuxieme choix depend de la strategie
        if strategie == Strategie.CHANGER:
            deuxieme_choix = portes[0]                          # s'il change son choix se dirige vers la porte restante
        elif strategie == Strategie.GARDER:
            deuxieme_choix = premier_choix                      # s'il ne change pas : reste sur son choix initial
        else:
            raise ValueError("Stratégie non reconnue!")
        
        resultat_partie = 1 if deuxieme_choix == bonne_porte else 0     # 1 si le joueur a gagné cette partie sinon 0
        tableau_gains = np.append(tableau_gains, np.array(resultat_partie))
        i += 1

    return tableau_gains


if __name__ == "__main__":
    # juste un test :
    print("test", play_several_games(Strategie.CHANGER, 10))