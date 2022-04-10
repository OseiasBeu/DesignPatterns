class Frete(object):
    def __init__(self):
        self.__valor = 0 
    # @property
    def valor(self, valor):
        self.__valor = valor
        return self.__valor

