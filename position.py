class Position:
    """Classe définissant les positions de la main possibles'"""

    
    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""
    def __init__(self,poignet,doigt):
        """Par défaut, notre surface est vide"""
        self.surface = ""
    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""

        
        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire
