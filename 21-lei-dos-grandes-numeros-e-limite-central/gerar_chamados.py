"""Gera chamados_outubro.csv: a espera de 300 chamados do chat da Loja Exemplo em outubro.

Só biblioteca padrão. Sai igual toda vez.

    python3 gerar_chamados.py

Cada espera, em minutos, do cliente abrir o chat até a primeira resposta, sai de uma
distribuição exponencial com média de 8 minutos, com uma casa decimal.
"""
import csv
import math
import random

N, MEDIA = 300, 8.0


def main():
    rng = random.Random(1001)
    esperas = [round(-MEDIA * math.log(1 - rng.random()), 1) for _ in range(N)]
    with open("chamados_outubro.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["id_chamado", "minutos"])
        w.writerows([i + 1, f"{m:.1f}"] for i, m in enumerate(esperas))
    print(f"chamados={N} menor={min(esperas)} maior={max(esperas)}")


if __name__ == "__main__":
    main()
