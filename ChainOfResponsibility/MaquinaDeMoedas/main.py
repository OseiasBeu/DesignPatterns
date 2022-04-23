from validators import UmRealValidator,VinteECincoValidator, CinquentaValidator

class VarificaMoeda:
    def __init__(self) -> None:
        self.val = [
            UmRealValidator(),
            VinteECincoValidator(),
            CinquentaValidator(),
        ]


    def process(self, moeda: str):
        for v in self.val:
            if v.validate(moeda): return v.action()



verifcarMoeda = VarificaMoeda()
verifcarMoeda.process('1')
verifcarMoeda.process('25')
verifcarMoeda.process('50')
verifcarMoeda.process('1')
verifcarMoeda.process('1')
verifcarMoeda.process('25')

