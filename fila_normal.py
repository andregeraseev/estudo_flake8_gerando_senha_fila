from fila_base import Filabase

class FinalNormal(Filabase):
    def gerasenhaatual(self)->None:
        self.senhaatual = f'NM{self.codigo}'

    def atualizafila(self)->None:
        self.reseta_fila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)
    def chamacliente(self, caixa:str)->str:
        cliente_atual :int = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return(f'cliente atual {cliente_atual} dirija-se ao caixa {caixa}')

