import abc

class Idesconto(abc.ABC):
    @abc.abstractmethod
    def calcular(self, valor: float) -> float:
        pass


class DescontoNormal(Idesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1
    

class DescontoVip(Idesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.2  
    

class DescontoPremium(Idesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3
    

