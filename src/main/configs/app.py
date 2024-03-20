from fastapi import FastAPI
from .rotas.rota_inicial import inicio
from .rotas.rota_cliente import select_clientes, insert_cliente, select_by_id, deletar_cliente, update_cliente
from .rotas.rota_agendamento import insert_agendamento, select_agendamento, select_agendamento_by_id, delete_agendamento
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# rota de inicio da API
app.include_router(inicio.router, tags=["Mensagem inicial API."])

# rotas de manipulação de dados, dos clientes.
app.include_router(select_clientes.router, tags=["Seleciona todos os clientes do banco de dados."])
app.include_router(select_by_id.router, tags=["seleciona cliente pelo id de registro."])
app.include_router(insert_cliente.router, tags=["Realiza a inserção de clientes no banco de dados."])
app.include_router(deletar_cliente.router, tags=["Realiza a remoção de clientes no banco de dados pelo id."])
app.include_router(update_cliente.router, tags=["Realiza a atualização de clientes no banco de dados pelo id."])

# rotas de agendamento
app.include_router(insert_agendamento.router, tags=["Realiza a inserção de agendamentos no banco de dados."])
app.include_router(select_agendamento.router, tags=["Seleciona os agendamentos no banco de dados."])
app.include_router(select_agendamento_by_id.router, tags=["Seleciona os agendamentos no banco de dados pelo id do cliente."])
app.include_router(delete_agendamento.router, tags=["Deleta os agendamentos no banco de dados pelo id do agendamento."])


# Lista de origens permitidas
allowed_origins = [
    "http://www.icnvararuama.com.br",
    "https://www.icnvararuama.com.br",
    "http://170.231.112.194",
    "http://icnvararuama.netlify.app",
    "https://icnvararuama.netlify.app",
    "http://2600:1f1e:c3c:f302::c8",
    "http://2600:1f1e:c3c:f301::c8",
    "http://52.67.97.86",
    "http://177.71.195.255",
    "http://170.231.112.205"
]

# Configurar CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Substitua pelo domínio do seu aplicativo, * para todos os dominios
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],  # Você pode especificar métodos permitidos, como ["GET", "POST"]
    allow_headers=["Authorization"],  # Você pode especificar cabeçalhos permitidos, como ["Authorization"]
)



