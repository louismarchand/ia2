import sys
sys.path.append(".")
from . import state
from . import State4
from . import StateD


class State3(state.State):
    """
    ETAT 3 de l'automate
    Lecture des determinants si il y en a.
    Permet de renseigner la partie : LIMIT
    """
    def __init__(self,prevState=None):
        self.prevState=prevState
        self._whoami=" ETAT 3 : "
    def step(self,parsing,requete):
        my_file = open("./DATA/Determinants.dat","r")              #le fichier contenant les déterminants
        contenu = my_file.read()                                   #le contenu du fichier
        determinants = contenu.split("\n")                         #la liste des déterminants
        for i,ligne in enumerate(determinants):                       #pour chaque ligne du fichier
            determinant = ligne.split(":")                              #la ligne du fichier
            if(parsing[0]==determinant[0]):                             #si le mot lu dans la question est un determinant
                if(determinant[1]!="*"):                                    #si le déterminant est singulier
                    requete["limit"].append(determinant[1])                    #ajouter la limite dans la partie LIMIT de la requete
                    
                del parsing[0]                                              #supprimer l'élément traité
                my_file.close()                                             #fermer le fichier
                return State4.State4(self)                                             #PASSER à L'ETAT 4
        
        my_file.close()
        my_file = open("./DATA/Prepositions.dat","r")               #le fichier contenant les déterminants
        contenu = my_file.read()                                    #le contenu du fichier
        prep = contenu.split("\n")                                  #la liste des déterminants
        for i,ligne in enumerate(prep):                             #pour chaque ligne du fichier
            if(parsing[0]==ligne):                                      #si le mot lu dans la question est un determinant
                my_file.close()                                             #fermer le fichier
                del parsing[0]                                              #supprimer le mot traité
                return StateD.StateD(self)                                             #ALLER à L'2TAT D
                
        
         
        if(len(requete["where"])):                                   #si au moins un élément à été ajouté dans le 'where' à l'étape précédente
            my_file.close()
            return StateD.StateD(self)
                
        #sinon
        my_file.close()                                     #fermer le fichier
        return State4.State4(self)                                     #PASSER à L'ETAT 4
        pass
        

