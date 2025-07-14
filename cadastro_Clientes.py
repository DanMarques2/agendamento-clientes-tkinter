import customtkinter as ctk

# Configurar aparência da interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Lista para armazenar os clientes cadastrados (em memória)
clientes = []

# Função para adicionar cliente na lista e atualizar tabela
def cadastrar_cliente():
    nome = entrada_nome.get().strip()
    telefone = entrada_telefone.get().strip()
    email = entrada_email.get().strip()

    # Validação simples: não deixar campos vazios
    if not nome or not telefone or not email:
        resultado.configure(text="Preencha todos os campos!", text_color="red")
        return

    # Adicionar cliente na lista
    clientes.append((nome, telefone, email))

    # Atualizar tabela
    atualizar_tabela()

    # Limpar campos após cadastro
    entrada_nome.delete(0, ctk.END)
    entrada_telefone.delete(0, ctk.END)
    entrada_email.delete(0, ctk.END)

    resultado.configure(text="Cliente cadastrado com sucesso!", text_color="green")

# Função para atualizar tabela de clientes na tela
def atualizar_tabela():
    # Limpar tabela antiga
    for widget in frame_tabela.winfo_children():
        widget.destroy()

    # Cabeçalho
    ctk.CTkLabel(frame_tabela, text="Nome", width=100, anchor="w", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=0, padx=5)
    ctk.CTkLabel(frame_tabela, text="Telefone", width=120, anchor="w", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=1, padx=5)
    ctk.CTkLabel(frame_tabela, text="E-mail", width=200, anchor="w", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=2, padx=5)

    # Inserir dados dos clientes
    for i, (nome, telefone, email) in enumerate(clientes, start=1):
        ctk.CTkLabel(frame_tabela, text=nome, width=100, anchor="w").grid(row=i, column=0, padx=5, pady=2)
        ctk.CTkLabel(frame_tabela, text=telefone, width=120, anchor="w").grid(row=i, column=1, padx=5, pady=2)
        ctk.CTkLabel(frame_tabela, text=email, width=200, anchor="w").grid(row=i, column=2, padx=5, pady=2)

# Criar janela principal
app = ctk.CTk()
app.title("Cadastro de Clientes")
app.geometry("480x400")

# Frame para formulário de cadastro
frame_form = ctk.CTkFrame(app)
frame_form.pack(pady=15, padx=15, fill="x")

# Campo Nome
ctk.CTkLabel(frame_form, text="Nome:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entrada_nome = ctk.CTkEntry(frame_form, width=300)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)

# Campo Telefone
ctk.CTkLabel(frame_form, text="Telefone:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entrada_telefone = ctk.CTkEntry(frame_form, width=300)
entrada_telefone.grid(row=1, column=1, padx=5, pady=5)

# Campo Email
ctk.CTkLabel(frame_form, text="E-mail:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entrada_email = ctk.CTkEntry(frame_form, width=300)
entrada_email.grid(row=2, column=1, padx=5, pady=5)

# Botão cadastrar
botao_cadastrar = ctk.CTkButton(frame_form, text="Cadastrar Cliente", command=cadastrar_cliente)
botao_cadastrar.grid(row=3, column=0, columnspan=2, pady=15)

# Label para resultado (sucesso/erro)
resultado = ctk.CTkLabel(app, text="")
resultado.pack()

# Frame para tabela de clientes
frame_tabela = ctk.CTkFrame(app)
frame_tabela.pack(padx=15, pady=10, fill="both", expand=True)

# Inicializa tabela vazia
atualizar_tabela()

# Rodar app
app.mainloop()
