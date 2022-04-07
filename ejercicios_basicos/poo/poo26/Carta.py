"""_summary_

    Juego de Cartas con POO

"""

class Carta:
    def __init__(self, numero: int, palo: str)-> None:
        self.palo = palo
        self.numero = numero
        
    def imprimir(self)-> None:
        letra_numero: str = self.convertir_numero_a_letras()
        print(f"{letra_numero} de {self.palo}")
        
    def convertir_numero_a_letras(self) -> str:
        valor: str = ""
        if (self.numero == 11):
            valor = "J"
        elif (self.numero == 12):
            valor = "Q"
        elif (self.numero == 13):
            valor = "K"    
        elif (self.numero == 1):
            valor = "As"
        else:
            valor = str(self.numero)
        return valor

if __name__ == '__main__':
    carta: Carta = Carta(11, "Treboles")
    carta.imprimir()