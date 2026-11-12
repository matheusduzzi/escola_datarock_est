# 14. Bayes e taxa-base

Os arquivos da aula «Bayes e taxa-base» do curso Estatística para decisão.

## Os dados da aula

| Arquivo | Colunas |
|---|---|
| `dados/crediario_semestre.csv` | As 1.000 compras no crediário do primeiro semestre de 2025: `id_compra`, `cliente` (novo ou recorrente), `alerta` (1 quando o alerta de risco acendeu na compra) e `inadimpliu` (1 quando a compra virou inadimplência, com parcela em mais de 90 dias de atraso) |

## Os dados do exercício

| Arquivo | Colunas |
|---|---|
| `dados/alerta_novo_semestre.csv` | As 1.200 compras no crediário do segundo semestre de 2025, em que o fornecedor testou o alerta novo: `id_compra`, `cliente` (novo ou recorrente), `alerta_novo` (1 quando o alerta novo acendeu) e `inadimpliu` (1 quando a compra virou inadimplência) |

## A folha de respostas

`respostas-modelo.md` é a folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta, só com o pandas que o README do kit já instala:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. O primeiro bloco cria a função `chance_depois`, e o segundo cria a tabela `c`. Os outros usam as duas. Os caminhos começam em `dados/`.

Os dois arquivos vêm prontos e são sempre os mesmos.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
