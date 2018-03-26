import sys
sys.path.append(".")
from . import state
from . import State3
   
class State2(state.State):
    """
    ETAT 2 de l'automate
    Lecture du verbe de la question.
    Permet éventuellement de renseigner la partie : FROM selon le verbe rencontré.
    """
    def __init__(self,prevState=None):
        self.prevState=prevState
        self._whoami=" ETAT 2 : Pronom interrogatif lu"
    def step(self,parsing,requete):
        my_file = open("./DATA/Verbes.dat","r")                    #le fichier contenant les verbes
        contenu = my_file.read()                            #lecture du fichier
        verbes = contenu.split("\n")                        #mettre chaque ligne dans un tableau
        verbe=[]                                            #un verbe dans la liste
        for i,ligne in enumerate(verbes):                               #pour chaque ligne
            verbe = ligne.split(":")                            #récupérer le verbe
            if(parsing[0]==verbe[0]):                           #si le verbe lu est est dans la liste
                parameters = verbe[1].split(";")                    #récupérer les paramètres : cardinalité, table etc...
                if(len(parameters[0])!=0 and len(parameters[1])!=0):# si les paramètres table et colonne sont renseignés
                    for j,fr in enumerate(parameters[1].split(",")):
                        requete["from"].append(fr)                      #ajouter les tables dans le from
                    for j,wh in enumerate(parameters[0].split(",")):
                        requete["where"].append(wh)                     #ajouter les colonnes dans le from
                    
                del parsing[0]                                      #suppression de l'élément traité
                my_file.close()                                     #fermeture du fichier
                
                return State3.State3(self)                                     #PASSER à L'ETAT 3
                
        print("Votre question n'est pas bien formulée.")
        print("Je ne parviens pas à traiter votre demande")
        my_file.close()                                             #fermer le fichier
        return                                                      #sortir
        pass
 
