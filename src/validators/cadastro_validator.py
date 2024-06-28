from cerberus import Validator

def casdastro_validator(request: any):

    body_validator = Validator({
        "attributes": {
        "type":"dict",
        "schema":{
                "nome" : {"type":"string", "required":True, "empty":False},
                "telefone":{"type":"string", "required":True, "empty":True, "minlength":11,"maxlength":13},
                "email": {"type":"string", "required":True, "empty":False, "regex":r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"},
                "endereco": {"type":"string","required":True,"empty":False}
                }
             }
        })
    
    response = body_validator.validate(request.json)
    
    # Botar class de errors personalizados da Entidade
    if response is False:
        print(body_validator.errors)