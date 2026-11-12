# 31. P-valor, erros e relevância

Os arquivos da aula «P-valor, erros e relevância» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `entregas_junho.csv` | O piloto de junho da Dani, o mesmo da aula «Hipóteses e distribuição nula»: 60 entregas da capital, 30 sorteadas para cada transportadora. Colunas `id_entrega`, `transportadora` (`atual` ou `nova`) e `horas` |
| `respostas-modelo.md` | A folha do exercício, com as sete tarefas e uma linha para cada frase do Bruno. Salve uma cópia com o seu nome |

O exercício não tem arquivo de dados. Os pedidos com e sem avaria viram listas de 1 e 0 no próprio Python.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 3. O bloco da seção 3 cria as funções `diferenca_medias` e `distribuicao_nula`. O da seção 4 cria `linha_de_corte` e `piloto`, e o da seção 6 cria `intervalo_bootstrap`. O resto da aula e o exercício usam essas funções. Os blocos das seções 4 e 7 levam alguns segundos.

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`. Rodar só uma parte continua o sorteio de onde ele parou.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
