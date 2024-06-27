from src.view.http_types.http_response import HttpResponse
from src.errors.types.http_400 import Http400Error

def handle_erros(error: Exception) -> HttpResponse:

    if isinstance(error, Http400Error):
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