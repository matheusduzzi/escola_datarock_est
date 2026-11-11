# Tarefa 3 do diagnóstico: entregas de março por região.
# Rode de dentro da pasta 00-apresentacao:  python3 tarefa3.py
import pandas as pd

entregas = pd.read_csv("dados/entregas_marco.csv")
print(entregas.head())

# Monte aqui a tabela com uma linha por região e as colunas
# regiao, entregas, sem_baixa, media_horas e ate_48h_pct.
# Guarde a tabela final na variável resultado e mostre com print(resultado).
