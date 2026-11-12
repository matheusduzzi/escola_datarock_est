# 04. Dispersão e escala

Os arquivos da aula «Dispersão e escala» do curso Estatística para decisão. Rode os comandos de dentro dessa pasta.

| Arquivo | Para que serve |
|---|---|
| `dispersao.py` | As contas da aula: centro, variância, desvio, IQR e CV das entregas de outubro, as mesmas medidas em dias, a entrega perdida e a simulação do n − 1. |
| `dados/entregas_outubro.csv` | 120 entregas: `id_entrega`, `transportadora` (`rapida` ou `via_sul`) e `horas` do pedido até a entrega. |
| `dados/reposicoes.csv` | 80 pedidos de embalagem do exercício: `id_pedido`, `fornecedor` (`norte` ou `leste`), `dias`, `caixas` e `diferenca`. O exercício explica cada coluna. |
| `minha_analise.py` | Onde você escreve o código do exercício. |
| `minhas-respostas.md` | Onde você escreve as respostas do exercício. |

## Como rodar

Você precisa do Python com o pandas, como no README do kit do curso.

```bash
python3 dispersao.py
```

A saída é a mesma da seção 4 da aula, e sai igual toda vez: o sorteio da simulação começa sempre do mesmo ponto.

```bash
python3 minha_analise.py
```

Antes de você escrever qualquer coisa, ele só mostra `80 pedidos: norte 40, leste 40`. As tarefas ficam embaixo, nos comentários.

Se aparecer `FileNotFoundError`, você está rodando de outra pasta. Entre na pasta dessa aula e rode de novo.

Os dois CSVs vêm prontos e não mudam. Não edite à mão: as respostas do exercício dependem desses números.

## Se precisar de ajuda

Deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
