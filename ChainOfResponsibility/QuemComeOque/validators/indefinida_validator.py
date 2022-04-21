from .interface import ValidatorInterface

class IndefinidaValidator(ValidatorInterface):
    def validate(self,comida: str)-> bool:
        if comida == 'Indefinida': return True
        return False
    
    def action(self) -> None:
        print('O Leão come a Indefinida!')

