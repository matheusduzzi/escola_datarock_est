# 27. Intervalo para proporção

Os arquivos da aula «Intervalo para proporção» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `entregas_maio.csv` | O exercício: 90 entregas de maio, 60 da capital e 30 do interior: `id_entrega`, `regiao` (`capital` ou `interior`) e `horas`, em horas cheias. Célula de `horas` vazia quer dizer que a baixa não foi anotada |
| `minha_solucao.py` | Onde você escreve a função `proporcao_da_coluna` da tarefa 2 |
| `conferir.py` | Testa a sua função com as entregas de março e com casos pequenos. Não usa as entregas de maio |
| `gerar_dados.py` | O programa que gera `entregas_maio.csv` de novo, igual toda vez. O começo dele conta como os tempos e as baixas que faltam foram sorteados: abra só depois de fazer o exercício |
| `respostas-modelo.md` | A folha do exercício. Salve uma cópia com o seu nome |

As 48 entregas de março, que a aula usa, ficam na base compartilhada do kit: `../dados/loja/entregas.csv`.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 2. O bloco da seção 2 importa `csv` e `math` e cria `horas`. O da seção 3 cria `wald` e `pct`, o da seção 5 cria `wilson` e o da seção 6 cria `exato`. O exercício usa essas funções.

Nenhuma conta da aula usa sorteio: as saídas são sempre as mesmas.

Para testar a sua função da tarefa 2:

```bash
python3 conferir.py
```

Enquanto a função não estiver pronta, aparecem linhas com `FALHA` e o motivo. Quando tudo passar, a última linha é `tudo certo`.

Para gerar o arquivo de maio de novo:

```bash
python3 gerar_dados.py
```

A saída é `maio=90 capital=60 interior=30 sem_baixa=6`.

Tudo aqui usa só a biblioteca padrão do Python 3.9 ou mais novo. No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
