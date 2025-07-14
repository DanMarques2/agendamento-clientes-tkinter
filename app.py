import customtkinter as ctk

# Configuração visual da interface
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

# Função que vai abrir a segunda janela após login
def abrir_tela_principal():
    # Criamos uma nova janela
    janela_principal = ctk.CTk()
    janela_principal.title("Tela Principal")
    janela_principal.geometry("400x300")

    # Label para mostrar uma mensagem
    label = ctk.CTkLabel(janela_principal, text="Bem-vindo(a) à Barbearia Onset!")
    label.pack(pady=40)

    # Botão para fechar essa janela
    botao_sair = ctk.CTkButton(janela_principal, text="Sair", command=janela_principal.destroy)
    botao_sair.pack(pady=20)

    # Inicia o loop da nova janela (fica mostrando até fechar)
    janela_principal.mainloop()

# Função que verifica login e abre a tela principal se tudo estiver certo
def realizar_login():
    usuario = entrada_usuario.get()  # Pega texto digitado no campo usuário
    senha = entrada_senha.get()      # Pega texto digitado no campo senha

    # Aqui você pode colocar a lógica de verificação de usuário e senha
    if usuario == "admin" and senha == "1234":
        resultado.configure(text="Login realizado com sucesso!", text_color="green")
        # Fecha a janela de login
        app.destroy()
        # Abre a tela principal
        abrir_tela_principal()
    else:
        resultado.configure(text="Usuário ou senha incorretos.", text_color="red")

# Criando a janela principal (de login)
app = ctk.CTk()
app.title("Barbearia Onset")
app.geometry("400x400")

# Criando o label (texto) e entrada de texto para o usuário
label_usuario = ctk.CTkLabel(app, text="Usuário:")
label_usuario.pack(pady=(30, 5))  # espaçamento de cima 30, de baixo 5
entrada_usuario = ctk.CTkEntry(app)
entrada_usuario.pack(pady=5)

# Label e entrada para senha
label_senha = ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=5)
entrada_senha = ctk.CTkEntry(app, show="*")  # show="*" esconde o texto digitado
entrada_senha.pack(pady=5)

# Botão para enviar os dados do login
botao_login = ctk.CTkButton(app, text="Entrar", command=realizar_login)
botao_login.pack(pady=20)

# Label para mostrar mensagem de sucesso ou erro
resultado = ctk.CTkLabel(app, text="")
resultado.pack()

# Inicia o loop principal da janela de login
app.mainloop()
