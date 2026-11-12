"""Testa as suas funções margem e n_para_margem antes de usar no piloto de abril.

    python3 conferir.py                    # testa minha_solucao.py, nessa pasta
    python3 conferir.py outro_arquivo.py   # testa outro arquivo

Os testes usam os números de março da aula e casos pequenos feitos à mão.
Nenhum teste usa o piloto de abril: os números de abril são você que descobre.
Sai com código 0 quando tudo passa e 1 quando algum teste falha.
"""
import importlib.util
import sys
from pathlib import Path

PASTA = Path(__file__).resolve().parent


def carregar(arquivo):
    spec = importlib.util.spec_from_file_location("solucao_do_aluno", arquivo)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.margem, mod.n_para_margem


def main():
    arquivo = Path(sys.argv[1]) if len(sys.argv) > 1 else PASTA / "minha_solucao.py"
    try:
        margem, n_para_margem = carregar(arquivo)
    except Exception as erro:  # o arquivo pode nem abrir; o aluno precisa ver o motivo
        print(f"não consegui carregar margem e n_para_margem de {arquivo.name}: {erro!r}")
        return 1

    def perto(valor, esperado):
        return isinstance(valor, (int, float)) and abs(valor - esperado) < 0.0005

    casos = [
        ("março, 95%: 2,12 horas, como na seção 2", lambda: margem(7.24, 45), lambda r: perto(r, 2.1153), "2.1153"),
        ("março, 99%: z de 2,576", lambda: margem(7.24, 45, 0.99), lambda r: perto(r, 2.78), "2.78"),
        ("março, 80%: z de 1,282", lambda: margem(7.24, 45, 0.80), lambda r: perto(r, 1.3831), "1.3831"),
        ("quatro vezes mais entregas, metade da margem", lambda: margem(7.24, 180) / margem(7.24, 45),
         lambda r: perto(r, 0.5), "0.5"),
        ("desvio zero, margem zero", lambda: margem(0, 10), lambda r: perto(r, 0.0), "0.0"),
        ("1 hora com o desvio de março: 202 entregas", lambda: n_para_margem(7.24, 1),
         lambda r: r == 202 and isinstance(r, int), "202 (inteiro)"),
        ("5 pontos de proporção com 50%: 385, arredondado para cima de 384,1",
         lambda: n_para_margem(0.5, 0.05), lambda r: r == 385 and isinstance(r, int), "385 (inteiro)"),
        ("meia hora com 99%: 1.392 entregas", lambda: n_para_margem(7.24, 0.5, 0.99), lambda r: r == 1392, "1392"),
        ("desvio zero ainda pede pelo menos 1 entrega", lambda: n_para_margem(0, 1), lambda r: r == 1, "1"),
    ]
    falhas = 0
    for nome, chamar, ok, esperado in casos:
        try:
            r = chamar()
            problema = "" if ok(r) else f"deu {r!r}, esperado {esperado}"
        except Exception as erro:
            problema = f"deu erro: {erro!r}"
        print(("ok    " if not problema else "FALHA ") + nome + ("" if not problema else f": {problema}"))
        falhas += bool(problema)

    invalidos = [
        ("desvio negativo na margem", lambda: margem(-1, 45)),
        ("n zero na margem", lambda: margem(7.24, 0)),
        ("confiança 95 em vez de 0.95", lambda: margem(7.24, 45, 95)),
        ("confiança 1 (100%) não existe", lambda: margem(7.24, 45, 1.0)),
        ("margem desejada zero", lambda: n_para_margem(7.24, 0)),
        ("desvio negativo no tamanho", lambda: n_para_margem(-7.24, 1)),
    ]
    for nome, chamar in invalidos:
        try:
            r = chamar()
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
