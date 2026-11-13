# 35. Aplicar ANOVA e interpretar limites

Os arquivos da aula «Aplicar ANOVA e interpretar limites» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `carrinho.csv` | As quatro semanas do teste da faixa de frete do Rafa: 949 pedidos, um por linha. Colunas `pedido`, `cliente`, `semana`, `dia`, `dia_semana`, `versao` (`sem_faixa`, `faixa_199` ou `faixa_149`) e `valor` em reais |
| `transportadoras.csv` | O teste da Dani no interior, do exercício: 1.150 entregas, uma por linha. Colunas `entrega`, `dia`, `transportadora` (`atual`, `A`, `B` ou `C`), `status` (`entregue` ou `extraviada`) e `horas`. A extraviada fica com `horas` vazia |
| `distribuicao_f.py` | A tabela F no Python, só com a biblioteca padrão: `f_acumulada(x, gl1, gl2)` dá a chance de ficar abaixo de `x`. Os graus de liberdade podem ter vírgula |
| `distribuicao_t.py` | A tabela t no Python: `t_acumulada(x, gl)` e `t_critico(nivel, gl)`, que dá o número da tabela para uma faixa de `nivel` |
| `relatorio-modelo.md` | A folha do exercício, com as seis tarefas e as oito partes do relatório. Salve uma cópia com o seu nome |
| `gerar_dados.py` | Gera os dois CSVs de novo. Ele conta como cada número nasce: abra só depois de fazer a aula e o exercício |

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta, porque eles leem os CSVs e importam as duas tabelas:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 3. O bloco da seção 3 lê o `carrinho.csv` e cria `primeiros_pedidos` e as listas `grupos`. O da seção 4 cria `resumo`. O da seção 5 cria `anova_classica`, `anova_welch` e `mostrar`. O da seção 6 cria `comparar`. O resto da aula e o exercício usam essas funções. Todos os blocos rodam em poucos segundos.

Para gerar os CSVs de novo:

```bash
python3 gerar_dados.py
```

A saída é `carrinho=949 transportadoras=1150`. Os arquivos saem iguais toda vez.

O sorteio da seção 8 sai igual toda vez que você roda. Se a sua saída tiver outro número, rode o bloco inteiro de novo, desde a linha do `random.Random`.

Só usa a biblioteca padrão do Python: `csv`, `math`, `random`, `collections` e `statistics`. No Windows, troque `python3` por `py`. Não precisa do SciPy. Se você já usa o SciPy, a aula mostra as funções equivalentes.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
