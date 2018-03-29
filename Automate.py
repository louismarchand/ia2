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
    def __init__(self,question,requete=[]):
        self._state=StateInit.StateInit()               #L'état courant
        self._question=question                         #La question posée
        self._parsing=self._question.split(" ")         #La question splitée sur les espaces
        self._requete= dict()                           #la requete à construire
        self._requete["select"]=[]                      #le selecteur de la requete
        self._requete["from"]=[]                        #le from
        self._requete["where"]=[]                       #le where
        self._requete["whereegal"]=[]                   #les valeurs du where
        self._requete["order"]=[]                       #le tri
        self._requete["limit"]=[]                       #le nombre de résultat souhaité
        self._requete["finale"]=""
        
        self._finished=False                            #boolean valant True quand l'automate est terminé
        
    def nextStep(self):
        """
        Cette methode fait avancer d'une étape l'automate dans la reconnaissance de la question.
        A chaque étape franchie, la requête se construit et l'état actuel de l'automate change.
        """

        self._state = self._state.step(self._parsing,self._requete)#Avancer d'une étape
        if(self._state==1):
            self._finished=True
        else:
            self._finished=False
        
    def afficher(self):
        """
            Afficher en détail l'état actuel de l'automate
        """
        self._state.whoami()                            #Afficher le statut de l'automate
        print("\tQuestion : ",self._question)           #La question posée
        print("\tReste à lire : ",self._parsing)        #Le reste à traiter de la question
        print("\tRequete : ")             #La requête sous forme de liste (en cours de construction)
        for name,val in enumerate(self._requete):
            print(val,"\t:\t",self._requete[val])
        
    def isFinished(self):
        """
            Renvoyer la vrai si l'automate a terminé
        """
        return self._finished



def launchAutomate3000(verbose,cursor):
    """
        LANCER LE SUPER AUTOMATE3000
    """
    while(True):                            #EN BOUCLE ('q' pour sortir)
            print("")
            question = input("Posez moi une question : ").lower()       #poser une question
            if(question=="q"):                                          #si 'q' alors sortir
                print("À bientôt")
                return
            
            automate = Automate(question)                               #initialisation de l'AUTOMATE
            
            print("","Je réfléchis...","",sep="\n")
            
            while(not automate.isFinished()):                           #tant que l'automate n'est pas terminé
                if(verbose=="o"):                                           #si verbose
                    automate.afficher()                                          #afficher détails
                automate.nextStep()                                         #faire avancer l'automate
            
            if(verbose=="o"):                                           #afficher un rappel
                print("    La question était : ")
                print("   "+question)
                print("    La requete construite est la suivante : ")
                print("   "+automate._requete["finale"])
                print("")
            else:
                print("    La requete construite est la suivante : ")
                print("   "+automate._requete["finale"])
                print("")
            
            
            cursor.execute(automate._requete["finale"])                 #execution de la requete formée
            rows = cursor.fetchall()                                    #obtention des résultats
            print("J'ai trouvé ",len(rows)," réponse(s) :")             #Affichage des résultats
            for i,row in enumerate(rows):
                print("   n°",i+1,":",row)
    
    pass


def launchTests(verbose,cursor):
    """
        LANCER L'AUTOMATE AVEC UN JEU DE QUESTION
    """
    print("#############","MODE TEST","#############",sep="\n")
    question = (
        "qui habite à angers ?",
        "qui habite paris ?",
        "un étudiant qui prépare le diplome m2pro ?",
        "naissance des etudiants qui preparent le diplome m1informatique ?",
        "qui est le responsable du diplome m1informatique ?",
        "quelles sont les personnes qui habitent à paris ?",
        "quelles sont les personnes qui habitent à angers et qui préparent le diplome m1informatique ?",
        "quels sont les etudiants qui preparent le diplome m2pro ?",
        "qui prépare le diplome m1informatique ?",                          #ne fonctionne pas correctement
        "ou habite les etudiants qui preparent le diplome m2pro ?"          #ne fonctionne pas
    )
    
    taille = len(question)                                              #le nombre de question
    bueno = 0                                                           #le nombe de question ne provoquant pas d'erreur
    
    try:
        for i,q in enumerate(question):
            print("Question n°",i+1,":",q)
            automate = Automate(q)
            while(not automate.isFinished()):
                if(verbose=="o"):                                           #si verbose
                    automate.afficher()                                          #afficher détails
                automate.nextStep()                                         #faire avancer l'automate
            
            print("    "+automate._requete["finale"])
            cursor.execute(automate._requete["finale"])
            rows = cursor.fetchall()
            for j,row in enumerate(rows):
                print("  n°",j+1,":",row)
                
            print()
            bueno+=1
    except:
        print("","Une erreur est survenu ","oups !","",sep="\n")
    finally:
        res = bueno/taille
        gauche = (""+str(res)).split(".")[0]
        droite = (""+str(res)).split(".")[1]
        res = gauche+"."+droite[:2]
        print("Résultats (",res,"% )")                       #afficher le nombre de 'succès'
    

def main():
    """
    PROGRAMME PRINCIPAL
    """
    print("*********************************")
    print("*********AUTOMATE 3000***********")
    print("*********************************")
    
    verbose = input("Mode verbose ? (O)ui : ").lower()          #mode verbose ? oui/non
    print("  Tapez Q pour quitter.")
    
    connexion = dbm.initDB()                                    #intialisation de la base de données et obtention de la connexion
    with connexion:
        cursor = connexion.cursor()                                 #le curseur de la connexion
        
        #Au choix :
        print("Quel automate voulez-vous choisir ?")
        test = input("  (T)est ou (I)nterractif : ")
        if(test.lower()=="t"):
            launchTests(verbose,cursor)            #le mode test avec une batterie de question
        else:
            launchAutomate3000(verbose,cursor)     #le vrai automate interractif
        
    pass
    

    
if __name__ == "__main__":
    main()
    
    
       
# A FAIRE
#
# Pour faire en sorte que les Questions 8 et 9 fonctionnent:
#     ajouter au verbes la notion de (objet du verbe et sujet du verbe)
#           exemple : preparent:diplome;table1!prenom,nom;table1
#               car on prépare un diplome (l'objet) et c'est prenom,nom (le sujet) qui prépare
#     ainsi à l'étape 5 de l'automate on peut determiner si le nom de rubrique qu'on lit doit nous renseigner sur le sujet ou l'objet du precedent verbe
#     ainsi à l'étape 3 de l'automate on sait si l'on doit utiliser le sujet du verbe ou pas selon le PI précédent           
#
#   Et donc ajouter la notion de sujet/objet aux PI
