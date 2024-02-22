# Comando SQL para criar a tabela clientes
create_clientes_table_query = '''CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    data_nasc VARCHAR(10) NOT NULL,
    telefone1 VARCHAR(20) NOT NULL,
    telefone2 VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    senha TEXT NOT NULL
);'''