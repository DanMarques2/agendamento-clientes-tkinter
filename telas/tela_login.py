import customtkinter as ctk
from main import abrir_tela_principal  # Importa o menu principal

def abrir_tela_login():
    def realizar_login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        if usuario == "admin" and senha == "1234":
            resultado.configure(text="Login realizado com sucesso!", text_color="green")
            login_janela.destroy()
            abrir_tela_principal()
        else:
            resultado.configure(text="Usuário ou senha incorretos.", text_color="red")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    login_janela = ctk.CTk()
    login_janela.title("Login - Barbearia Onset")
    login_janela.geometry("400x300")

    ctk.CTkLabel(login_janela, text="Usuário:").pack(pady=(30, 5))
    entrada_usuario = ctk.CTkEntry(login_janela)
    entrada_usuario.pack(pady=5)

    ctk.CTkLabel(login_janela, text="Senha:").pack(pady=5)
    entrada_senha = ctk.CTkEntry(login_janela, show="*")
    entrada_senha.pack(pady=5)

    ctk.CTkButton(login_janela, text="Entrar", command=realizar_login).pack(pady=20)

    resultado = ctk.CTkLabel(login_janela, text="")
    resultado.pack()

    login_janela.mainloop()
