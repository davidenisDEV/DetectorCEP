# DetectorCEP

Este projeto é um script Python que utiliza a biblioteca `pycep` para obter informações detalhadas de um CEP (Código de Endereçamento Postal) fornecido pelo usuário. 

## Funcionalidades

- Solicita ao usuário a entrada de um CEP.
- Utiliza a biblioteca `pycep` para buscar informações sobre o CEP.
- Exibe as informações encontradas, como CEP, UF, cidade, bairro e rua.

## Requisitos

- Python 3.6 ou superior
- Biblioteca `pycep`

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/davidenisDEV/DetectorCEP.git

   
### Navegue até o diretório do projeto:
```bash
cd DetectorCEP
```
### Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
### Instale a biblioteca pycep:
```bash
pip install pycep
```
### Uso
Execute o script main.py:
```bash
python main.py
```
Digite os 8 dígitos do seu CEP e script irá exibir as informações relacionadas ao CEP fornecido.
### Exemplo
```bash
Digite os 8 digitos do seu CEP: 01234567
CEP: 01234567
UF: XX
Cidade: XXXXXXX
Bairro: XXXXXXXXX
Rua: XXXXXXXXXXXX
```
### Estrutura do Projeto
```bash
detector-cep/
│
├── main.py          # Script principal que executa a funcionalidade do projeto
├── README.md        # Este arquivo README
``` 
