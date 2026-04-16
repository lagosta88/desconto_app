import abc

class Idesconto(abc.ABC):
    @abc.abstractmethod
    def calcular(self, valor):
        raise NotImplementedError


class DescontoNormal(Idesconto):
    def calcular(self, valor):
        return valor * 0.1
    

class DescontoVip(Idesconto):
    def calcular(self, valor):
        return valor * 0.2  
    

class DescontoPremium(Idesconto):
    def calcular(self, valor):
        return valor * 0.3
    

