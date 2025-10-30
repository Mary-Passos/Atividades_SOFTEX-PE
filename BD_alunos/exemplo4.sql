.tables
.schema Aluno

SELECT data_nascimento
FROM Aluno
WHERE DATE(data_nascimento) > '2000-12-31';