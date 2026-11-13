# Kit do curso Estatística para decisão

Os arquivos que você usa nas aulas: o diagnóstico, a preparação de matemática, os tíquetes e as entregas da Loja Exemplo e o estudo de orientação alimentar das aulas 39 e 40.

## Como o kit está organizado

| Pasta | O que tem |
|---|---|
| `00-apresentacao/` | O [diagnóstico](00-apresentacao/diagnostico.md), a [preparação de matemática](00-apresentacao/preparacao-matematica.md), os dados e programas das tarefas, a [folha de respostas](00-apresentacao/minhas-respostas.md), a [folha da ordem de estudo](00-apresentacao/minha-ordem.md) e o `primeira_olhada.py` da apresentação. |
| `dados/loja/` | Tíquetes de 400 pedidos e horas de 48 entregas da Loja Exemplo. Ver [dados/loja/LEIA-ME.md](dados/loja/LEIA-ME.md). |
| `dados/nutricao/` | Postos, participantes e medidas do estudo de orientação alimentar. Ver [dados/nutricao/LEIA-ME.md](dados/nutricao/LEIA-ME.md). |
| `NN-titulo/` | Uma pasta por aula, com o número e o título da aula. Elas entram no kit junto com as aulas. |

Os comandos das aulas rodam de dentro da pasta da aula. Quando uma aula usa uma base compartilhada, ela diz o caminho, por exemplo `../dados/loja/entregas.csv`.

## Do que você precisa

- Python 3.9 ou mais novo, com o pandas. É o ambiente de Primeiros passos em dados: SQL e Python para quem está migrando; se você ainda não preparou o seu, a aula 03. Preparar o ambiente, de lá, mostra como.
- Um editor de código e um terminal.

O NumPy vem junto com o pandas. O SciPy, que faz os testes e as distribuições, e a biblioteca de gráficos entram nas aulas que usam cada um, com a versão e o comando de instalação. As aulas mostram o código pronto e explicam linha por linha o que ele calcula: o foco é o raciocínio, não escrever a implementação sozinho.

Na pasta do kit, instale o que o diagnóstico usa:

```bash
python3 -m pip install -r requirements.txt
```

E veja se funcionou:

```bash
cd 00-apresentacao
python3 tarefa4.py
```

A saída tem duas linhas de números. Não olhe ainda: a tarefa 4 do diagnóstico pede para você prever essas linhas antes de rodar. Se aparecer `No module named 'pandas'`, o `pip` instalou em outro Python. Rode `python3 -m pip install pandas` com o mesmo `python3` que você usa para rodar o programa. No Windows, troque `python3` por `py`.

Para gerar de novo as bases compartilhadas:

```bash
cd ../dados/loja
python3 gerar.py
cd ../nutricao
python3 gerar.py
```

As saídas são `tiquetes=400 entregas=48 entregas_sem_baixa=3` e `postos=8 participantes=240 medidas=456 sem_semana_12=24`. Os dois geradores só usam a biblioteca padrão e saem iguais toda vez.

## Se precisar de ajuda

Deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.

## Licença

A licença de uso e redistribuição do kit ainda vai ser definida pela Escola Datarock. Até lá, use os arquivos para estudar o curso. Os dados da Loja Exemplo e do estudo de orientação alimentar são inventados e foram gerados pelos programas do próprio kit.

## Aulas com arquivos neste kit

