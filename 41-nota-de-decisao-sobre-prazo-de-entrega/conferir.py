"""Testa as suas funções quadro_de_prazos e prazo_para_mostrar antes de usar no interior.

    python3 conferir.py                    # testa minha_solucao.py, nessa pasta
    python3 conferir.py outro_arquivo.py   # testa outro arquivo

Os testes usam o piloto de setembro e as entregas de março da aula, mais casos pequenos
montados à mão. Nenhum teste usa as entregas do interior: esses números são você que descobre.
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
    return mod.quadro_de_prazos, mod.prazo_para_mostrar


def comparar(linha, esperado):
    for chave, valor in esperado.items():
        if chave not in linha:
            return f"faltou a chave {chave!r}"
        if isinstance(valor, (int, str)) and not isinstance(valor, bool):
            if linha[chave] != valor:
                return f"{chave} deu {linha[chave]!r}, esperado {valor!r}"
        elif round(linha[chave], 4) != valor:
            return f"{chave} deu {round(linha[chave], 4)}, esperado {valor}"
    return ""


def main():
    arquivo = Path(sys.argv[1]) if len(sys.argv) > 1 else PASTA / "minha_solucao.py"
    try:
        quadro_de_prazos, prazo_para_mostrar = carregar(arquivo)
    except Exception as erro:  # o arquivo pode nem abrir; o aluno precisa ver o motivo
        print(f"não consegui carregar as funções de {arquivo.name}: {erro!r}")
        return 1

    with open(PASTA / "setembro.csv", encoding="utf-8") as f:
        setembro = list(csv.DictReader(f))
    atual = [l["horas"] for l in setembro if l["transportadora"] == "atual"]
    nova = [l["horas"] for l in setembro if l["transportadora"] == "nova"]
    with open(PASTA.parent / "dados" / "loja" / "entregas.csv", encoding="utf-8") as f:
        marco = [l["horas"] for l in csv.DictReader(f)]
    sessenta = ["10"] * 60

    falhas = 0

    def teste(nome, funcao):
        nonlocal falhas
        try:
            motivo = funcao()
        except NotImplementedError as erro:
            motivo = f"a função ainda não foi escrita ({erro})"
        except Exception as erro:  # o aluno precisa ver qual erro apareceu
            motivo = f"deu erro: {erro!r}"
        if motivo:
            falhas += 1
            print(f"FALHA {nome}: {motivo}")
        else:
            print(f"ok    {nome}")

    def caso(valores, prazos, esperados, minimo=0.90):
        def rodar():
            quadro = quadro_de_prazos(valores, prazos, minimo)
            if len(quadro) != len(esperados):
                return f"o quadro tem {len(quadro)} linhas, esperado {len(esperados)}"
            for linha, esperado in zip(quadro, esperados):
                motivo = comparar(linha, esperado)
                if motivo:
                    return f"prazo {esperado.get('prazo')}: {motivo}"
            return ""
        return rodar

    teste("setembro, atual: 48 h fica abaixo de 90% e 54 h passa, como na aula",
          caso(atual, [48, 54], [
              {"prazo": 48, "ate": 85, "n": 105, "vazias": 0, "p": 0.8095, "inferior": 0.724,
               "superior": 0.8732, "pior": 0.724, "melhor": 0.8732, "decisao": "não mostrar"},
              {"prazo": 54, "ate": 102, "n": 105, "vazias": 0, "inferior": 0.9193, "decisao": "mostrar"}]))
    teste("setembro, nova: 48 h fica inconclusivo",
          caso(nova, [48], [{"prazo": 48, "ate": 91, "n": 105, "inferior": 0.7886, "superior": 0.9189,
                             "decisao": "inconclusivo"}]))
    teste("março: as 3 sem baixa entram no pior e no melhor caso, e 48 h não passa nem no melhor",
          caso(marco, [48], [{"prazo": 48, "ate": 26, "n": 45, "vazias": 3, "p": 0.5778, "inferior": 0.433,
                              "superior": 0.7103, "pior": 0.4029, "melhor": 0.7298, "decisao": "não mostrar"}]))
    teste("48 horas cravadas contam como até 48",
          caso(["48", "48.0", "50"], [48], [{"ate": 2, "n": 3, "vazias": 0}]))
    teste("vazio, célula só com espaços e None ficam fora do n e contam como vazias",
          caso(["", "  ", None, "10", "60"], [48], [{"ate": 1, "n": 2, "vazias": 3}]))
    teste("60 entregas no prazo passam; com 3 sem baixa, o pior caso não passa mais",
          lambda: caso(sessenta, [48], [{"ate": 60, "n": 60, "pior": 0.9398, "decisao": "mostrar"}])()
          or caso(sessenta + ["", "", ""], [48], [{"ate": 60, "n": 60, "vazias": 3, "inferior": 0.9398,
                                                   "pior": 0.8691, "melhor": 1.0, "decisao": "inconclusivo"}])())

    def mesmo_minimo():
        pior = quadro_de_prazos(atual, [54])[0]["pior"]
        decisao = quadro_de_prazos(atual, [54], pior)[0]["decisao"]
        return "" if decisao == "mostrar" else f"com o mínimo igual ao começo da faixa deu {decisao!r}"
    teste("começo da faixa igual ao mínimo conta como mostrar", mesmo_minimo)

    def ordem_e_menor():
        quadro = quadro_de_prazos(atual, [60, 48, 54])
        if [l["prazo"] for l in quadro] != [60, 48, 54]:
            return "o quadro precisa seguir a ordem dos prazos recebidos"
        escolhido = prazo_para_mostrar(quadro)
        if escolhido != 54:
            return f"prazo_para_mostrar deu {escolhido!r}; o menor prazo que passa é 54"
        nenhum = prazo_para_mostrar(quadro_de_prazos(marco, [48, 54]))
        return "" if nenhum is None else f"sem prazo que passe, esperado None, veio {nenhum!r}"
    teste("prazo_para_mostrar escolhe o menor prazo que passa, e None se nenhum passa", ordem_e_menor)

    def recusa(valores, minimo):
        def rodar():
            try:
                quadro_de_prazos(valores, [48], minimo)
            except ValueError:
                return ""
            return "esperava ValueError"
        return rodar
    teste("sem nenhuma entrega com baixa: ValueError", recusa(["", None, " "], 0.90))
    teste("mínimo em porcentagem (90 no lugar de 0.90): ValueError", recusa(["10", "20"], 90))

    def nao_mexe():
        valores = ["", "10", None, "60"]
        copia = list(valores)
        quadro_de_prazos(valores, [48])
        return "" if valores == copia else "a função mudou a lista que recebeu"
    teste("a função não muda a lista que recebeu", nao_mexe)

    if falhas:
        print(f"{falhas} teste(s) com FALHA")
        return 1
    print("tudo certo")
    return 0


if __name__ == "__main__":
    sys.exit(main())
