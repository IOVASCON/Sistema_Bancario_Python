"""
Sistema Bancário com Interface Gráfica

Este programa implementa um sistema bancário simples com operações de depósito,
saque e extrato usando a biblioteca tkinter para a interface gráfica.

Funções principais:
- Depositar: Permite ao usuário adicionar fundos à conta.
- Sacar: Permite ao usuário retirar fundos da conta, respeitando limites diários e de saldo.
- Extrato: Exibe todas as movimentações da conta e o saldo atual.

Autor: Izairton Oliveira de Vasconcelos
Data: 05/06/2024
"""


"""
Explicação dos Comentários:

    Resumo no Início do Código:
        Descreve o objetivo do programa e as funcionalidades principais.
        Segue as recomendações do PEP8 para documentação e boas práticas.

    Importação de Módulos:
        Explica a importação das bibliotecas necessárias (tkinter e messagebox).

    Variáveis Globais:
        Descreve as variáveis usadas para gerenciar o estado da conta bancária.

    Funções:
        Cada função (depositar, sacar, mostrar_extrato) é comentada para explicar sua finalidade e funcionamento.

    Configuração da Interface Gráfica:
        Explica a criação da janela principal, frame e widgets (rótulos, campos de entrada, botões).
        Cada widget é comentado para descrever sua criação e posicionamento na interface gráfica.

Como Executar:

    Salve o Código:
        Salve o código em um arquivo Python, por exemplo, sistema_bancario_gui_comentado.py.
"""

import tkinter as tk
from tkinter import messagebox

# Variáveis globais para gerenciar o estado da conta bancária
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite máximo para saques
extrato = ""  # Histórico das movimentações
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Número máximo de saques permitidos por dia

def depositar():
    """
    Função para realizar depósito na conta bancária.
    """
    global saldo, extrato  # Declaração de uso das variáveis globais
    valor = float(entry_valor.get())  # Obtém o valor informado pelo usuário
    if valor > 0:
        saldo += valor  # Atualiza o saldo
        extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra o depósito no extrato
        messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Valor inválido para depósito.")  # Informa erro se o valor for inválido
    entry_valor.delete(0, tk.END)  # Limpa o campo de entrada

def sacar():
    """
    Função para realizar saque na conta bancária.
    """
    global saldo, extrato, numero_saques  # Declaração de uso das variáveis globais
    valor = float(entry_valor.get())  # Obtém o valor informado pelo usuário
    excedeu_saldo = valor > saldo  # Verifica se o valor excede o saldo disponível
    excedeu_limite = valor > limite  # Verifica se o valor excede o limite permitido
    excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o número de saques diários foi excedido

    if excedeu_saldo:
        messagebox.showerror("Erro", "Saldo insuficiente.")  # Informa erro se o saldo for insuficiente
    elif excedeu_limite:
        messagebox.showerror("Erro", "Valor do saque excede o limite.")  # Informa erro se o valor exceder o limite
    elif excedeu_saques:
        messagebox.showerror("Erro", "Número máximo de saques excedido.")  # Informa erro se o número de saques for excedido
    elif valor > 0:
        saldo -= valor  # Atualiza o saldo
        extrato += f"Saque: R$ {valor:.2f}\n"  # Registra o saque no extrato
        numero_saques += 1  # Incrementa o contador de saques
        messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Valor inválido para saque.")  # Informa erro se o valor for inválido
    entry_valor.delete(0, tk.END)  # Limpa o campo de entrada

def mostrar_extrato():
    """
    Função para exibir o extrato da conta bancária.
    """
    global saldo, extrato  # Declaração de uso das variáveis globais
    extrato_texto = "Não foram realizadas movimentações." if not extrato else extrato  # Define o texto do extrato
    extrato_texto += f"\nSaldo: R$ {saldo:.2f}"  # Adiciona o saldo atual ao extrato
    messagebox.showinfo("Extrato", extrato_texto)  # Exibe o extrato em uma caixa de mensagem

# Configuração da interface gráfica
root = tk.Tk()  # Cria a janela principal
root.title("Sistema Bancário")  # Define o título da janela

frame = tk.Frame(root)  # Cria um frame para organizar os widgets
frame.pack(padx=10, pady=10)  # Adiciona o frame à janela principal com padding

# Criação dos widgets
label_valor = tk.Label(frame, text="Valor:")  # Cria um rótulo para o campo de valor
label_valor.grid(row=0, column=0, padx=5, pady=5)  # Posiciona o rótulo na grade

entry_valor = tk.Entry(frame)  # Cria um campo de entrada para o valor
entry_valor.grid(row=0, column=1, padx=5, pady=5)  # Posiciona o campo de entrada na grade

button_depositar = tk.Button(frame, text="Depositar", command=depositar)  # Cria um botão para depósito
button_depositar.grid(row=1, column=0, padx=5, pady=5)  # Posiciona o botão na grade

button_sacar = tk.Button(frame, text="Sacar", command=sacar)  # Cria um botão para saque
button_sacar.grid(row=1, column=1, padx=5, pady=5)  # Posiciona o botão na grade

button_extrato = tk.Button(frame, text="Extrato", command=mostrar_extrato)  # Cria um botão para exibir o extrato
button_extrato.grid(row=2, column=0, columnspan=2, padx=5, pady=5)  # Posiciona o botão na grade

root.mainloop()  # Inicia o loop principal da interface gráfica
