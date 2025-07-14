import customtkinter as ctk
from telas import tela_login

if __name__ == "__main__":
    tela_login.abrir_tela_login()

from telas import tela_cadastro, tela_agendamento  # importa suas telas

def abrir_tela_principal():
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.title("Sistema Barbearia")
    app.geometry("400x300")

    titulo = ctk.CTkLabel(app, text="Menu Principal", font=ctk.CTkFont(size=20, weight="bold"))
    titulo.pack(pady=20)

    btn_cadastro = ctk.CTkButton(app, text="Cadastrar Cliente", width=200, height=40, command=tela_cadastro.abrir_tela_cadastro)
    btn_cadastro.pack(pady=10)

    btn_agendamento = ctk.CTkButton(app, text="Agendar Horário", width=200, height=40, command=tela_agendamento.abrir_tela_agendamento)
    btn_agendamento.pack(pady=10)

    btn_sair = ctk.CTkButton(app, text="Sair", width=200, height=40, fg_color="red", hover_color="#cc0000", command=app.destroy)
    btn_sair.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    abrir_tela_principal()


