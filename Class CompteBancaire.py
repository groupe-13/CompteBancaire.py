# AL-HADI MAHAMAT AHMAT
  # matricule:18A851FS
class CompteBancaire:
      # creation classe mere Banque
    def __init__(self,nomB,nomTitulaire,solde,lieu):
        self.nomB=nomB
        self.nomTitulaire=nomTitulaire
        self.solde=solde
        self.lieu=lieu
    def set_nomB(self,nomB):
        self.nomB=nomB
    def get_nomB(self):
        return self.nomB
    def set_nomTitulaire(self,nomTitulaire):
        self.nomTitulaire=nomTitulaire
    def get_nomTitulaire(self):
        return self.nomTitulaire
    def set_solde(self,solde):
        self.solde=solde
    def get_solde(self):
        return self.solde
    def set_lieu(self,lieu):
        self.lieu=lieu
    def get_lieu(self):
        return self.lieu
    def depot(self,mt):
        self.solde+=mt
        print("la solde deposée est de :",self.solde)
    def retrait(self,mt):
        if(self.solde-mt>=0):
            self.solde-=mt
            print("vous avez fait un retrait de ",mt)
        else:
             print("solde est insuffisante pour faire le retrait")
  #programme principal
B=CompteBancaire("EUI","Alhadi",10,"Dang")
B.depot(100)
B.retrait(200)
print("Nom de la banque: {}, son Titulaire: {} a une balance {}$ et situé à : {} ".format(B.nomB,B.nomTitulaire,B.solde,B.lieu))
