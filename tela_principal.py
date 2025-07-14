import customtkinter as ctk
from telas.tela_cadastro import abrir_tela_cadastro

def abrir_tela_principal():
    app = ctk.CTk()
    app.title("Tela Principal")
    app.geometry("400x300")

    ctk.CTkLabel(app, text="Bem-vindo! Barbearia Onset").pack(pady=20)

    ctk.CTkButton(app, text="Cadastrar Cliente", command=abrir_tela_cadastro).pack(pady=10)
    ctk.CTkButton(app, text="Sair", command=app.destroy).pack(pady=10)

    app.mainloop()
