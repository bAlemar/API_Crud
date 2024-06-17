CREATE TABLE IF NOT EXISTS Usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(50),
    endereco VARCHAR(100)
);
