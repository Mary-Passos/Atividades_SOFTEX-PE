.tables
.schema Aluno

SELECT ano, COUNT() as quantidade_turma
FROM turma
GROUP BY ano;
