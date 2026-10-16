Sistema de controle de gastos pessoais no terminal, feito em Python utilizando o VS code.
As funções criadas (funcoes.py) foram para facilitar e diminuir o programa principal (main.py)
Funções: 
def leiaInt():
  Serve para ler e validar apenas números inteiros, usada para validar as opções do menu;
def menu(lista):
  Serve para criar a lista com opçõs que o menu oferece para o controle de gastos;
def salvar_dados(transacoes):
  Serve para criar uma lista contendo um dicionário com todas as transações registradas pelo usuário;
def carregar_dados():
  Serve para trazer essa lista com as transações guardadas e mostrar ao usuário;
--> Dia 30/09/2026 fiz a parte 3 que mostrar o saldo.
def calacular_saldo(transacoes)
  Serve para que se o 'tipo' for 'ENTRADA' ele soma o 'valor' ao saldo e se for 'tipo' 'SAIDA' ele subtraia o'valor' do saldo
--> Dia 05/10/2026 criei uma função para mostrar melhor as transações:
def mostrar_transacoes(transacoes)
   Agora é apresentado em tabelas organizadas por: TIPO, VALOR e CATEGORIA
--> Dia 10/10/2026 terminaei a função 4 que mostra o total por categoria, com isso finaliza a Versão 1(V1) do meu projeto!
def total_por_categoria
  Mostra o valor seja positivo ou negativo por categoria
--> Dia 16/10/2026 V2 em progresso, já criei a opção de perguntar e guardar a data das trasnsações, já coloquei ela na função mostrar_transacoes(transacoes) de forma formatada em DD/MM/AAAA.
def leia_data()
  pergunta a data e guarda no arquivo entardas.

Programa em desenvolvimento: Meu próximo passo agora é remover e editar uma transação e depois filtrar ou resumir por mês.
