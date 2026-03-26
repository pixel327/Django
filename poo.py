class Vehicule:
    def __init__(self,matriculation,poids,annee):
        self.matriculation = matriculation
        self.poids = poids
        self.annee = annee

class Fourgon(Vehicule):
    def __init__(self,matriculation,annee,charge):
        super().__init__(matriculation,annee)
        self.charge = charge
        self.poids = 2
        self.poids_max = 3
        self.vitmaxvide = 110
        self.vitmaxcharge = 100
    def __str__(self):
        return

class Camion(Vehicule):
    def __init__(self,matriculation,annee,charge):
        super().__init__(matriculation,annee)
        self.charge = charge
        self.poids = 5 
        self.poids_max = 6
        self.vitmaxvide = 110
        self.vitmaxcharge = 90
        self.vitmaxchargemax = 80

class Buss(Vehicule):
    def __init__(self,matriculation,annee,charge):
        super().__init__(matriculation,annee)
        self.charge = charge
        self.poids = 20
        self.vitmax = 100

class Taxi(Vehicule):
    def __init__(self,matriculation,annee,charge):
        super().__init__(matriculation,annee)
        self.charge = charge
        self.poids = 2
        self.vitmax = 130

class Flote:
    def __init__(self,f,vitesse):
        self.tab = []
        self.f = f
        self.vitesse = vitesse
    def ajouter_vehicule(self,v):
        self.tab.append(v)
    def afficher(self):
        for vehicule in self.tab:
            print(vehicule)
    def vitessFlote(self):
        if self.f == False:
            return 0
        else:
            return self.vitesse
    def positionneCovoi(self,i,v):
        self.tab.insert(i,v)
    def enleveConvoi(self,i):
        del self.tab[i]

