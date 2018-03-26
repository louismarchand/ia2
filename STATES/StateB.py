import sys
sys.path.append(".")
from . import state
from . import StateD


class StateB(state.State):
    """
    ETAT B de l'automate
    Lecture des déterminants ou prépositions, ou rien
    """
    def __init__(self,prevState=None):
        self.prevState=prevState
        self._whoami=" ETAT B : "
    def step(self,parsing,requete):
        my_file = open("./DATA/Determinants.dat","r")              #le fichier contenant les déterminants
        contenu = my_file.read()                            #le contenu du fichier
        lignes = contenu.split("\n")                        #les ligens du fichier
        for i,ligne in enumerate(lignes):                               #pour chaque ligne du fichier
            det = ligne.split(":")                              #la ligne
            if(parsing[0]==det[0]):                              #si le mot lu est dans la liste des déterminants
                my_file.close()                                     #fermeture du fichier
                del parsing[0]                                      #supprimer le mot traité
                return StateD.StateD(self)                                     #ALLER à L'ETAT D
        
        my_file.close()
        
        my_file = open("./DATA/Prepositions.dat","r")              #le fichier contenant les déterminants
        contenu = my_file.read()                            #le contenu du fichier
        lignes = contenu.split("\n")                        #les ligens du fichier
        for i,ligne in enumerate(lignes):                               #pour chaque ligne du fichier
            if(parsing[0]==ligne):                              #si le mot lu est dans la liste des déterminants
                my_file.close()                                     #fermeture du fichier
                del parsing[0]                                      #supprimer le mot traité
                return StateD.StateD(self)                                     #ALLER à L'ETAT D
                
        my_file.close()
        return StateD.StateD(self)
        
        pass 
