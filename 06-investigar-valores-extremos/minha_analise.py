"""Exercício da aula «Investigar valores extremos»: um 45 no meio das porções.

Rode de dentro da pasta da aula:  python3 minha_analise.py
Escreva o seu código embaixo de cada tarefa. As respostas em texto vão no minhas-respostas.md.
"""
import pandas as pd

medidas = pd.read_csv("../dados/nutricao/medidas.csv")
participantes = pd.read_csv("../dados/nutricao/participantes.csv")
postos = pd.read_csv("../dados/nutricao/postos.csv")
print(f"{len(medidas)} medidas de {medidas['id_participante'].nunique()} pessoas")

# Tarefa 1: depois das contas à mão, rode as mesmas medidas nos nove valores.
nove = pd.Series([2.0, 2.5, 3.0, 3.0, 3.5, 4.0, 4.5, 5.0, 32.0])


# Tarefa 2: a cerca de 1,5 IQR e |z| > 3 em cada semana; na semana 12, de novo sem o 45.


# Tarefa 3: as duas medidas de cada pessoa marcada.


# Tarefa 4: a mudança média de cada grupo nos três cenários.
