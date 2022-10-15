from pessoa import Pessoa


class PessoaF(Pessoa):

    def __init__(self, nome, remuneracaoAnual):
        Pessoa.__init__(self, nome)
        self.remunecaraoAnual = remuneracaoAnual

    def calcularIr(self):
        return self.remunecaraoAnual * 0.15
