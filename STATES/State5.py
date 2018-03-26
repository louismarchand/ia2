import sys
sys.path.append(".")
from . import state
from . import StateA
from . import StateD
from . import State3


class State5(state.State):
    """
    ETAT 5 de l'automate
    Traitements :
        -si un "qui" est lu alors etat A
        -sinon etat 3
    """
    def __init__(self,prevState=None):
        self.prevState=prevState
        self._whoami=" ETAT 5 : "
    def step(self,parsing,requete):
        if(parsing[0]=="qui"):                              #si on lit un "qui" on passe en StateA
            del parsing[0]
            return StateA.StateA(self)
            
        my_file = open("./DATA/Prepositions.dat","r")       #le fichier contenant les prépositions            
        contenu = my_file.read()                            #le contenu du fichier
        lignes = contenu.split("\n")                        #les lignes du fichier
        for i,ligne in enumerate(lignes):                   #pour chaqque ligne du fichier
            if(parsing[0]==ligne):
                my_file.close()                             #fermeture du fichier
                del parsing[0]                              #suppression du mot traité
                return StateD.StateD(self)
        
        my_file.close()            
        return State3.State3(self)                                     #sinon State3
        pass
