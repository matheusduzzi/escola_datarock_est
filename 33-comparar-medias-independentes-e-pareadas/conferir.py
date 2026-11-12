"""Testa a sua função comparar_pareadas antes de usar na mesa de embalagem.

    python3 conferir.py                    # testa minha_solucao.py, nessa pasta
    python3 conferir.py outro_arquivo.py   # testa outro arquivo

Os testes usam casos pequenos montados à mão, com as contas da seção 6 da aula.
Nenhum teste usa embalagem.csv: os números da mesa nova são você que descobre.
Sai com código 0 quando tudo passa e 1 quando algum teste falha.
"""
import copy
import importlib.util
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent
sys.path.insert(0, str(PASTA))

QUATRO = [{"a": "10", "b": "8"}, {"a": "12", "b": "11"}, {"a": "9", "b": "8"}, {"a": "11", "b": "8"}]
INCOMPLETAS = [{"a": "13", "b": ""}, {"a": "", "b": "7"}, {"a": "  ", "b": "9"}, {"a": None, "b": "4"},
               {"a": "30", "b": None}]
ESPERADO = {"n": 4, "diferenca": 1.75, "baixo": 0.2265, "alto": 3.2735, "gl": 3, "dz": 1.8278, "dav": 1.254}


def carregar(arquivo):
    spec = importlib.util.spec_from_file_location("solucao_do_aluno", arquivo)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.comparar_pareadas


def comparar(r, esperado):
    if not isinstance(r, dict):
        return f"era para retornar um dicionário e retornou {r!r}"
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
        print(f"não consegui carregar comparar_pareadas de {arquivo.name}: {erro!r}")
        return 1

    casos = [
        ("quatro pares completos, faixa t de 95%", QUATRO, "a", "b", 0.95, ESPERADO),
        ("pares com um lado vazio, só com espaços ou None saem inteiros", QUATRO + INCOMPLETAS, "a", "b", 0.95,
         ESPERADO),
        ("faixa de 90% usa o t de 90%", QUATRO, "a", "b", 0.90,
         dict(ESPERADO, baixo=0.6234, alto=2.8766)),
        ("a diferença é a menos b: trocar as colunas troca o sinal", QUATRO, "b", "a", 0.95,
         {"n": 4, "diferenca": -1.75, "baixo": -3.2735, "alto": -0.2265, "gl": 3, "dz": -1.8278, "dav": -1.254}),
        ("zero é número", [{"x": "0", "y": "1"}, {"x": "2", "y": "2"}, {"x": "1", "y": "0"}, {"x": "3", "y": "1"}],
         "x", "y", 0.95,
         {"n": 4, "diferenca": 0.5, "baixo": -1.5543, "alto": 2.5543, "gl": 3, "dz": 0.3873, "dav": 0.4745}),
    ]
    falhas = 0
    for nome, linhas, col_a, col_b, nivel, esperado in casos:
        copia = copy.deepcopy(linhas)
        try:
            r = funcao(linhas, col_a, col_b, nivel)
            problema = comparar(r, esperado)
        except Exception as erro:
            problema = f"deu erro: {erro!r}"
        if not problema and linhas != copia:
            problema = "a função mudou a lista que recebeu"
        print(("ok    " if not problema else "FALHA ") + nome + ("" if not problema else f": {problema}"))
        falhas += bool(problema)

    for nome, linhas in [("um par completo só", [{"a": "10", "b": "8"}, {"a": "", "b": "3"}]),
                         ("nenhum par completo", [{"a": "", "b": "3"}, {"a": "4", "b": " "}]),
                         ("lista vazia", [])]:
        try:
            r = funcao(linhas, "a", "b", 0.95)
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