| Pasta | Aula |
|---|---|
| [00-apresentacao/](00-apresentacao/) | Apresentação |
| [01-o-que-queremos-estimar/](01-o-que-queremos-estimar/) | O que queremos estimar |
| [02-como-a-amostra-foi-formada/](02-como-a-amostra-foi-formada/) | Como a amostra foi formada |
| [03-media-mediana-e-extremos/](03-media-mediana-e-extremos/) | Média, mediana e extremos |
| [04-dispersao-e-escala/](04-dispersao-e-escala/) | Dispersão e escala |
| [05-descrever-distribuicao/](05-descrever-distribuicao/) | Descrever distribuição |
| [06-investigar-valores-extremos/](06-investigar-valores-extremos/) | Investigar valores extremos |
| [07-ausencia-de-dados-e-incerteza/](07-ausencia-de-dados-e-incerteza/) | Ausência de dados e incerteza |
| [08-covariancia-e-correlacao/](08-covariancia-e-correlacao/) | Covariância e correlação |
| [09-investigar-associacoes/](09-investigar-associacoes/) | Investigar associações |
| [10-por-que-associacao-nao-demonstra-causa/](10-por-que-associacao-nao-demonstra-causa/) | Por que associação não demonstra causa |
| [11-revisar-uma-conclusao-causal/](11-revisar-uma-conclusao-causal/) | Revisar uma conclusão causal |
| [12-eventos-e-regras-de-probabilidade/](12-eventos-e-regras-de-probabilidade/) | Eventos e regras de probabilidade |
| [13-condicional-e-independencia/](13-condicional-e-independencia/) | Condicional e independência |
| [14-bayes-e-taxa-base/](14-bayes-e-taxa-base/) | Bayes e taxa-base |
| [15-variaveis-aleatorias-e-esperanca/](15-variaveis-aleatorias-e-esperanca/) | Variáveis aleatórias e esperança |
| [16-bernoulli-binomial-e-hipergeometrica/](16-bernoulli-binomial-e-hipergeometrica/) | Bernoulli, binomial e hipergeométrica |
| [17-poisson-e-geometrica/](17-poisson-e-geometrica/) | Poisson e geométrica |
| [18-normal-e-exponencial/](18-normal-e-exponencial/) | Normal e exponencial |
| [19-distribuicoes-t-e-qui-quadrado/](19-distribuicoes-t-e-qui-quadrado/) | Distribuições t e qui-quadrado |
| [20-simular-e-confrontar-um-modelo/](20-simular-e-confrontar-um-modelo/) | Simular e confrontar um modelo |
| [21-lei-dos-grandes-numeros-e-limite-central/](21-lei-dos-grandes-numeros-e-limite-central/) | Lei dos grandes números e limite central |
| [22-distribuicao-amostral-por-simulacao/](22-distribuicao-amostral-por-simulacao/) | Distribuição amostral por simulação |
| [23-estimadores-vies-e-precisao/](23-estimadores-vies-e-precisao/) | Estimadores, viés e precisão |
| [24-intervalo-de-confianca-e-cobertura/](24-intervalo-de-confianca-e-cobertura/) | Intervalo de confiança e cobertura |
| [25-bootstrap-e-suas-hipoteses/](25-bootstrap-e-suas-hipoteses/) | Bootstrap e suas hipóteses |
| [26-intervalo-para-media-de-entregas/](26-intervalo-para-media-de-entregas/) | Intervalo para média de entregas |
| [27-intervalo-para-proporcao/](27-intervalo-para-proporcao/) | Intervalo para proporção |
| [28-margem-de-erro-e-sensibilidade/](28-margem-de-erro-e-sensibilidade/) | Margem de erro e sensibilidade |
| [29-hipoteses-e-distribuicao-nula/](29-hipoteses-e-distribuicao-nula/) | Hipóteses e distribuição nula |
| [30-a-senhora-que-prova-cha/](30-a-senhora-que-prova-cha/) | A senhora que prova chá |
| [31-p-valor-erros-e-relevancia/](31-p-valor-erros-e-relevancia/) | P-valor, erros e relevância |
| [32-poder-e-planejamento-de-amostra/](32-poder-e-planejamento-de-amostra/) | Poder e planejamento de amostra |
| [33-comparar-medias-independentes-e-pareadas/](33-comparar-medias-independentes-e-pareadas/) | Comparar médias independentes e pareadas |
| [34-anova-e-comparacoes-entre-grupos/](34-anova-e-comparacoes-entre-grupos/) | ANOVA e comparações entre grupos |
| [35-aplicar-anova-e-interpretar-limites/](35-aplicar-anova-e-interpretar-limites/) | Aplicar ANOVA e interpretar limites |
| [36-familias-de-testes-e-multiplicidade/](36-familias-de-testes-e-multiplicidade/) | Famílias de testes e multiplicidade |
| [37-metodos-nao-parametricos-e-permutacao/](37-metodos-nao-parametricos-e-permutacao/) | Métodos não paramétricos e permutação |
| [38-comparar-conclusoes-sob-metodos-distintos/](38-comparar-conclusoes-sob-metodos-distintos/) | Comparar conclusões sob métodos distintos |
| [39-case-de-nutricao-pergunta-e-desenho/](39-case-de-nutricao-pergunta-e-desenho/) | Case de nutrição: pergunta e desenho |
| [40-case-de-nutricao-analise-e-defesa/](40-case-de-nutricao-analise-e-defesa/) | Case de nutrição: análise e defesa |
| [41-nota-de-decisao-sobre-prazo-de-entrega/](41-nota-de-decisao-sobre-prazo-de-entrega/) | Nota de decisão sobre prazo de entrega |
| [42-banca-de-interpretacao/](42-banca-de-interpretacao/) | Banca de interpretação |
