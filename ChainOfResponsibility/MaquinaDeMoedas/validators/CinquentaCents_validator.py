from .interface import ValidatorInterface

class CinquentaValidator(ValidatorInterface):
    def validate(self,moeda: str)-> bool:
        if moeda == '50': return True
        return False
    
    def action(self) -> None:
        print(10*'==')
        print('->50 centavos armazenados no slot de 50 centavos!')

