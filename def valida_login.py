def valida_login(usuario, senha, status_da_conta):
    if status_da_conta == "inativo":
        mensagem = "Conta Inativa"
    elif usuario == "admin" and senha == "senha@123" and status_da_conta == "ativo":
        mensagem = "Login Bem-Sucedido"
    else:
        mensagem = "Credenciais incorretas"
    return mensagem