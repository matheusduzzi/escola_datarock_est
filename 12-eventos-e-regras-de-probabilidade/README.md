# 12. Eventos e regras de probabilidade

Os arquivos da aula «Eventos e regras de probabilidade» do curso Estatística para decisão.

## Os dados da aula

| Arquivo | Colunas |
|---|---|
| `dados/pedidos_outubro.csv` | Os 200 pedidos de outubro de 2026: `id_pedido`, `canal` (site ou app), `status` (no prazo, atrasado ou cancelado) e `devolvido` (1 quando o cliente devolveu). As 10 primeiras linhas são os pedidos de 1 de outubro, que a aula resolve à mão |

## Os dados do exercício

| Arquivo | Colunas |
|---|---|
| `dados/chamados_outubro.csv` | Os 160 chamados do atendimento em outubro de 2026: `id_chamado`, `canal` (chat, telefone ou email), `motivo` (atraso, troca, pagamento ou outro) e `resolvido_primeiro_contato` (1 quando se resolveu no primeiro contato). As 12 primeiras linhas são a tabela da tarefa 1 |

## A folha de respostas

`respostas-modelo.md` é a folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta, só com o pandas que o README do kit já instala:

```bash
python3
```

Depois cole os blocos da aula na ordem. Os caminhos começam em `dados/`. Cada bloco usa a tabela `p` e as listas criadas nos blocos anteriores (`atrasou`, `devolvido`, `cancelado`), então rode na ordem, a partir da seção 4.

Os dois arquivos vêm prontos e são sempre os mesmos.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
