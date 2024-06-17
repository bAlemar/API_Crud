from flask import Blueprint, request, jsonify
api = Blueprint("api_routes", __name__)

from src.main.adapter.request_adapter import request_adapter
from src.main.composer.cadastro_composer import cadastro_composer


@api.route("/cadastro", methods=["POST"])
def calculate():
    calculator_view = cadastro_composer()
    
    http_request = request_adapter(request)
    http_response = calculator_view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
