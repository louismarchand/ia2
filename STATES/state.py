import abc

class State(metaclass=abc.ABCMeta):
    """
    Classe abstraite modélisant un état de l'automate.
    """
    def whoami(self):
        """
        Afficher le type de la classe
        """
        print("-----",self._whoami)
    @abc.abstractmethod
    def step(self,parsing,traite,order,limit):
        """
        Effectuer le traitement associer à l'état de l'automate
        """
        pass
