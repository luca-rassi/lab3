import string


class Padaria():
    def fazerBolo(cobertura: string): cobertura


class aniversario_cobertura():
    def __init__(self,sabor):
        self.sabor = sabor


class BoloAniversario():
    def __init__(self):
        self.cobertura()

    def definir_cobertura(self):
        self.cobertura.aniversario_cobertura('chocolate')

        
class casamento_cobertura():
    def __init__(self):
        self.cobertura()


class BoloCasamento():
    def __init__(self,cobertura):
        self.cobertura = cobertura

    def definir_cobertura(self):
        self.cobertura.casamento_cobertura('baunilha')


class festa_cobertura():
    def __init__(self,sabor):
        self.sabor = sabor


class BoloFesta():
    def __init__(self):
        self.cobertura()

    def definir_cobertura(self):
        self.cobertura.festa_cobertura('ninho')


class cobertura():
    def __init__(self,cobertura):
        self.cobertura = cobertura
