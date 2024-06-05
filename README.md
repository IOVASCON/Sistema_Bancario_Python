# Sistema Bancário com Interface Gráfica

Este projeto implementa um sistema bancário simples com operações de depósito, saque e extrato usando a linguagem Python e a biblioteca `tkinter` para a interface gráfica.

## Funcionalidades

- **Depositar**: Permite ao usuário adicionar fundos à conta.
- **Sacar**: Permite ao usuário retirar fundos da conta, respeitando limites diários e de saldo.
- **Extrato**: Exibe todas as movimentações da conta e o saldo atual.
- **Sair**: Sai do aplicativo.

## Estrutura do Projeto

Sistema_Bancario_Python/
├── apoio/
│ └── README.md
├── codigo-fonte/
│ ├── README.md
│ └── sistema_bancario_gui_comentado.py
├── doc/
│ └── README.md
├── tests/
│ └── README.md
└── README.md


- `apoio/`: Pasta para arquivos de apoio.
- `codigo-fonte/`: Contém o código fonte do projeto.
- `doc/`: Documentação do projeto.
- `tests/`: Testes para o projeto.
- `README.md`: Arquivo com informações sobre o projeto.

## Instalação

Certifique-se de ter o Python instalado em sua máquina. Este projeto foi desenvolvido usando Python 3. Se ainda não tiver o Python, você pode baixá-lo e instalá-lo a partir do [site oficial do Python](https://www.python.org/).

### Verificando a Instalação do `tkinter`

`tkinter` geralmente vem pré-instalado com Python, mas você pode verificar se ele está instalado executando o seguinte script no terminal:

```python
import tkinter as tk

root = tk.Tk()
root.title("Teste Tkinter")
label = tk.Label(root, text="Tkinter está instalado!")
label.pack()
root.mainloop()

Se uma janela aparecer com a mensagem "Tkinter está instalado!", então está tudo pronto.

## Execução do Projeto

1. Clone o repositório:
git clone https://github.com/IOVASCON/Sistema_Bancario_Python.git

2. Navegue até o diretório do projeto:
cd Sistema_Bancario_Python/codigo-fonte

3. Execute o script Python:
python sistema_bancario_gui.py

## Uso
### Interface Gráfica

    Valor: Campo de entrada para o valor das operações.
    Depositar: Botão para realizar depósitos.
    Sacar: Botão para realizar saques.
    Extrato: Botão para exibir o extrato da conta.

## Contribuição

Se você deseja contribuir com este projeto, sinta-se à vontade para fazer um fork do repositório, criar um branch, adicionar suas alterações e enviar um pull request.
Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
Nota: Este projeto foi criado como parte de um desafio proposto pela empresa educadora DIO para implementar um sistema bancário básico usando Python e tkinter
Autor
Izairton Oliveira de Vasconcelos