# Tarefa 4 do diagnóstico: leia tudo e anote a saída antes de rodar.
import pandas as pd

tiquetes = pd.Series([80.0, 95.0, 100.0, 110.0, 120.0, 135.0, 2400.0])
media = tiquetes.mean()
mediana = tiquetes.median()
acima = int((tiquetes > media).sum())
print(len(tiquetes), round(float(media), 2), float(mediana), acima)

sem_maior = tiquetes[tiquetes < 1000]
print(round(float(sem_maior.mean()), 2), float(sem_maior.median()))
