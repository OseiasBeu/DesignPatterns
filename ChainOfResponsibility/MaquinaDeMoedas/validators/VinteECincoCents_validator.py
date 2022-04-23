from .interface import ValidatorInterface

class VinteECincoValidator(ValidatorInterface):
    def validate(self,moeda: str)-> bool:
        if moeda == '25': return True
        return False
    
    def action(self) -> None:
        print(10*'==')
        print('->25 centavos armazenados no slot de 25 centavos!')

