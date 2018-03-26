import sys
sys.path.append(".")
from . import state
from . import State5
from . import State6

# FINIR L'ETAT C
class StateC(state.State):
    """
    ETAT C de l'automate
    SI LECTURE de :
        -'et' alors retour à l'état 5
        -sinon aller à l'état 6
    """
    def __init__(self,prevState=None):
        self.prevState=prevState
        self._whoami=" ETAT C : "
    def step(self,parsing,requete):
        if(parsing[0]=="et"):
            del parsing[0]
            return State5.State5(self)
        
        return State6.State6(self)
        pass
 
