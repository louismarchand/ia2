import sys
sys.path.append(".")
from . import state
from . import StateA
from . import StateB

class StateE(state.State):
    """
    ETAT E de l'automate
    SI LECTURE de :
        -'qui' alors aller à l'état A
        -sinon aller à l'état B
    """
    def __init__(self,prevState=None):
        self.prevState=prevState
        self._whoami=" ETAT E : "
    def step(self,parsing,requete):
        if(parsing[0]=="qui"):                          #si lecture du mot "qui"
            del parsing[0]                              #supprimer le mot traité
            return StateA.StateA(self)                             #ALLER à L'ETAT A


        return StateB.StateB(self)                                 #ALLER à L'ETAT B
        pass
