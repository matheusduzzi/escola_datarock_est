"""Gera os dois arquivos da aula «Poisson e geométrica» em dados/.

Rodar dentro da pasta dessa aula:  python3 gerar_dados.py
A saída é igual toda vez: o sorteio usa só random.Random(...).random().

chamados_outubro.csv: chamados do chat por hora, de 1 a 31 de outubro, das 8h às 19h
(a hora 19 vai das 19h às 20h). A chegada de chamados segue uma Poisson com média que muda
com a hora: 1,5 de manhã (8h a 11h), 5 à tarde (12h a 15h) e 2,5 no fim do dia (16h a 19h).
No sábado, 17 de outubro, o site ficou fora do ar das 14h às 17h, e os clientes abriram
chamados juntos: 22, 27 e 11 chamados a mais nessas três horas.

entregas_interior.csv: 300 pacotes da transportadora do interior. A transportadora tenta
até 3 vezes; depois da terceira falha, o pacote volta para a loja. Em 88 de cada 100
endereços a chance de entregar em cada tentativa é 0,88. Nos outros 12 (número da casa
faltando, portaria que não recebe), é 0,3 em cada tentativa.
"""
import csv
import math
import random
from pathlib import Path

PASTA = Path(__file__).resolve().parent / "dados"
MEDIA_HORA = {h: 1.5 for h in range(8, 12)} | {h: 5.0 for h in range(12, 16)} | {h: 2.5 for h in range(16, 20)}
QUEDA = {(17, 14): 22, (17, 15): 27, (17, 16): 11}


def poisson(rng, media):
    """Sorteia uma Poisson multiplicando números aleatórios até passar de e elevado a -media."""
    limite, k, produto = math.exp(-media), 0, rng.random()
    while produto > limite:
        k += 1
        produto *= rng.random()
    return k


def chamados():
    rng = random.Random(1710)
    linhas = []
    for dia in range(1, 32):
        for hora in range(8, 20):
            linhas.append((f"2026-10-{dia:02d}", hora, poisson(rng, MEDIA_HORA[hora]) + QUEDA.get((dia, hora), 0)))
    return linhas


def entregas():
    rng = random.Random(2026)
    linhas = []
    for i in range(1, 301):
        chance = 0.3 if rng.random() < 0.12 else 0.88
        tentativas, entregue = 0, 0
        while tentativas < 3 and not entregue:
            tentativas += 1
            entregue = 1 if rng.random() < chance else 0
        linhas.append((f"P{i:03d}", tentativas, entregue))
    return linhas


if __name__ == "__main__":
    PASTA.mkdir(exist_ok=True)
    for nome, cab, linhas in [("chamados_outubro.csv", ("data", "hora", "chamados"), chamados()),
                              ("entregas_interior.csv", ("pacote", "tentativas", "entregue"), entregas())]:
        with open(PASTA / nome, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(cab)
            w.writerows(linhas)
        print(f"dados/{nome}: {len(linhas)} linhas")
