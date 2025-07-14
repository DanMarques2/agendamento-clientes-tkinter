import customtkinter as ctk
from main import abrir_tela_principal

USUARIO_PADRAO = "admin"
SENHA_PADRAO = "123"

def abrir_tela_login():
    def verificar_login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        if usuario == USUARIO_PADRAO and senha == SENHA_PADRAO:
            resultado.configure(text="Login bem-sucedido!", text_color="green")
            login_janela.destroy()
            abrir_tela_principal()
        else:
            resultado.configure(text="Usuário ou senha incorretos.", text_color="red")

    login_janela = ctk.CTk()
    login_janela.title("Login")
    login_janela.geometry("300x250")

    ctk.CTkLabel(login_janela, text="Usuário:").pack(pady=5)
    entrada_usuario = ctk.CTkEntry(login_janela)
    entrada_usuario.pack()

    ctk.CTkLabel(login_janela, text="Senha:").pack(pady=5)
    entrada_senha = ctk.CTkEntry(login_janela, show="*")
    entrada_senha.pack()

    ctk.CTkButton(login_janela, text="Entrar", command=verificar_login).pack(pady=15)

    resultado = ctk.CTkLabel(login_janela, text="")
    resultado.pack()

    login_janela.mainloop()

