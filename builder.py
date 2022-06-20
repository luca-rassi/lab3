
class Bolo:
 
    def __init__(self):
        self.Cobertura()
 
    def Cobertura(self):
        raise NotImplementedError
 
    def __repr__(self):
        return 'Cobertura : {0.cobertura}'.format(self)
 

class BoloAniversario(Bolo):
 
    def Cobertura(self):
        self.cobertura = "Aniversario"
 
    def __str__(self):
        return "Bolo de Aniversario"
 

class Festa(Bolo):
 
    def Cobertura(self):
        self.cobertura = "Festa"
 
    def __str__(self):
        return "Bolo de Festa"

class Casamento(Bolo):
 
    def Cobertura(self):
        self.cobertura = "Casamento"
 
    def __str__(self):
        return "Bolo de Casamento"
 
 

def construct_bolo(cls):
 
    bolo = cls()
    bolo.Cobertura()
 
    return bolo    