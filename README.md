# Smartphone Classifier

Um classificador que prevê, para cada produto, sua característica: 'smartphone' ou 'nao-smartphone'.

## Descrição dos arquivos

- **trainer.py**: script responsável pelo treinamento do classificador. O modelo gerado é salvo em smartphone_classifier e utilizado no arquivo classificador. Quando executado, também exibe informações sobre o modelo, em um teste realizado com 70% das entradas.

- **classifier.py**: classificador final. Utiliza o arquivo smartphone_classifier para prever a categoria de cada título. As respostas são salvas no arquivo output.csv. Quando executado, também exibe informações sobre as previsões realizadas em todas as entradas.

- **general.py**: contém funções utilizadas para carregamento e pré-processamento do dataset.

- **data_estag_ds.tv**: conjunto de títulos disponibilizado.

- **y_file.csv**: classificação dos títulos, realizada manualmente, em 'smartphone' ou 'nao-smartphone'. Ele é utilizado como parâmetro para o treinamento e análise dos resultados do classificador.

- **output_file.csv**: arquivo de resposta. Para cada título, exibe sua categoria prevista.

- **smartphone_classifier**: modelo de classificador salvo após a execução de trainer.py.

## Como utilizar

O classificador foi desenvolvido em Python, utilizando as bibliotecas: Numpy, CSV, Pickle, Pandas e re. 

O classificador pode ser gerado e treinado executando o arquivo *trainer.py*. O modelo gerado é salvo em *smartphone_classifier*. 

Para realizar a classificação, basta executar *classifier.py*. Este arquivo utiliza o modelo salvo em *smartphone_classifier* para a classificação. Em seguida, os resultados são registrados em *output_file.csv*.

#### Observações

- São disponibilizados os arquivos *smartphone_classifier* e *output_file.csv*, caso queira utilizar o modelo adicionado ao repositório mais recentemente, ou visualizar os últimos resultados. Logo, é possível também testar o classificador, ao executar *classifier.py*, sem ter executado anteriormente *trainer.py*.

- A técnica de Aprendizado de Máquina utilizada corresponde ao Random Forest Classifier.

- Como a base de dados é relativamente pequena e de fácil anotação, todos os dados foram classificados manualmente e disponibilizados em *y_file.csv*, de maneira que pudesse ser utilizado para treinamento e análise dos resultados do classificador. 
