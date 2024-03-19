from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def inicio():
    """
    :return: rota inicial da api.
    """

    data = {
        "success": 200,
        "mensagem": "Api rodando perfeitamente"
    }

    return data
