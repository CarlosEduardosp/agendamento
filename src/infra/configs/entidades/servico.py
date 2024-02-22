
# Comando SQL para criar a tabela clientes
create_servico_table_query = '''CREATE TABLE servico (
    id_servico SERIAL PRIMARY KEY NOT NULL,
    nome_servico TEXT NOT NULL, 
    descricao_servico TEXT NOT NULL
    );'''