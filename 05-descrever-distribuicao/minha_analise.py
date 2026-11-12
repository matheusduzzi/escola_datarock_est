"""Exercício da aula «Descrever distribuição»: os pedidos do app e do WhatsApp.

Rode de dentro da pasta da aula:  python3 minha_analise.py
Escreva o seu código embaixo de cada tarefa. As respostas em texto vão no minhas-respostas.md.
Os gráficos você salva com fig.savefig, como no graficos.py.
"""
import pandas as pd

pedidos = pd.read_csv("dados/pedidos_canais_novos.csv")
contagem = pedidos["canal"].value_counts()
print(f"{len(pedidos)} pedidos: app {contagem['app']}, whatsapp {contagem['whatsapp']}")

# Tarefa 1: depois das contas à mão, rode os quartis do WhatsApp no pandas.


# Tarefa 2: o app. Quantis, contagem por faixa de R$ 20, números do boxplot e o histograma.


# Tarefa 3: o violino dos dois canais, com a mediana marcada.


# Tarefa 4: o diagnóstico vai no minhas-respostas.md.
