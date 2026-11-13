# 34. ANOVA e comparações entre grupos

Os arquivos da aula «ANOVA e comparações entre grupos» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `distribuicao_f.py` | A tabela F no Python, só com a biblioteca padrão: `f_acumulada(x, gl1, gl2)` dá a chance de ficar abaixo de `x`, e `f_critico(alfa, gl1, gl2)` dá o número da tabela. Os graus de liberdade podem ter vírgula |
| `respostas-modelo.md` | A folha do exercício, com as seis tarefas e as oito linhas do plano. Salve uma cópia com o seu nome |

A aula não tem arquivo de dados. As contas usam os números do texto: os doze pedidos da seção 3, os doze tempos do exercício e os mundos que as funções sorteiam.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta, porque eles importam o `distribuicao_f.py`:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. O primeiro bloco da seção 4 cria `anova_classica` e `mostrar`. O da seção 5 cria `p_welch` e `rodar_testes`. O da seção 8 cria `anova_welch` e o da seção 10 cria `n_por_grupo` e o `n` do plano. O resto da aula e o exercício usam essas funções.

As simulações levam tempo. O bloco da seção 5 leva uns 25 segundos, o da seção 8, uns 30, e o da seção 10, uns 15. No exercício, cada chamada da `rodar_testes` com quatro grupos leva uns 15 segundos.

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`. Rodar só uma parte continua o sorteio de onde ele parou.

Só usa a biblioteca padrão do Python: `math`, `random`, `itertools` e `statistics`. No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
