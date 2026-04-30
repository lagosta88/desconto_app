from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService

class PedidoController:
    def __init__(self, service:PedidoService):
        self.service = service

    def criar_pedido(self, pedido: Pedido):
        self.service.adicionar_pedido(pedido)

    def processar_pedidos(self):
        self.service.processar_pedidos()