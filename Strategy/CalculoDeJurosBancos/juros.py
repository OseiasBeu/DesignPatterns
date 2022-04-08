class Bradesco(object):
    def calcula(montante,periodo):
        return (montante.valor*periodo*0.1)/100

class Itau(object):
    def calcula(montante,periodo):
        return (montante.valor*periodo*0.2)/100

class Santander(object):
    def calcula(montante,periodo):
        return (montante.valor*periodo*0.02)/100

class Nubank(object):
    def calcula(montante,periodo):
        return (montante.valor*periodo*0.22)/100
