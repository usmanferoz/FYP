import jwt


def encode_token(object):
    payload = {
        'id': object.id,
        'email': object.email,
        'user_type': object.user_type,
    }
    secret_key = "hypernym%lifemaster"

    token = jwt.encode(payload, secret_key, algorithm="HS256")
    if token:
        return token
    return None

def create_resonse(error, message, data=[]):
    kwargs = {
        "error": error,
        "message": message,
        "data": data
    }
    return kwargs