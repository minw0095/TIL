SELECT * 
FROM users INNER JOIN role
ON users.role_id = role.id
WHERE role.id = 2;

SELECT *
FROM users INNER JOIN role
ON users.role_id = role.id
ORDER BY users.name
DESC;

SELECT *
FROM articles LEFT OUTER JOIN users
ON articles.id = users.role_id
;
SELECt *
from articles join role join users
ON articles.id = users.role_id and users.role_id = role.id;