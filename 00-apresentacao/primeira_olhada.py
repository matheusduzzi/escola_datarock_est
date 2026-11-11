# Primeira olhada: a pergunta da Dani sobre o prazo de 48 horas.
# Rode de dentro da pasta 00-apresentacao:  python3 primeira_olhada.py
#
# Três passos com as mesmas 48 entregas: descrever o que aconteceu, estimar quanto
# isso pode variar de um mês para outro e só então olhar a decisão.
# O sorteio do passo 3 usa um número fixo (2026) para a saída sair igual em toda máquina.
import numpy as np
import pandas as pd


def br(numero, casas=1):
    return f"{numero:.{casas}f}".replace(".", ",")


entregas = pd.read_csv("../dados/loja/entregas.csv")
horas = entregas["horas"].dropna()
sem_baixa = len(entregas) - len(horas)
acima = int((horas > 48).sum())

print("1. Descrever: o que aconteceu nas entregas do mês")
print(f"   {len(entregas)} entregas, {len(horas)} com baixa anotada, {sem_baixa} sem baixa")
print(f"   média {br(horas.mean())} h   mediana {br(horas.median())} h")
print(f"   passaram de 48 h: {acima} de {len(horas)} ({br(acima / len(horas) * 100)}%)")

print("2. As 3 sem baixa")
print(f"   se todas chegaram em até 48 h: {acima} de {len(entregas)} ({br(acima / len(entregas) * 100)}%)")
print(f"   se todas passaram de 48 h: {acima + sem_baixa} de {len(entregas)} "
      f"({br((acima + sem_baixa) / len(entregas) * 100)}%)")

print("3. Inferir: 10 mil meses sorteados a partir das 45 entregas")
sorteio = np.random.default_rng(2026)
pct, medias = [], []
for _ in range(10_000):
    mes = sorteio.choice(horas.to_numpy(), size=len(horas), replace=True)
    pct.append((mes > 48).mean() * 100)
    medias.append(mes.mean())
p_baixo, p_alto = np.percentile(pct, [2.5, 97.5])
m_baixo, m_alto = np.percentile(medias, [2.5, 97.5])
print(f"   média entre {br(m_baixo)} h e {br(m_alto)} h em 95% dos meses")
print(f"   acima de 48 h entre {br(p_baixo)}% e {br(p_alto)}% em 95% dos meses")

print("4. Decidir: que prazo as entregas de fato cumprem")
for prazo in (48, 54, 60):
    passou = int((horas > prazo).sum())
    print(f"   prometer {prazo} h: {passou} de {len(horas)} acima do prazo ({br(passou / len(horas) * 100)}%)")
