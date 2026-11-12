# 26. Intervalo para média de entregas

Os arquivos da aula «Intervalo para média de entregas» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `entregas_abril.csv` | O exercício: 60 entregas de abril, 40 da capital e 20 do interior: `id_entrega`, `regiao` (`capital` ou `interior`) e `horas`. Célula de `horas` vazia quer dizer que a baixa não foi anotada |
| `minha_solucao.py` | Onde você escreve a função `intervalo_da_coluna` da tarefa 2 |
| `conferir.py` | Testa a sua função com as entregas de março e com casos pequenos. Não usa as entregas de abril |
| `gerar_dados.py` | O programa que gera `entregas_abril.csv` de novo, igual toda vez. O começo dele conta como os tempos e as baixas que faltam foram sorteados: abra só depois de fazer o exercício |
| `respostas-modelo.md` | A folha do exercício. Salve uma cópia com o seu nome |

As 48 entregas de março, que a aula usa, ficam na base compartilhada do kit: `../dados/loja/entregas.csv`.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 2. O bloco da seção 2 importa `csv`, `random` e `statistics` e cria `horas`. O da seção 3 cria `intervalo_t`, o da seção 4 cria `media` e `bootstrap`, e o da seção 8 cria `bootstrap_por_regiao`. O exercício usa essas funções.

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`.

Para testar a sua função da tarefa 2:

```bash
python3 conferir.py
```

Enquanto a função não estiver pronta, aparecem linhas com `FALHA` e o motivo. Quando tudo passar, a última linha é `tudo certo`.

Para gerar o arquivo de abril de novo:

```bash
python3 gerar_dados.py
```

A saída é `abril=60 capital=40 interior=20 sem_baixa=8`.

Tudo aqui usa só a biblioteca padrão do Python 3.9 ou mais novo. No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
