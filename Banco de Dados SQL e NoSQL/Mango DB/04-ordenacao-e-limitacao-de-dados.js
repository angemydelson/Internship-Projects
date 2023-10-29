/*
 Como buscar/filtrar dados de uma coleção com valores maiores que o especificado?

 Usamos o operador $gt

 gt = Greather than

*/

db.inscricoes.find(
	{
		"notas": {
			$gt: 8.0
		}
	}
)

/*
 Como buscar/filtrar dados de uma coleção com valores maiores ou igual o especificado?

 Usamos o operador $gte

 gte = Greather than or equal
 
*/

db.inscricoes.find(
	{
		"notas": {
			$gte: 8.0
		}
	}
)

db.inscricoes.insert(
	{
		"aluno": "Jair Rodrigues",
		"data_nascimento": new Date(1981, 06, 19),
		"curso": {
			"nome": "História"
		},
		"notas": [6, 7, 8, 5.5]
	}
)

db.inscricoes.insert(
	{
		"aluno": "Bruna Marquezi",
		"data_nascimento": new Date(1995, 02, 06),
		"curso": {
			 "nome": "História"
		},
		"notas": [10, 9.7, 6.5, 8.7]
	}
)

/*
 Como fazer para buscar apenas 1 resultado dentre possíveis vários?
*/

db.inscricoes.findOne(
	{
		"notas": {
			$gt: 7.7
		}
	}
)

/*
Como fazer para ordenar os resultados pelo nome (ordem alfabética)?

 O método sort() recebe um dado chave/valor, sendo a chave 
 o campo no qual queremos ordenar e o valor se a ordenação
 será crescente ou decrescente.

 1 para ordem crescente;
 -1 para ordem decrescente;

*/

db.inscricoes.find().sort({"aluno": 1}).pretty()

db.inscricoes.find().sort({"aluno": -1}).pretty()

/*
 Limitando os resultados....
*/

db.inscricoes.find().sort({"aluno": 1}).limit(3).pretty()

