# Estudo inventado de orientação alimentar

Os dados das aulas 39 e 40. O estudo, os postos e as pessoas são inventados e foram sorteados por `gerar.py`. O resultado não serve para aconselhar ninguém sobre alimentação: ele existe para treinar a análise e os limites de um estudo.

Oito postos de atendimento. Quatro aderiram a um programa de orientação alimentar e quatro seguiram o atendimento de sempre. Cada participante anotou quantas porções de frutas e hortaliças comeu por dia, no começo (semana 0) e depois de 12 semanas.

## Arquivos

| Arquivo | Linhas | Colunas | Uma linha é |
|---|---|---|---|
| `postos.csv` | 8 | `posto`, `grupo` (`programa` ou `comparacao`) | um posto |
| `participantes.csv` | 240 | `id_participante`, `posto`, `faixa_etaria` | uma pessoa |
| `medidas.csv` | 456 | `id_participante`, `semana` (0 ou 12), `porcoes_dia` | uma medida de uma pessoa |

Quem não voltou para a medida da semana 12 não tem a linha dessa semana. Por isso `medidas.csv` tem menos de 480 linhas.

## Como gerar de novo

```bash
python3 gerar.py
```

A saída é `postos=8 participantes=240 medidas=456 sem_semana_12=24`. A semente é fixa, então os arquivos saem iguais toda vez.

O começo de `gerar.py` conta o mecanismo inteiro: quem escolheu aderir, quanto cada posto puxa o consumo, quem desiste e o tamanho da mudança. Faça a análise da aula 40 antes de abrir o gerador. Depois compare o que você concluiu com o que foi sorteado.
