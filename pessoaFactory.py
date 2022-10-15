from pessoa import TipoPessoa, Pessoa

from pf import PessoaF
from pj import PessoaJ


class PessoaFactory:

    @staticmethod
    def create(tipo: TipoPessoa, nome, remuneracaoAnual) -> Pessoa:
        if tipo == TipoPessoa.PESSOA_FISICA:
            return PessoaF(nome, remuneracaoAnual)

        if tipo == TipoPessoa.PESSOA_JURIDICA:
            return PessoaJ(nome, remuneracaoAnual)

        return None
