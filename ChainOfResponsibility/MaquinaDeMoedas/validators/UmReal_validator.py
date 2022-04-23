from .interface import ValidatorInterface

class UmRealValidator(ValidatorInterface):
    def validate(self,moeda: str)-> bool:
        if moeda == '1': return True
        return False
    
    def action(self) -> None:
        print(10*'==')
        print('->1 Real armazenado no slot de 1 real!')

