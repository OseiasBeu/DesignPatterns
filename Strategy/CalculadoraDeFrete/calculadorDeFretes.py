import fretes

class Calculadora_de_Fretes(object):
    def realiza_calculo(self,fretes,valor_frete,peso,distancia):
        frete_calculado = fretes.calcula(valor_frete,peso,distancia)
        print(f'Valor de frete é:{frete_calculado}')

if __name__ == '__main__':
    from valorFrete import Frete
    calculador = Calculadora_de_Fretes()
    valor_frete = Frete()
    distancia = 10
    peso = 30


    calculador.realiza_calculo(fretes.MercadoLivre,valor_frete, peso,distancia)
    calculador.realiza_calculo(fretes.DHL,valor_frete, peso,distancia)
    calculador.realiza_calculo(fretes.Log,valor_frete, peso,distancia)

