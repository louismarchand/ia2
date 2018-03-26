import sys
sys.path.append(".")
from . import state
from . import State5




class State4(state.State):
    """
    ETAT 4 de l'automate
    Lecture des noms de rubriques.
    Renseignement de colonnes de la requete. partie SELECT
    """
    def __init__(self,prevState=None):
        self.prevState=prevState
        self._whoami=" ETAT 4 : "
    def step(self,parsing,requete):
        my_file = open("./DATA/NomsRubrique.dat","r")              #le fichier contenant les noms de rubrique
        contenu = my_file.read()                            #le contenu du fichier
        lignes = contenu.split("\n")                        #les lignes du fichier
        for i,ligne in enumerate(lignes):                               #pour chaque ligne du fichier
            nomRubrique = ligne.split(":")                      #la rubrique de la ligne
            if(parsing[0]==nomRubrique[0]):                     #si le mot lu est dans la liste des noms de rubrique
                parameters = nomRubrique[1].split(";")              #récupérer les paramètres

                if(len(parameters[0])!=0 and len(parameters[1])!=0):  # si les paramètres (select,from) sont renseignés
                    for j,col in enumerate(parameters[0].split(",")):
                        requete["select"].append(col)                       #ajout des noms de colonne dans le SELECT
                    for j,tabl in enumerate(parameters[1].split(",")):
                        requete["from"].append(tabl)                        #ajout des noms de table dans le FROM
                        
                    
                else:                                               #si le mot n'est pas reconnu
                    print("JE NE CONNAIS PAS CE MOT : ",parsing[0])
                    print("Qu'est-ce que c'est ?")
                    # FAIRE QUELQUE CHOSE DE PARTICULIER
                    # GENRE DEMANDER LES PARAMETRES DE CE MOT ET L'APPRENDRE
                    my_file.close()                                     #fermer le fichier
                    return
                
                my_file.close()                                     #fermer le fichier
                del parsing[0]                                      #supprimer mot traité
                return State5.State5(self)
        pass
