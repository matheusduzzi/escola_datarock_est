# 11. Revisar uma conclusão causal

Os arquivos da aula «Revisar uma conclusão causal» do curso Estatística para decisão.

## Os dados da aula

| Arquivo | Colunas |
|---|---|
| `dados/clientes_app.csv` | Os 600 clientes que compraram pelo menos uma vez de março a agosto de 2026: `id_cliente`, `compras_mar_ago` (total de compras nesses seis meses), `instalou_setembro` (1 quando instalou o app em setembro), `tem_app_31out` (1 quando ainda tinha o app em 31 de outubro) e `compras_outubro` |

## Os dados do exercício

| Arquivo | Colunas |
|---|---|
| `dados/assinantes_clube.csv` | Os 500 assinantes do clube de frete em 30 de setembro: `id_assinante`, `meses_de_clube` (desde a assinatura), `pedidos_jul_set` (pedidos de julho a setembro), `usou_chat_setembro` (1 quando falou com o chat em setembro) e `cancelou_outubro` (1 quando cancelou o clube em outubro) |

## A folha do parecer

`parecer-modelo.md` é a folha do exercício, com as seis partes do parecer da aula. Salve uma cópia com o seu nome.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta, só com o pandas que o README do kit já instala:

```bash
python3
```

Depois cole os blocos da aula na ordem. Os caminhos começam em `dados/`. Os blocos da seção 5 e os pedidos 3 e 4 usam a tabela `c` e as colunas criadas antes, então rode a seção 4 primeiro.

Os dois arquivos vêm prontos e são sempre os mesmos.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
