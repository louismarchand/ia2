import sys
sys.path.append(".")
from . import state
from . import StateB


class StateA(state.State):
    """
    ETAT A de l'automate
    DEBUT DE LA PARTIE TRAITEMENT DES CONDITIONS ET RESTRICTIONS DE LA REQUETE
    Lecture du verbe qui suit le mot "qui" dans la question forumlée.
    Renseignement 
    """
    def __init__(self,prevState=None):
        self.prevState=prevState
        self._whoami=" ETAT A : "
    def step(self,parsing,requete):
        my_file = open("./DATA/Verbes.dat","r")                    #le fichier contenant les verbes            
        contenu = my_file.read()                            #le contenu du fichier
        lignes = contenu.split("\n")                        #les lignes du fichier
        for i,ligne in enumerate(lignes):                               #pour chaqque ligne du fichier
            verbe = ligne.split(":")                            #la ligne
            if(parsing[0]==verbe[0]):                           #si le mot lu est dans la liste des verbes
                parameters=verbe[1].split(";")                      #récupérer les paramètres
                if(len(parameters[0])!=0 and len(parameters[1])!=0): # si les parametres sont renseignés
                    for j,wh in enumerate(parameters[0].split(",")):
                        requete["where"].append(wh)                     #ajouter les colonnes dans le SELECT
                    for j,fr in enumerate(parameters[1].split(",")):
                        requete["from"].append(fr)                      #ajouter les tables dans le FROM
                
                my_file.close()                                     #fermer le fichier
                del parsing[0]                                      #supprimer le mot traité
                return StateB.StateB(self)                                     #ALLER à L'ETAT B
        
        
        print("Je ne connais pas le mot",parsing[0],"est-ce bien un verbe ?")
        print("Je ne parviens pas à traiter votre demande")
        my_file.close()                                             #fermer le fichier
        return                                                      #sortir
        pass
