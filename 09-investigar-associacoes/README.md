# 09. Investigar associações

Os arquivos da aula «Investigar associações» do curso Estatística para decisão.

| Arquivo | Para quê |
|---|---|
| `associacao.py` | As contas da seção 5: Pearson e Spearman de duas colunas no total e em cada segmento, e as linhas que mais mexem no Pearson quando saem da conta |
| `dispersao.py` | O gráfico de dispersão de duas colunas, com uma cor e um marcador por segmento. Salva o PNG em `saidas/` |
| `dados/pedidos_setembro.csv` | Os 150 pedidos de setembro da aula: `id_pedido`, `canal` (app, site ou empresas), `distancia_km` do cliente e `valor` do pedido em reais |
| `dados/entregas_maio.csv` | As 90 entregas de maio do exercício: `id_entrega`, `modalidade` (normal ou expressa), `volumes` (caixas), `distancia_km` e `horas` até a baixa |
| `gerar.py` | Gera de novo os dois CSVs, sempre iguais. Deixe para abrir depois de entregar o exercício |
| `modelo-analise.md` | A folha da análise: pergunta, o que o número diz, hipóteses, o que não dá para dizer, limites e próximo passo |

Rode tudo de dentro dessa pasta:

```bash
python3 associacao.py
python3 associacao.py --sem 1150 --influentes 0
python3 dispersao.py --destacar 1150
```

O `associacao.py` usa só o pandas, que o README do kit já instala. As opções `--arquivo`, `--x`, `--y` e `--segmento` trocam o arquivo e as colunas; `--segmento nenhum` calcula só o total. `--sem` tira uma linha pelo id, só da conta, e pode ser repetido. `--influentes` diz quantas linhas mostrar no fim (0 esconde a lista).

O `dispersao.py` precisa também do Matplotlib, a biblioteca de gráficos. Instale com o mesmo `python3` que roda o programa:

```bash
python3 -m pip install matplotlib
```

A aula rodou com o Matplotlib 3.9.4. Sem ele, o programa para com a mensagem do comando acima. O gráfico sai em `saidas/dispersao_<x>_<y>.png`; abra o arquivo para ver.

Para gerar os dados de novo:

```bash
python3 gerar.py
```

A saída é `pedidos_setembro=150 entregas_maio=90`. O sorteio é sempre o mesmo, então os arquivos saem iguais toda vez.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
