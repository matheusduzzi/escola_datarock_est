"""Gera piloto_abril.csv, as 40 entregas de abril do exercício da aula «Margem de erro e sensibilidade».

    python3 gerar_dados.py

Abra este arquivo só depois de fazer o exercício: o começo dele conta como os tempos e as baixas
que faltam foram sorteados.

Como o sorteio funciona:
- cada entrega é da capital com chance de 2/3 e do interior com chance de 1/3;
- na capital, o tempo segue uma normal de média 42 horas e desvio 5; no interior, média 55 e desvio 6;
- a baixa fica sem anotar com chance de 5% quando a entrega leva até 48 horas e de 30% quando passa disso.
É o mesmo mundo da seção 8 da aula. O número fixo do sorteio faz o arquivo sair igual toda vez.
"""
import csv
import random
from pathlib import Path

PASTA = Path(__file__).resolve().parent


def gerar():
    rng = random.Random(2831)
    linhas = []
    for i in range(1, 41):
        regiao = "capital" if rng.random() < 2 / 3 else "interior"
        horas = round(rng.gauss(42, 5) if regiao == "capital" else rng.gauss(55, 6), 1)
        sem_baixa = rng.random() < (0.05 if horas <= 48 else 0.30)
        linhas.append({"id_entrega": str(i), "regiao": regiao, "horas": "" if sem_baixa else f"{horas:.1f}"})
    return linhas


def main():
    linhas = gerar()
    with open(PASTA / "piloto_abril.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id_entrega", "regiao", "horas"], lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)
    capital = sum(1 for l in linhas if l["regiao"] == "capital")
    vazias = sum(1 for l in linhas if l["horas"] == "")
    print(f"abril={len(linhas)} capital={capital} interior={len(linhas) - capital} sem_baixa={vazias}")


if __name__ == "__main__":
    main()
