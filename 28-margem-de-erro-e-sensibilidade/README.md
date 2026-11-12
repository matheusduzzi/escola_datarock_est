# 28. Margem de erro e sensibilidade

Os arquivos da aula «Margem de erro e sensibilidade» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `piloto_abril.csv` | O exercício: 40 entregas de abril, sorteadas entre todas as do mês: `id_entrega`, `regiao` (`capital` ou `interior`) e `horas`. Célula de `horas` vazia quer dizer que a baixa não foi anotada |
| `minha_solucao.py` | Onde você escreve as funções `margem` e `n_para_margem` da tarefa 2 |
| `conferir.py` | Testa as suas funções com os números de março da aula e com casos pequenos. Não usa o piloto de abril |
| `gerar_dados.py` | O programa que gera `piloto_abril.csv` de novo, igual toda vez. O começo dele conta como os tempos e as baixas que faltam foram sorteados: abra só depois de fazer o exercício |
| `respostas-modelo.md` | A folha do exercício. Salve uma cópia com o seu nome |

As 48 entregas de março, que a aula usa, ficam na base compartilhada do kit: `../dados/loja/entregas.csv`.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 2. O primeiro bloco da seção 2 lê março e cria `horas`, `n` e `s`. O segundo cria `z_do_nivel` e `margem`. O da seção 6 cria `n_para_margem`, e o da seção 8 cria `VERDADE`, `coletar` e `simular`. O exercício usa essas funções.

O bloco da seção 8 sorteia 500 meses para cada tamanho e leva alguns segundos. Ele usa um número fixo no sorteio, então as saídas são sempre as mesmas da aula.

Para testar as suas funções da tarefa 2:

```bash
python3 conferir.py
```

Enquanto as funções não estiverem prontas, aparecem linhas com `FALHA` e o motivo. Quando tudo passar, a última linha é `tudo certo`.

Para gerar o arquivo de abril de novo:

```bash
python3 gerar_dados.py
```

A saída é `abril=40 capital=27 interior=13 sem_baixa=3`.

Tudo aqui usa só a biblioteca padrão do Python 3.9 ou mais novo. No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
