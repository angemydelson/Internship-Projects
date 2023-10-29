/*
Como inserir um novo campo em um documento existente?
*/

db.inscricoes.update(
	{"_id" : ObjectId("5d07ad35d4975e81d79dee18")},
	{
		$set: {
			"localizacao": {
				"endereco": "Avenida Zulmira Borba, 1978"
			}
		}
	}
)

/*
Como utilizar campos com coordenadas geográficas?

OBS: Quando vamos trabalhar com coordenadas geográficas com MongoDB
precisamos ter um campo chamado 'coordinates' e especificar o 'type'
*/

db.inscricoes.update(
	{"_id" : ObjectId("5d07ad35d4975e81d79dee18")},
	{
		$set: {
			"localizacao": {
				"endereco": "Avenida Zulmira Borba, 1978",
				"coordinates": [-20.388008, -54.577545],
				"type": "Point"
			}
		}
	}
)

/*
	Como importar dados para banco de dados MongoDB?

*/

a) Abra o terminal no mesmo diretório que está o arquivo contendo os dados;

b) Execute o comando abaixo: 

mongoimport -d meubanco -c inscricoes --jsonArray < inscricoes.json

Onde, 'meubanco' é o nome do banco dados, 'inscricoes' é o nome da coleção na qual
queremos importar os dados e por último 'inscricoes.json' é o arquivo contendo
os dados.

/*

Como utilizar os recursos avançados do MongoDB para buscar dados por localização?
*/ 

1 - Devemos informar ao MonboDB qual é o campo que deve ser utilizado como índice de busca.

db.inscricoes.createIndex(
	{
		"localizacao": "2dsphere"
	}
)

2 - Devemos realizar uma consulta utilizando agregação para que os cálculos sejam aplicados.

db.inscricoes.aggregate(
	[
		{
			$geoNear: {
				"near": {
					"coordinates": [-20.388008, -54.577546],
					"type": "Point"
				},
				"distanceField": "distancia.calculada",
				"spherical": true,
				"num": 4
			}
		}
	]
)

OBS: Na consulta acima, estamos trazendo 4 resultados, sendo que o primeiro é o próprio elemento da busca.

Caso queiramos ignorar o primeiro resultado, então devemos informar isso na consulta.


db.inscricoes.aggregate(
	[
		{
			$geoNear: {
				"near": {
					"coordinates": [-20.388008, -54.577546],
					"type": "Point"
				},
				"distanceField": "distancia.calculada",
				"spherical": true,
				"num": 4
			}
		},
		{
			$skip: 1
		}
	]
).pretty()
