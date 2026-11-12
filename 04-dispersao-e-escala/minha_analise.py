"""Exercício da aula «Dispersão e escala»: dois fornecedores com o mesmo prazo.

Rode de dentro da pasta da aula:  python3 minha_analise.py
Escreva o seu código embaixo de cada tarefa. As respostas em texto vão no minhas-respostas.md.
"""
import pandas as pd

reposicoes = pd.read_csv("dados/reposicoes.csv")
contagem = reposicoes["fornecedor"].value_counts()
print(f"{len(reposicoes)} pedidos: norte {contagem['norte']}, leste {contagem['leste']}")

# Tarefa 1: depois das contas à mão, rode as mesmas medidas nos cinco prazos.
prazos = pd.Series([6, 8, 10, 12, 14])


# Tarefa 2: as medidas de cada fornecedor na coluna dias.


# Tarefa 3: o CV que o Léo pediu (Leste, dias e caixas) e o que a Carla pediu (diferenca).
