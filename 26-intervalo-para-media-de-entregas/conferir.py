"""Testa a sua função intervalo_da_coluna antes de usar nas entregas de abril.

    python3 conferir.py                    # testa minha_solucao.py, nessa pasta
    python3 conferir.py outro_arquivo.py   # testa outro arquivo

Os testes usam as 48 entregas de março da aula e casos pequenos montados à mão.
Nenhum teste usa as entregas de abril: os números de abril são você que descobre.
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
    return mod.intervalo_da_coluna


def perto(r, esperado):
    for chave, valor in esperado.items():
        if chave not in r:
            return f"faltou a chave {chave!r}"
        if isinstance(valor, int):
            if r[chave] != valor:
                return f"{chave} deu {r[chave]}, esperado {valor}"
        elif round(r[chave], 2) != valor:
            return f"{chave} deu {round(r[chave], 2)}, esperado {valor}"
    return ""


def main():
    arquivo = Path(sys.argv[1]) if len(sys.argv) > 1 else PASTA / "minha_solucao.py"
    try:
        funcao = carregar(arquivo)
    except Exception as erro:  # o arquivo pode nem abrir; o aluno precisa ver o motivo
        print(f"não consegui carregar intervalo_da_coluna de {arquivo.name}: {erro!r}")
        return 1

    with open(PASTA.parent / "dados" / "loja" / "entregas.csv", encoding="utf-8") as f:
        marco = [linha["horas"] for linha in csv.DictReader(f)]

    casos = [
        ("março, como na aula (t = 2,015)", marco, 2.015,
         {"n": 45, "vazias": 3, "media": 46.10, "inferior": 43.92, "superior": 48.27}),
        ("vazio e célula só com espaços contam como vazias", ["30", "", "40", "  ", "50"], 4.303,
         {"n": 3, "vazias": 2, "media": 40.0, "inferior": 15.16, "superior": 64.84}),
        ("zero é número, None é vazio", ["0", "10", None], 12.706,
         {"n": 2, "vazias": 1, "media": 5.0, "inferior": -58.53, "superior": 68.53}),
    ]
    falhas = 0
    for nome, valores, t, esperado in casos:
        copia = list(valores)
        try:
            r = funcao(valores, t)
            problema = perto(r, esperado)
        except Exception as erro:
            problema = f"deu erro: {erro!r}"
        if not problema and valores != copia:
            problema = "a função mudou a lista que recebeu"
        print(("ok    " if not problema else "FALHA ") + nome + ("" if not problema else f": {problema}"))
        falhas += bool(problema)

    for nome, valores in [("só vazias", ["", " "]), ("um valor só", ["7", ""])]:
        try:
            r = funcao(valores, 12.706)
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
