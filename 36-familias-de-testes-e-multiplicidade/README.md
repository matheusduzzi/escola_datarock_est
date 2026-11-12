# 36. Famílias de testes e multiplicidade

Os arquivos da aula «Famílias de testes e multiplicidade» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `painel_carrinho.csv` | O painel do teste do carrinho: 20 métricas, faixa de R$ 199 contra sem faixa, com diferença, erro padrão e p-valor |
| `relatorio_chat.csv` | O relatório do fornecedor do chat, usado no exercício: a pergunta do plano e 16 comparações por região |
| `painel.py` | As funções `sortear_painel` e `comparar`, que a seção 4 da aula usa para sortear o painel num mundo sem diferença |
| `gerar_dados.py` | Gera de novo os dois arquivos `.csv` |
| `respostas-modelo.md` | A folha do exercício, com as cinco tarefas e as seis linhas da definição da família. Salve uma cópia com o seu nome |

Nos arquivos, as proporções são a parte dos clientes: 0,15 é 15%. A diferença é sempre o segundo grupo menos o primeiro.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 3. A seção 3 cria `chance_de_algum`. A seção 4 cria `alarmes`. A seção 5 lê o `painel_carrinho.csv` na lista `painel`. A seção 8 cria `faixa` e `fator_tamanho`. A prática guiada e o exercício usam essas funções. Os sorteios da seção 4 levam uns 10 segundos cada.

Para gerar os arquivos de novo:

```bash
python3 gerar_dados.py
```

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`. Rodar só uma parte continua o sorteio de onde ele parou.

Só usa a biblioteca padrão do Python: `csv`, `math`, `random` e `statistics`. No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
