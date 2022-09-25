
# Extração e processamento de Pokémons

EP 01 de ciência de dados, sendo realizado a extração e processamento da base de Pokédex do site https://www.serebii.net/


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/tg-martins/EP01-EXTRACAO-PROCESSAMENTO-POKEMONS.git
```

Entre no diretório do projeto

```bash
  cd EP01-EXTRACAO-PROCESSAMENTO-POKEMONS
```

Instale as dependências

```bash
  pip install scrapy
  pip install pandas
  pip install mrjob 
```

Execute o script para realizar a extração dos dados e gerar o arquivo json

```bash
  scrapy runspider extract_pokemons.py -o pokemons.json
```

Execute o script para realizar a normalização dos dados para o arquivo em formato csv

```bash
  python normalize_csv.py
```
Execute o script para calcular as métricas dos pokemons utilizando o csv normalizado

```bash
  python analyze.py pokemons.csv
```



## Arquitetura

![App Screenshot](https://github.com/tg-martins/EP01-EXTRACAO-PROCESSAMENTO-POKEMONS/architecture.png)


## Referência

 - [MrJob](https://mrjob.readthedocs.io/)
 - [Scrapy](https://scrapy.org/)
 - [Pandas](https://pandas.pydata.org/)

