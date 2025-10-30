.tables
.schema Aluno

SELECT id_turma, AVG(nota1) as media_nota1
FROM Aluno
GROUP BY id_turma;