from datetime import datetime

def enviar_email_boas_vindas(usuario: dict):
    mensagem = f"Olá {usuario['nome']}, bem-vindo ao sistema!"
    print(f"[EMAIL SIMULADO] Enviando para {usuario['email']}: {mensagem}")
    salvar_log_email(usuario, mensagem)

def salvar_log_email(usuario: dict, mensagem: str):
    with open("log_email.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {usuario['email']} - {mensagem}\n")
