import requests

def buscar_usuario_api(user_id: int):
    r = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if r.status_code == 200:
        dados = r.json()
        return {"nome": dados["name"], "email": dados["email"]}
    return None
