from pycep import PyCep

cep_input = input('Digite os 8 digitos do seu CEP: ')
cep = PyCep(cep_input)

retorno = cep.dadosCep

if retorno:
    cepDaRua = retorno['cep']
    print(f'CEP: {cepDaRua}')

    uf = retorno['uf']
    print(f'UF: {uf}')

    cidade = retorno['localidade']
    print(f'Cidade: {cidade}')

    bairro = retorno['bairro']
    print(f'Bairro: {bairro}')

    rua = retorno['logradouro']
    print(f'Rua: {rua}')
else:
    print('CEP não encontrado ou inválido.')