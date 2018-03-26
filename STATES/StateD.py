import sys
sys.path.append(".")
from . import state
from . import StateE
from . import StateC
from . import State5

class StateD(state.State):
    """
    ETAT D de l'automate.
    2 cas :
        -etat precedant = StateB:
            Permet de lire les valeurs de rubrique et/ou les noms de rubriques suplémentaires.
            Renseignement de 'from' et 'where'
        -etat precedent = State5 ET le mot suivant n'est PAS 'qui'
            Permet de lire le sujet d'une requete. On renseigne alors le 'from' et le 'select'
            ex: Date_naissance des étudiants qui ...
                --> StateD va lire 'etudiants' et renseigner 'nom,prenom' (resp. 'table1') dans 'select' (resp. 'from')
    """
    def __init__(self,prevState=None):
        self.prevState=prevState
        """ CONSTRUCTEUR """
        self._whoami=" ETAT D : "
        
    def step(self,parsing,requete):
        """ ACTION """
        my_file = open("./DATA/NomsRubrique.dat","r")               #le fichier contenant les noms de rubrique
        contenu = my_file.read()                                    #le contenu du fichier
        lignes = contenu.split("\n")                                #les lignes du fichier
        
        for i,ligne in enumerate(lignes):#RECHERCHER le mot dans la liste des noms de rubrique
            
            rubrique = ligne.split(":")                                 #la rubrique courante dans le fichier
            
            if(parsing[0]==rubrique[0]):                                #si on trouve le mot dans la liste
                
                parameters = rubrique[1].split(";")                         #obtention parametres de la rubrique
                
                for j,sel in enumerate(parameters[1].split(",")):           #ajout table dans 'from'
                    requete["from"].append(sel)
                for j,wh in enumerate(parameters[0].split(",")):            #ajout colonnes dans :
                                                                            #'select' si prevState=State5 ET que le prochain mot n'est pas 'qui'
                    if(type(self.prevState)==type(State5.State5()) and parsing[1]=="qui"):
                            requete["select"].append(wh)
                    else:                                                       #'where' si prevState=StateB
                        requete["where"].append(wh)
                    
                my_file.close()                                     #fermer fichier
                del parsing[0]                                      #supprimer mot traité
                return StateE.StateE(self)                          #ALLER à STATE E
        
        
        #ajouter l'apprentisage de vocabulaire.
        # si l'état précédent est State5 et que le mot n'est pas dans la liste des noms de rubrique alors:
        #       -> demander à ajouter le mot dans la liste avec les paramètres corrects       
        
          
        #SINON ALORS le mot est une valeur de rubrique
        val = "\'"+parsing[0]+"\'"                          #récupérer la valeur de rubrique souhaitée
        requete["whereegal"].append(val)                    #ajouter la valeurs à la requete
        del parsing[0]                                      #supprimer le mot traité
        return StateC.StateC(self)                          #ALLER à L'ETAT C
        
        pass
