# 39. Case de nutrição: pergunta e desenho

Os arquivos da aula «Case de nutrição: pergunta e desenho» do curso Estatística para decisão.

## Os dados da aula

| Arquivo | Uma linha é | Colunas |
|---|---|---|
| `dados/refeitorios.csv` | um refeitório | `refeitorio` (A a F) e `grupo` (`salada_primeiro` nos três sorteados para pôr a salada no começo do bufê a partir de 05/10/2026, `ordem_de_sempre` nos outros três) |
| `dados/bandejas.csv` | uma bandeja, um almoço de uma pessoa num dia | `data`, `refeitorio`, `cracha`, `periodo` (`antes`: 14 a 25/09/2026; `depois`: 19 a 30/10/2026) e `salada_g` (gramas de salada servida na bandeja, pesada no fim do bufê) |

## Os dados do exercício

O exercício usa o estudo de orientação alimentar, que fica em `../dados/nutricao/`, uma pasta acima dessa. Leia o `LEIA-ME.md` de lá, mas não abra o `gerar.py`: ele conta como os números foram sorteados, e isso é assunto da próxima aula.

## A folha da ficha

`ficha-desenho.md` é a folha do exercício, com as seis partes da ficha da aula. Salve uma cópia com o seu nome.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta, só com o pandas que o README do kit já instala:

```bash
python3
```

Depois cole os blocos da aula na ordem. Os caminhos começam em `dados/`. Os blocos da seção 5 e o pedido 2 usam a tabela `b` já juntada com os refeitórios, então rode a seção 4 primeiro.

Os dois arquivos vêm prontos e são sempre os mesmos.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
