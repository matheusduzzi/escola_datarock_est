# 40. Case de nutrição: análise e defesa

Os arquivos da aula «Case de nutrição: análise e defesa» do curso Estatística para decisão.

## Os dados da aula

| Arquivo | Uma linha é | Colunas |
|---|---|---|
| `dados/refeitorios.csv` | um refeitório | `refeitorio` (A a F) e `grupo` (`salada_primeiro` nos três sorteados para pôr a salada no começo do bufê a partir de 05/10/2026, `ordem_de_sempre` nos outros três) |
| `dados/bandejas.csv` | uma bandeja, um almoço de uma pessoa num dia | `data`, `refeitorio`, `cracha`, `periodo` (`antes`: 14 a 25/09/2026; `depois`: 19 a 30/10/2026) e `salada_g` (gramas de salada servida na bandeja, pesada no fim do bufê) |

São os mesmos dois arquivos da aula 39, «Case de nutrição: pergunta e desenho».

## Os arquivos de código

- `relatorio_refeitorios.py` refaz todos os números do relatório da aula, na ordem do relatório.
- `distribuicao_t.py` dá o número da tabela t para o intervalo de Welch, só com a biblioteca padrão. É o mesmo das aulas 37 e 38.

## Os dados do exercício

O exercício usa o estudo de orientação alimentar, que fica em `../dados/nutricao/`, uma pasta acima dessa, como na aula 39. A folha `modelo-relatorio.md` tem as cinco partes do relatório. Salve uma cópia com o seu nome e escreva o seu `relatorio_orientacao.py` nessa pasta.

O `LEIA-ME.md` de `../dados/nutricao/` fala do `gerar.py`. Abra o gerador só depois de entregar o relatório.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta, só com o pandas que o README do kit já instala:

```bash
python3
```

Depois cole os blocos da aula na ordem, da seção 4 à seção 7. Os caminhos começam em `dados/`. O pedido 2 da prática usa a tabela `mudanca` e as funções das seções 5 e 6.

Para refazer o relatório inteiro de uma vez:

```bash
python3 relatorio_refeitorios.py
```

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
