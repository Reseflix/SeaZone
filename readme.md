# SeaZone
Teste realizado para a vaga:Analista de Dados Jr.
> inicie com o arquivo start.py
# Dependencias 
    Bibliotecas utilizadas (informações completas em requirement.txt):
    - Pandas
    - Pathlib
    - Jupyter notebook
    - virtualenv
    Comandos:
    > pip install -r requirements.txt

# Utilização
    Caso seja necessario alguma alteração sobre nome das bases foi feito um arquivo em JSON para realizar as alterações.

    Utilizei Jupyter notebook para visualização da informação e executar os codigos sem a necessidade de recarregar os arquivos csv
    
    Utilezei o excel para realizar os graficos

# Perguntas do teste
- Existem correlações entre as características de um anúncio e seu faturamento?
> Sim, Informações como "star_rating" , "number_of_bedrooms" e "number_of_bathrooms" refletem sobre a qualidade e custo benefícios do imóvel assim levando em consideração propriedades economicas de "Demanda e oferta" esses valores tende a sobre alterações por seu consumo.

>Enquanto informações como "number_of_bedrooms" e "number_of_bathrooms" refletem uma certa prioridade ou visibilidade entre os consumidores, sendo os mais consumíveis: Imóveis com 2 banheiros e 2 quartos // com 1 banheiro e 1 quarto, mostrando um padrao de consumo de casais e solteiros.

- Qual a antecedência média das reservas?
> A media de antecedência para as reservas são um mes de antecedência (32 dias antes)

- Esse número é maior ou menor para finais de semana?
> A media ser mantem para os finais de semana sendo um mes de antecedência(32 dias antes)