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
    

class Pedido:
    def __init__(self, desconto: Idesconto):
        self.desconto = desconto
    
    def total(self, valor):
        return valor - self.desconto.calcular(valor)
    
if __name__ == "__main__":
        pedido_normal = Pedido(DescontoNormal())
        print(pedido_normal.total(100))
        
        pedido_vip = Pedido(DescontoVip())
        print(pedido_vip.total(100))
        
        pedido_premium = Pedido(DescontoPremium())
        print(pedido_premium.total(100))
