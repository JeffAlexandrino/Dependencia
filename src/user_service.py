from typing import List, Dict
from rich.table import Table
from rich.console import Console

usuarios: List[Dict] = []
console = Console()

def adicionar_usuario(nome: str, email: str) -> Dict:
    usuario = {
        "id": len(usuarios) + 1,
        "nome": nome,
        "email": email,
        "ativo": True
    }
    usuarios.append(usuario)
    return usuario

def listar_usuarios():
    if not usuarios:
        console.print("[yellow]Nenhum usuário cadastrado.[/yellow]")
        return
    tabela = Table(title="Lista de Usuários")
    tabela.add_column("ID", style="cyan")
    tabela.add_column("Nome", style="green")
    tabela.add_column("Email", style="magenta")
    tabela.add_column("Status", style="red")

    for u in usuarios:
        status = "Ativo" if u["ativo"] else "Inativo"
        tabela.add_row(str(u["id"]), u["nome"], u["email"], status)

    console.print(tabela)

def desativar_usuario(user_id: int) -> bool:
    for u in usuarios:
        if u["id"] == user_id:
            u["ativo"] = False
            return True
    return False
