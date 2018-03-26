import sys
sys.path.append(".")
from . import state


def removeDoublon(liste):
    """
    retirer les doublons dans une liste
    """
    tmp=[]
    for i,elt in enumerate(liste):
        if elt not in tmp:
            tmp.append(elt)
    return tmp

class State6(state.State):
    """
    ETAT 6 de l'automate
    Assemblage des différents éléments de la requête
    """
    def __init__(self,prevState=None):
        self.prevState=prevState
        self._whoami=" ETAT 6 : Requete formée "
    def step(self,parsing,requete):
        """
            CONSTRUCTION d'une requete sql à partir de l'objet 'requete' 
            et des ses différentes entrées.
        """
        #RETIRER LES DOUBLONS EVENTUELS sur chacun des parametres de la requete
        requete["select"]=removeDoublon(requete["select"])
        requete["where"]=removeDoublon(requete["where"])
        requete["whereegal"]=removeDoublon(requete["whereegal"])
        requete["from"]=removeDoublon(requete["from"])
    
        requeteFinale=" SELECT "                                #SELECT
        if(len(requete["select"])==0):                          #colonne(s)
            requeteFinale+=" * "
        else:
            requeteFinale+=",".join(requete["select"])
            
        requeteFinale+=" FROM "                                 #FROM
        requeteFinale+=" NATURAL JOIN ".join(requete["from"])#table(s)
        
        requeteFinale+=" WHERE"                                 #WHERE
        for i,elt in enumerate(requete["where"]):               #condition
            requeteFinale+=" "+elt
            requeteFinale+="="
            requeteFinale+=requete["whereegal"][i]
            requeteFinale+=" AND"
        if(len(requete["where"])!=0):
            requeteFinale=requeteFinale[:len(requeteFinale)-3]  #retirer le dernier 'and'

        if(len(requete["limit"])!=0):                           #LIMIT
            requeteFinale+=" LIMIT 1"
        requeteFinale+=";"                                      #fin construction requete
        requete["finale"]=requeteFinale
        
        return 1                                                #retourner 1 (requete terminée)
        pass
