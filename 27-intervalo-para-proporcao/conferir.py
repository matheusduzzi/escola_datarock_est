"""Testa a sua função proporcao_da_coluna antes de usar nas entregas de maio.

    python3 conferir.py                    # testa minha_solucao.py, nessa pasta
    python3 conferir.py outro_arquivo.py   # testa outro arquivo

Os testes usam as 48 entregas de março da aula e casos pequenos montados à mão.
Nenhum teste usa as entregas de maio: os números de maio são você que descobre.
Sai com código 0 quando tudo passa e 1 quando algum teste falha.
"""
import csv
import importlib.util
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent


def carregar(arquivo):
    spec = importlib.util.spec_from_file_location("solucao_do_aluno", arquivo)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.proporcao_da_coluna


def comparar(r, esperado):
    for chave, valor in esperado.items():
        if chave not in r:
            return f"faltou a chave {chave!r}"
        if isinstance(valor, int):
            if r[chave] != valor:
                return f"{chave} deu {r[chave]}, esperado {valor}"
        elif round(r[chave], 4) != valor:
            return f"{chave} deu {round(r[chave], 4)}, esperado {valor}"
    return ""


def main():
    arquivo = Path(sys.argv[1]) if len(sys.argv) > 1 else PASTA / "minha_solucao.py"
    try:
        funcao = carregar(arquivo)
    except Exception as erro:  # o arquivo pode nem abrir; o aluno precisa ver o motivo
        print(f"não consegui carregar proporcao_da_coluna de {arquivo.name}: {erro!r}")
        return 1

    with open(PASTA.parent / "dados" / "loja" / "entregas.csv", encoding="utf-8") as f:
        marco = [linha["horas"] for linha in csv.DictReader(f)]

    casos = [
        ("março até 48 horas, como na aula", marco,
         {"ate": 26, "n": 45, "vazias": 3, "p": 0.5778, "inferior": 0.433, "superior": 0.7103}),
        ("48 horas cravadas contam como até 48", ["48", "48.0", "50"],
         {"ate": 2, "n": 3, "vazias": 0, "p": 0.6667, "inferior": 0.2077, "superior": 0.9385}),
        ("vazio, célula só com espaços e None ficam fora do numerador e do denominador",
         ["", "  ", None, "10", "60"],
         {"ate": 1, "n": 2, "vazias": 3, "p": 0.5, "inferior": 0.0945, "superior": 0.9055}),
        ("nenhuma até o limite: a faixa começa em zero, mas não termina em zero", ["50", "60", "70"],
         {"ate": 0, "n": 3, "vazias": 0, "p": 0.0, "inferior": 0.0, "superior": 0.5615}),
        ("zero é número, e todas até o limite: a faixa termina em 100%", ["0", "12"],
         {"ate": 2, "n": 2, "vazias": 0, "p": 1.0, "inferior": 0.3424, "superior": 1.0}),
    ]
    falhas = 0
    for nome, valores, esperado in casos:
        copia = list(valores)
        try:
            r = funcao(valores, 48)
            problema = comparar(r, esperado)
        except Exception as erro:
            problema = f"deu erro: {erro!r}"
        if not problema and valores != copia:
            problema = "a função mudou a lista que recebeu"
        print(("ok    " if not problema else "FALHA ") + nome + ("" if not problema else f": {problema}"))
        falhas += bool(problema)

    for nome, valores in [("só vazias", ["", " ", None]), ("lista vazia", [])]:
        try:
            r = funcao(valores, 48)
            problema = f"era para dar ValueError e retornou {r!r}"
        except ValueError:
            problema = ""
        except Exception as erro:
            problema = f"era para dar ValueError e deu {erro!r}"
        print(("ok    " if not problema else "FALHA ") + nome + ("" if not problema else f": {problema}"))
        falhas += bool(problema)

    if falhas:
        print(f"{falhas} teste(s) falharam")
        return 1
    print("tudo certo")
    return 0


if __name__ == "__main__":
    sys.exit(main())
