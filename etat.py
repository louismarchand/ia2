import sqlite3
import sys
sys.path.append("./")
from STATES import StateInit
import initDB as dbm


class Automate:
    """
    Classe context. Son état varie en fonction de situations
    Contient les objets pour la construction de la requete SQL.
    """
    def __init__(self,state,question,requete=[]):
        self._state=state                               #L'état courant
        self._question=question                         #La question posée
        self._parsing=self._question.split(" ")         #La question splitée sur les espaces
        self._requete= dict()                           #la requete à construire
        self._requete["select"]=[]                   #le selecteur de la requete
        self._requete["from"]=[]                        #le from
        self._requete["where"]=[]                       #le where
        self._requete["whereegal"]=[]                   #les valeurs du where
        self._requete["order"]=[]                       #le tri
        self._requete["limit"]=[]                       #le nombre de résultat souhaité
        self._requete["finale"]=""
        
    def nextStep(self):
        """
        Cette methode fait avancer d'une étape l'automate dans la reconnaissance de la question.
        A chaque étape franchie, la requête se construit et l'état actuel de l'automate change.
        """

        self._state = self._state.step(self._parsing,self._requete)#Avancer d'une étape
        
    def afficher(self):
        self._state.whoami()                            #Afficher le statut de l'automate
        print("\tQuestion : ",self._question)           #La question posée
        print("\tReste à lire : ",self._parsing)        #Le reste à traiter de la question
        print("\tRequete : ")             #La requête sous forme de liste (en cours de construction)
        for name,val in enumerate(self._requete):
            print(val,"\t:\t",self._requete[val])
        


        

def main():
    """
    PROGRAMME PRINCIPAL
    """
    print("*********************************")
    print("*********AUTOMATE 3000***********")
    print("*********************************")
    connexion = dbm.initDB()                                    #intialisation de la base de données et obtention de la connexion
    
    with connexion:
        cursor = connexion.cursor()                                 #le curseur de la connexion    
        verbose = input("Mode verbose ? (O)ui : ").lower()          #mode verbose ? oui/non
        
        print("(help) Tapez Q pour quitter.")
        
        while(True):
            print("")
            question = input("Posez moi une question : ").lower()       #poser une question
            if(question=="q"):
                print("À bientôt")
                return
            
            etatInitiale = StateInit.StateInit()                       #initialisation premier état automate
            automate = Automate(etatInitiale,question)                #initialisation context automate
            
            print("","Je réfléchis...","",sep="\n")
                
            
            while(automate._state!=1):                                   #l'automate renvoie 1 quand il termine
                if(verbose=="o"):                                           #si verbose
                    automate.afficher()                                          #afficher détails
                automate.nextStep()                                          #faire avancer l'automate
            
            if(verbose=="o"):                                           #afficher la requete formée
                print("    La question était : ")
                print("   "+question)
                print("    La requete construite est la suivante : ")
                print("   "+automate._requete["finale"])
                print("")
            
            
            
            cursor.execute(automate._requete["finale"])                  #execution de la requete

            rows = cursor.fetchall()                                    #obtention des résultats
            
            print("J'ai trouvé ",len(rows)," réponse(s) :")             #Affichage des résultats
            for i,row in enumerate(rows):
                print("   n°",i+1,":",row)
            
            
    
if __name__ == "__main__":
    main()
    
    
       
#
#MIEUX GERER l'attribution du where et des valeurs associés.
# FAIRE EN MODE CLé. pour que quand on renseigne la valeur m2pro par exemple on la mette pour le where diplome
#
# ou ALORS ALLER CHERCHER LES BVALEURS DE RUBRIQUE DANS LE FICHIER ET ALORS ON CONNAIT LES WHERE ASSOCIés
#
# et donc pour le moment ça : naissance des etudiants qui préparent le diplome m2pro ?
#   ça déconne.
# mais pas : les responsables du diplome m2pro ?
