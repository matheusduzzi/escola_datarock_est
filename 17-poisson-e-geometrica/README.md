# 17. Poisson e geométrica

Os arquivos da aula «Poisson e geométrica» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `dados/chamados_outubro.csv` | Chamados do chat por hora, de 1 a 31 de outubro, das 8h às 20h: data, hora e chamados. 372 linhas. Usado nas seções 4 e 5 da aula |
| `dados/entregas_interior.csv` | Os 300 pacotes da transportadora do interior: pacote, tentativas (1 a 3) e entregue (1) ou voltou (0). Usado na seção 7 |
| `dados/trocas_cd.csv` | Trocas que chegaram ao CD em cada dia útil de 8 semanas: semana, dia da semana e trocas. 40 linhas. Usado no exercício |
| `dados/ligacoes_pesquisa.csv` | Os 250 clientes da pesquisa de satisfação: cliente, ligações feitas (1 a 4) e atendeu (1) ou não (0). Usado no exercício |
| `gerar_dados.py` | Refaz os dois arquivos da aula, iguais toda vez |
| `respostas-modelo.md` | A folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome |

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos na ordem, a partir da seção 3. O primeiro cria a função `poisson`, o da seção 4 lê os chamados, e os outros usam o que veio antes. O bloco da seção 6 cria a função `geometrica`, que a seção 11 usa.

Se você mexer nos arquivos da aula e quiser os originais de volta:

```bash
python3 gerar_dados.py
```

O programa escreve `dados/chamados_outubro.csv` e `dados/entregas_interior.csv`. A saída é a mesma toda vez e foi igual no Python 3.9, no 3.14 e no 3.15. Os arquivos do exercício não são refeitos por ele; se precisar, baixe de novo a pasta da aula.

As contas usam só o `math`, o `csv` e o `statistics` do Python. O kit do curso pede o Python 3.9 ou mais novo. O SciPy não é necessário nessa aula.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
