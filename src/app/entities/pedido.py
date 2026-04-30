import abc
from src.app.entities.desconto import Idesconto

class Pedido:
    def __init__(self,cliente:str, valor_original: float, desconto: Idesconto):
        self.cliente = cliente
        self.desconto = desconto
        self.valor_original = valor_original

    def valor_desconto(self) -> float:
        return self.desconto.calcular(self.valor_original)

    def valor_final(self, valor) -> float:
        return self.valor_original - self.valor_desconto()
 