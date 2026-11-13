"""O que muda nas entregas de março quando três baixas faltam.

Rode de dentro da pasta da aula:  python3 vazios.py
Lê ../dados/loja/entregas.csv. Só precisa do pandas.
"""
import argparse
from pathlib import Path

import pandas as pd

PRAZO = 48


def br(x, casas=1):
    return f"{x:.{casas}f}".replace(".", ",")


def pct(a, b):
    return f"{a} de {b} ({br(100 * a / b)}%)"


def main():
    padrao = Path(__file__).resolve().parent.parent / "dados" / "loja" / "entregas.csv"
    p = argparse.ArgumentParser(description="Entregas sem baixa: o que muda na média e no prazo.")
    p.add_argument("--arquivo", default=str(padrao))
    args = p.parse_args()
    entregas = pd.read_csv(args.arquivo)
    if "horas" not in entregas.columns:
        raise SystemExit(f"{args.arquivo} não tem a coluna horas")
    horas = entregas["horas"]
    vazias = entregas.loc[horas.isna(), "id_entrega"].tolist()
    n, com = len(entregas), int(horas.count())
    sem = n - com
    acima = int((horas > PRAZO).sum())

    print(f"Entregas: {n} linhas")
    print(f"Com baixa: {com} | sem baixa: {sem} (ids {', '.join(map(str, vazias))})")
    print()
    print("O que o pandas faz sozinho")
    print(f"  len(entregas)        {n}")
    print(f"  horas.count()        {com}")
    print(f"  horas.mean()         {br(horas.mean())} h  (média das {com} com baixa)")
    print(f"  horas.dropna()       {len(horas.dropna())} linhas")
    print()
    print(f"Acima de {PRAZO} h")
    print(f"  entre as {com} com baixa     {pct(acima, com)}")
    print(f"  nas {n}, sem chutar nada   de {pct(acima, n)} a {pct(acima + sem, n)}")
    print()
    print(f"Se as {sem} sem baixa levaram...   média das {n}   acima de {PRAZO} h")
    for rotulo, valor in [("as mesmas horas que as outras", None), ("24 h cada", 24), ("48 h cada", 48),
                          ("72 h cada", 72), ("96 h cada", 96)]:
        if valor is None:
            media, conta = horas.mean(), pct(acima, com)
        else:
            cheio = horas.fillna(valor)
            media, conta = cheio.mean(), pct(int((cheio > PRAZO).sum()), n)
        print(f"  {rotulo:<30}{br(media):>8} h     {conta}")
    soma = PRAZO * n - horas.sum()
    print()
    print(f"A média das {n} passa de {PRAZO} h se as {sem} somarem mais de {br(soma)} h "
          f"({br(soma / sem)} h cada, em média).")
    print()
    print("Trocar o vazio por um número")
    print(f"  fillna(0)            média {br(horas.fillna(0).mean())} h, desvio {br(horas.fillna(0).std())} h")
    print(f"  fillna(média)        média {br(horas.fillna(horas.mean()).mean())} h, "
          f"desvio {br(horas.fillna(horas.mean()).std())} h")
    print(f"  só as {com} com baixa   média {br(horas.mean())} h, desvio {br(horas.std())} h")


if __name__ == "__main__":
    main()
