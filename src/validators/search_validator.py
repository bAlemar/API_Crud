from cerberus import Validator
from src.errors.types.http_422 import Http422Error
from typing import Dict
def search_validator(body: Dict):

    body_validator = Validator({
       "nome":{"type":"string", "required":True, "empty":False}
        })
    
    response = body_validator.validate(body)
    if response is False:
        raise Http422Error(body_validator.errors)