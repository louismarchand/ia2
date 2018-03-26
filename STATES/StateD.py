import sys
sys.path.append(".")
from . import state
from . import StateE
from . import StateC

class StateD(state.State):
    """
    ETAT E de l'automate
    Permet de lire les valeurs de rubrique et/ou les noms de rubriques suplémentaires.
    """
    def __init__(self):
        self._whoami=" ETAT D : "
    def step(self,parsing,requete):
        my_file = open("./DATA/NomsRubrique.dat","r")              #le fichier contenant les noms de rubrique
        contenu = my_file.read()                            #le contenu du fichier
        lignes = contenu.split("\n")                        #les lignes du fichier
        for i,ligne in enumerate(lignes):                               #pour chaque ligne du ficher
            nomRub = ligne.split(":")                           #la ligne
            if(parsing[0]==nomRub[0]):                          #si le mot lu est dans la liste des noms de rubrique
                
                parameters = nomRub[1].split(";")                   #obtention parametres
                for j,sel in enumerate(parameters[1].split(",")):
                    requete["from"].append(sel)                     #ajout table dans 'from'
                for j,wh in enumerate(parameters[0].split(",")):
                    requete["where"].append(wh)                     #ajout colonne dans 'where'
                    

                    
                    
                my_file.close()
                del parsing[0]
                return StateE.StateE()
               
        #SUREMENT UN CAS NON 2TUDIÉ  ici
                
                
        
        #si pas un nom de rubrique     
        val = "\'"+parsing[0]+"\'"                      #récupérer la valeur de rubrique souhaitée
        requete["whereegal"].append(val)                  #ajouter la valeurs à la requete
        del parsing[0]                                  #supprimer le mot traité
        return StateC.StateC()                                 #ALLER à L'ETAT C
        
        pass
