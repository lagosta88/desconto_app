from src.models.pedido import Pedido

class PedidoService:
    def __init__(self,repository):
        self.repository = repository

    def adicionar_pedido(self, pedido: Pedido):
        self.repository.adicionar_pedido(pedido)

    def  processar_pedidos(self):
        pedido = self.repository.listar_pedidos()
        for pedido in self.pedidos: 
            print(f"Pedido para {pedido.cliente}")
            print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")    

