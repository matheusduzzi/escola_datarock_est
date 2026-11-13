# 10. Por que associação não prova causa

Os arquivos da aula «Por que associação não prova causa» do curso Estatística para decisão.

## Os dados da aula

| Arquivo | Colunas |
|---|---|
| `dados/pedidos_setembro.csv` | Os 150 pedidos de setembro, os mesmos da aula 09: `id_pedido`, `canal` (app, site ou empresas), `distancia_km` do cliente e `valor` do pedido em reais |
| `dados/carrinhos_agosto.csv` | Os 400 carrinhos de agosto com frete calculado, de onde sai o relatório de frete do financeiro (os 134 finalizados são os pedidos de agosto do relatório): `id_carrinho`, `valor_carrinho` e `frete` em reais, e `finalizou` (1 quando o carrinho virou pedido, 0 quando o cliente desistiu) |
| `dados/entregas_outubro.csv` | As 120 entregas de outubro, com prazo de 48 horas: `id_entrega`, `horas` até a entrega, `consultas_24h` (consultas ao rastreamento nas primeiras 24 horas) e `consultas_total` |

## Os dados do exercício

| Arquivo | Colunas |
|---|---|
| `dados/clientes_outubro.csv` | 300 clientes: `id_cliente`, `meses_de_casa` (desde o cadastro), `recebe_email` (1 quando recebe o e-mail semanal) e `gasto_outubro` em reais |
| `dados/clientes_setembro.csv` | 400 clientes que compraram em setembro: `id_cliente`, `atrasou_setembro` (1 quando a entrega atrasou), `comprou_outubro` (1 quando comprou de novo) e `nota_pesquisa` de 0 a 10. A pesquisa vai junto com a compra de outubro; quem não comprou fica com a nota vazia |
| `dados/semanas_2026.csv` | As 40 primeiras semanas de 2026: `semana`, `desconto` (1 quando houve desconto na semana), `vendas` (pedidos da semana) e `vendas_semana_anterior` (vazia na semana 1) |

## A folha do mapa

`mapa-explicacoes.md` é a folha do exercício: uma ficha por frase, com a associação, as três explicações, a conta que separa, o que dá para dizer e o próximo passo. Salve uma cópia com o seu nome.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta, só com o pandas que o README do kit já instala:

```bash
python3
```

Depois cole o bloco da aula. Os caminhos começam em `dados/`.

Para gerar de novo os carrinhos e as entregas da aula:

```bash
python3 gerar.py
```

A saída é `carrinhos_agosto=400 entregas_outubro=120`. O sorteio é sempre o mesmo, então os arquivos saem iguais toda vez. Os pedidos de setembro vêm da aula 09, e os arquivos do exercício vêm prontos.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
