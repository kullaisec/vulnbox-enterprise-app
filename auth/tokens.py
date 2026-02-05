import jwt

SECRET = "kullai123"

def decode_token(token):
    return jwt.decode(token, SECRET, algorithms=["HS256"], options={"verify_exp": False})
