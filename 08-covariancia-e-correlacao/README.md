# 08. Covariância e correlação

Os arquivos da aula «Covariância e correlação» do curso Estatística para decisão.

| Arquivo | Para quê |
|---|---|
| `correlacao.py` | As contas da seção 5: covariância, Pearson e Spearman de cada coluna contra uma coluna-alvo, e a média do alvo em cada faixa |
| `dados/produtos.csv` | Os 60 produtos de outubro da planilha do Rafa: `id_produto`, `preco` em reais, `visitas` à página, `vendas` em unidades e `peso_kg` |
| `dados/entregas_abril.csv` | As 80 entregas de abril do exercício: `id_entrega`, `distancia_km`, `hora_saida` (hora cheia, de 7 a 19), `volumes` (caixas), `horas` até a baixa e `nota` do cliente, de 1 a 5 |
| `gerar.py` | Gera de novo os dois CSVs, sempre iguais. Deixe para abrir depois de entregar o exercício |
| `modelo-leitura.md` | A folha da leitura: pergunta, unidade, cada coluna, o que não dá para dizer e próximo passo |

Rode tudo de dentro dessa pasta:

```bash
python3 correlacao.py
python3 correlacao.py --multiplicar preco=100
python3 correlacao.py --arquivo dados/entregas_abril.csv --alvo horas
```

O programa usa só o pandas, que o README do kit já instala. Não precisa do SciPy nem de internet. O começo do `correlacao.py` mostra a linha de pandas de cada conta.

Para gerar os dados de novo:

```bash
python3 gerar.py
```

A saída é `produtos=60 entregas_abril=80`. O sorteio é sempre o mesmo, então os arquivos saem iguais toda vez.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
