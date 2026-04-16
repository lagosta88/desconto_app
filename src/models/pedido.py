import abc
from .desconto import Idesconto, DescontoNormal, DescontoVip, DescontoPremium 

class Pedido:
    def __init__(self,cliente, desconto: Idesconto):
        self.cliente = cliente
        self.desconto = desconto
        self.valor_original = 0.0
    
    def total(self, valor) -> float:
      self.valor_original = valor
      return self.valor_original - self.desconto.calcular(self.valor_original)
    
if __name__ == "__main__":
        pedido_normal = Pedido(DescontoNormal())
        print(pedido_normal.total(100))
        
        pedido_vip = Pedido(DescontoVip())
        print(pedido_vip.total(100))
        
        pedido_premium = Pedido(DescontoPremium())
        print(pedido_premium.total(100))
