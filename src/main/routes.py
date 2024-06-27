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


from src.main.composer.search_compose import search_composer

@api.route("/search",methods=["POST"])
def search():
    search_view = search_composer()

    http_request = request_adapter(request)
    http_response = search_view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code


from src.main.composer.delete_compose import delete_composer

@api.route("/delete",methods=["POST"])
def delete():
    delete_view = delete_composer()
    http_request = request_adapter(request)
    http_response = delete_view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code


from src.main.composer.update_composer import update_composer

@api.route("/update",methods=["POST"])
def update():
    update_view = update_composer()
    http_request = request_adapter(request)
    http_response = update_view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code


# Perguntar...
@api.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Página não encontrada"}), 404