# 13. Condicional e independência

Os arquivos da aula «Condicional e independência» do curso Estatística para decisão.

## Os dados da aula

| Arquivo | Colunas |
|---|---|
| `dados/pedidos_outubro.csv` | Os 200 pedidos de outubro de 2026, os mesmos da aula «Eventos e regras de probabilidade»: `id_pedido`, `canal` (site ou app), `status` (no prazo, atrasado ou cancelado) e `devolvido` (1 quando o cliente devolveu). As 10 primeiras linhas são os pedidos de 1 de outubro, que a aula resolve à mão |

## Os dados do exercício

| Arquivo | Colunas |
|---|---|
| `dados/entregas_novembro.csv` | As 240 entregas de novembro de 2026: `id_entrega`, `transportadora` (leva ou trilha), `atrasou` (1 quando a entrega atrasou) e `reclamou` (1 quando o cliente reclamou). As 12 primeiras linhas são a tabela da tarefa 1 |

## A folha de respostas

`respostas-modelo.md` é a folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta, só com o pandas que o README do kit já instala:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. Os caminhos começam em `dados/`. O primeiro bloco cria a tabela `p` e a coluna `atrasou`, que os outros usam.

Os dois arquivos vêm prontos e são sempre os mesmos.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
