import sys
sys.path.append(".")
from . import state
from . import State2
from . import State3

class StateInit(state.State):
    """
    Etat initiale de l'automate.
    Première lecture de la question.
    Renseignement de la partie : SELECT
    """
    def __init__(self,prevState=None):
        self.prevState=prevState
        self._whoami=" ETAT 1 : question initiale"
    def step(self,parsing,requete):
        my_file = open("./DATA/Interrogatifs.dat","r")
        contenu = my_file.read()
        interrogatifs = contenu.split("\n")
        for i,interrogatif in enumerate(interrogatifs):
            if(parsing[0]==interrogatif):
                del parsing[0]
                my_file.close()
                return State2.State2(self)
            
        my_file.close()
        return State3.State3(self)
        pass
