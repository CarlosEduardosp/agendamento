from fastapi import APIRouter
from src.main.adapter.adapter_cliente.adapter_cliente import AdapterCliente
from src.main.composer.cliente_composer.cliente_composer import register_cliente_composer

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.get('/select_cliente_by_id/{id}')
async def selecionar_cliente_by_id(id: int):
    """
    Seleciona todos os clientes do banco de dados.
    """
    # Criando uma instância do AdapterCliente
    request = AdapterCliente(
        api_route=register_cliente_composer(),
        data={'cliente_id': id}
    )

    # Chamando o método para selecionar os clientes
    response = request.select_by_id_adapter()
    if response:

        lista_pessoas = []
        for i in response.body:
            dados = {
                "id": i['id_cliente'],
                "nome": i['nome'],
                "data_nascimento": i['data_nasc'],
                "telefone1": i['telefone1'],
                "telefone2": i['telefone2'],
                "email": i['email'],
                "senha": i['senha']
            }
            lista_pessoas.append(dados)

        # Retornando a resposta
        return {'success': 200, 'body': lista_pessoas}

    return {'success': 200, 'body': 'Nenhum Cliente encontrado com o valor passado'}
