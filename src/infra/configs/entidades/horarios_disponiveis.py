
# Comando SQL para criar a tabela clientes
create_horarios_disponiveis_table_query = '''CREATE TABLE horarios (
    id_horario SERIAL PRIMARY KEY NOT NULL,
    horario TEXT NOT NULL,
    status BOOLEAN NOT NULL    
);'''