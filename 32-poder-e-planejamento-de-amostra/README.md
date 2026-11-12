# 32. Poder e planejamento de amostra

Os arquivos da aula «Poder e planejamento de amostra» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `respostas-modelo.md` | A folha do exercício, com as seis tarefas, a tabela dos cenários e as sete linhas do plano. Salve uma cópia com o seu nome |

A aula não tem arquivo de dados. As contas usam só os números do texto: o ganho que importa, o desvio, a linha e o poder.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. O primeiro bloco da seção 4 cria `poder_formula` e `n_por_grupo`. O segundo cria `piloto` e `poder_simulado`. A seção 7 cria `poder_depois` e a seção 9 cria `olhar_duas_vezes`. O resto da aula e o exercício usam essas funções. As simulações levam alguns segundos, e as do exercício, uns 10.

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`. Rodar só uma parte continua o sorteio de onde ele parou.

Só usa a biblioteca padrão do Python: `math`, `random` e `statistics`. No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
