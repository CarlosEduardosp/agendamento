
# Comando SQL para criar a tabela clientes
create_agendamento_table_query = '''CREATE TABLE agendamento (
    id_agendamento SERIAL PRIMARY KEY NOT NULL,
    id_servico INTEGER NOT NULL,
    data VARCHAR(8) NOT NULL,
    horario VARCHAR(20) NOT NULL,
    id_cliente INTEGER NOT NULL    
);'''