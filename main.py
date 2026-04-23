from src.models.pedido import Pedido
from src.models.desconto import  DescontoVip, DescontoNormal, DescontoPremium
from src.repositories.pedido_repository import PedidoRepository
from src.services.pedido_service import PedidoService
from src.controllers.pedido_controller import PedidoController
from src.database.connection import DatabaseConnection

"""
if __name__ == "__main__":
    pedido = Pedido("Leonardo", DescontoVip())

    valor_final = pedido.valor_final(100)
    print(f"cliente: {pedido.cliente}")
    print(f"Valor final do pedido: {valor_final}")
    """

if __name__ == "__main__":
    database = DatabaseConnection()
    
    repo = PedidoRepository(database)
    
    pedido1 = Pedido("Leonardo", DescontoNormal())
    pedido1.valor_original = 100.0
    pedido2 = Pedido("Maria", DescontoVip())
    pedido2.valor_original = 200.0
    pedido3 = Pedido("João", DescontoPremium())
    pedido3.valor_original = 300.0


    repo.adicionar_pedido(pedido1)
    repo.adicionar_pedido(pedido2)
    repo.adicionar_pedido(pedido3)

    pedidos = repo.listar_pedidos()

    for pedido in pedidos:
        print(f"Cliente: {pedido.cliente}")
        print(f"Valor Final: {pedido.valor_final(pedido.valor_original)}")
