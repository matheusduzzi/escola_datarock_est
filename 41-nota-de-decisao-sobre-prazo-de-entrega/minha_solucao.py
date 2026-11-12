"""Exercício da aula «Nota de decisão sobre prazo de entrega»: a sua folha.

Escreva as duas funções no lugar do raise. Teste com:
    python3 conferir.py
Quando aparecer "tudo certo", rode no interior:
    python3 minha_solucao.py
Esse é o comando que vai na sua nota.
"""
import csv
import math


def wilson(k, n, z=1.96):
    """A faixa de Wilson da aula «Intervalo para proporção»: k sins em n."""
    p = k / n
    centro = (p + z**2 / (2 * n)) / (1 + z**2 / n)
    margem = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / (1 + z**2 / n)
    return centro - margem, centro + margem


def quadro_de_prazos(valores, prazos, minimo=0.90, z=1.96):
    """Uma linha por prazo, na ordem de `prazos`.

    `valores` é a coluna horas como veio do CSV: célula vazia, só com espaços ou None é
    entrega sem baixa. Cada linha é um dicionário com:
      prazo, ate (com baixa até o prazo, prazo incluído), n (com baixa), vazias, p (ate / n),
      inferior e superior (faixa de Wilson de ate em n),
      pior (começo da faixa de Wilson se as vazias passaram do prazo),
      melhor (fim da faixa de Wilson se as vazias chegaram no prazo),
      decisao: "mostrar" se pior >= minimo, "não mostrar" se melhor < minimo,
               "inconclusivo" no resto.
    Levanta ValueError sem nenhuma entrega com baixa e com minimo fora de 0 a 1.
    Não muda a lista que recebeu.
    """
    raise NotImplementedError("escreva a função quadro_de_prazos")


def prazo_para_mostrar(quadro):
    """O menor prazo do quadro com decisao "mostrar"; None se nenhum passa."""
    raise NotImplementedError("escreva a função prazo_para_mostrar")


def pct(x):
    return round(100 * x, 1)


def mostrar(titulo, valores, prazos):
    print(titulo)
    quadro = quadro_de_prazos(valores, prazos)
    for l in quadro:
        print(" ", l["prazo"], "h:", l["ate"], "de", l["n"], "com baixa,", l["vazias"], "sem baixa;",
              pct(l["p"]), "% de", pct(l["inferior"]), "a", pct(l["superior"]),
              "| pior", pct(l["pior"]), "melhor", pct(l["melhor"]), "->", l["decisao"])
    print("  prazo para mostrar:", prazo_para_mostrar(quadro))


if __name__ == "__main__":
    with open("interior_outubro.csv", encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))
    prazos = [72, 96, 120]
    mostrar("outubro inteiro", [l["horas"] for l in linhas], prazos)
    mostrar("a partir do dia 15", [l["horas"] for l in linhas if int(l["dia"]) >= 15], prazos)
