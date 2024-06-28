from src.view.http_types.http_response import HttpResponse
from src.errors.types.http_400 import Http400Error
from src.errors.types.http_422 import Http422Error


def handle_erros(error: Exception) -> HttpResponse:
    print(str(error))
    if str(error) == "'NoneType' object has no attribute 'nome'":
        return handle_erros(Http400Error('Usuário Não encontrado'))
    elif str(error) == "'nome'":
        return handle_erros(Http400Error('Body incorreto, preencha dicionario com a key nome'))
    
    
    if isinstance(error, (Http400Error,Http422Error)):
        return HttpResponse(
            status_code= error.status_code,
            body={
                "erros": [
                    {
                        "title": error.name,
                        "detail":error.message
                    }
                ]
            }
        )
    else:
        return HttpResponse(
            status_code= 500,
            body = {
                "erros":[
                    {
                        "title":"Error não registrado",
                        "detail": str(error)
                    }
                ]
            }
        )