import juros

class Calculadora_de_Juros(object):

    def realiza_calculo(self,valor_juros,juros,periodo):
        juros_calculado = juros.calcula(valor_juros,periodo)
        print(f'Juros de:{juros_calculado}% ao dia.')

if __name__ == '__main__':
    from valor_juros import Juros
    calculador = Calculadora_de_Juros()
    valor_juros = Juros(500)

    calculador.realiza_calculo(valor_juros,juros.Bradesco,1)
    calculador.realiza_calculo(valor_juros,juros.Itau,1)
    calculador.realiza_calculo(valor_juros,juros.Santander,1)
    calculador.realiza_calculo(valor_juros,juros.Nubank,1)
