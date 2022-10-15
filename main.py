from pessoa import TipoPessoa

from pessoaFactory import PessoaFactory

if __name__ == '__main__':
    pfisica = PessoaFactory.create(TipoPessoa.PESSOA_FISICA, 'William', 10000.00)
    pjuridica = PessoaFactory.create(TipoPessoa.PESSOA_JURIDICA, '', 250000.00)
    nubank = PessoaFactory.create(TipoPessoa.PESSOA_JURIDICA, 'Nubank', 1000000.00)

    print("Digite 1 (um) para PJ e 2 (dois) para PF:")
    num = int(input("O numero escolhido é: "))

    match num:
        case 1:
             print(f'O valor do IR Pessoa Jurídica a ser recolhido é {pjuridica.calcularIr():.2f}')
        case 2:
             print(f'O valor do IR Pessoa Física a ser recolhido é {pfisica.calcularIr():.2f}')
        case 3:
             print(f'O valor do IR da {nubank.nome} a ser recolhido é {pjuridica.calcularIr():.2f}')
        case _:
            print("o número digitado não condiz com nenhuma opção. Reinicie o programa!!!")

