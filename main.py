from src.models.pedido import Pedido
from src.models.desconto import  DescontoVip, DescontoNormal, DescontoPremium
from src.services.pedido_service import PedidoService 

"""
if __name__ == "__main__":
    pedido = Pedido("Leonardo", DescontoVip())

    valor_final = pedido.valor_final(100)
    print(f"cliente: {pedido.cliente}")
    print(f"Valor final do pedido: {valor_final}")
    """

if __name__ == "__main__":
    
    service = PedidoService()
    
    pedido1 = Pedido("Leonardo", DescontoNormal())
    pedido1.valor_original = 100.0
    pedido2 = Pedido("Maria", DescontoVip())
    pedido2.valor_original = 200.0
    pedido3 = Pedido("João", DescontoPremium())
    pedido3.valor_original = 300.0


    service.adicionar_pedido(pedido1)
    service.adicionar_pedido(pedido2)
    service.adicionar_pedido(pedido3)

    service.processar_pedidos()
