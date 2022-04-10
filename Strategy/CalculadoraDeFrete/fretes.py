class MercadoLivre(object):
    def calcula(frete, peso, distancia):
        valor = distancia * peso * 0.2
        return frete.valor(valor)

class DHL(object):
    def calcula(frete, peso, distancia):
        valor = distancia * peso * 0.1
        return frete.valor(valor)
        
class Log(object):
    def calcula(frete, peso, distancia):
        valor = distancia * peso * 0.02
        return frete.valor(valor)
        