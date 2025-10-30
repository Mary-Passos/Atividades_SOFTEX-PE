.tables
.schema Alunno 

SELECT ano, COUNT() as quantidade_turma
FROM Turma
GROUP BY ano
HAVING COUNT() > 2;