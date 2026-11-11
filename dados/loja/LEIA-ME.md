# Tíquetes e entregas da Loja Exemplo

A Loja Exemplo não existe. Os pedidos e as entregas são números sorteados por `gerar.py`, que só usa a biblioteca padrão do Python. Nenhum dado vem de cliente, pessoa ou empresa real.

## Arquivos

| Arquivo | Linhas | Colunas | Uma linha é |
|---|---|---|---|
| `tiquetes.csv` | 400 | `id_pedido`, `canal` (`site` ou `loja_fisica`), `valor` em reais | um pedido |
| `entregas.csv` | 48 | `id_entrega`, `horas` do pedido até a baixa da entrega | uma entrega |

Em `entregas.csv`, a célula de `horas` fica vazia quando a baixa não foi anotada. Vazio não é zero: a entrega existiu, só não sabemos quanto tempo levou.

## Como gerar de novo

```bash
python3 gerar.py
```

A saída é `tiquetes=400 entregas=48 entregas_sem_baixa=3`. A semente é fixa, então os arquivos saem iguais toda vez. O começo de `gerar.py` diz como cada número nasce: que distribuição, que parâmetros e que caso foi colocado de propósito. Numa loja de verdade, ninguém conhece esses parâmetros. Nas aulas, você calcula primeiro e só depois abre o gerador para comparar.

Não edite os CSVs à mão. Se uma aula precisar de outro caso, ela traz os arquivos dela na própria pasta.
