from flask import request as FlaskRequest
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse

def request_adapter(request: FlaskRequest) -> HttpResponse:
    http_request = HttpRequest(
        header=request.headers,
        body=request.json,
        query_params=request.args,
        url=request.full_path,
    )

    return http_request
