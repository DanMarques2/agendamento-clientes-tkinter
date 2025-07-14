import customtkinter as ctk
import csv
import os

arquivo_csv = "dados/clientes.csv"

def abrir_tela_cadastro():
    clientes = []
    modo_edicao = False
    indice_edicao = None

    def carregar_clientes():
        if os.path.exists(arquivo_csv):
            with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as f:
                leitor = csv.reader(f)
                for linha in leitor:
                    if len(linha) == 3:
                        clientes.append(tuple(linha))
            atualizar_tabela()

    def salvar_todos_clientes_csv():
        os.makedirs("dados", exist_ok=True)
        with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerows(clientes)

    def cadastrar_ou_salvar():
        nonlocal modo_edicao, indice_edicao

        nome = entrada_nome.get().strip()
        telefone = entrada_telefone.get().strip()
        email = entrada_email.get().strip()

        if not nome or not telefone or not email:
            resultado.configure(text="Preencha todos os campos!", text_color="red")
            return

        if modo_edicao:
            clientes[indice_edicao] = (nome, telefone, email)
            resultado.configure(text="Cliente atualizado com sucesso!", text_color="green")
            modo_edicao = False
            indice_edicao = None
            botao_cadastrar.configure(text="Cadastrar Cliente")
        else:
            clientes.append((nome, telefone, email))
            resultado.configure(text="Cliente cadastrado com sucesso!", text_color="green")

        salvar_todos_clientes_csv()
        atualizar_tabela()
        limpar_campos()

    def editar_cliente(indice):
        nonlocal modo_edicao, indice_edicao

        nome, telefone, email = clientes[indice]
        entrada_nome.delete(0, ctk.END)
        entrada_nome.insert(0, nome)
        entrada_telefone.delete(0, ctk.END)
        entrada_telefone.insert(0, telefone)
        entrada_email.delete(0, ctk.END)
        entrada_email.insert(0, email)

        modo_edicao = True
        indice_edicao = indice
        botao_cadastrar.configure(text="Salvar Edição")
        resultado.configure(text="Editando cliente...", text_color="orange")

    def excluir_cliente(indice):
        clientes.pop(indice)
        salvar_todos_clientes_csv()
        atualizar_tabela()
        resultado.configure(text="Cliente removido.", text_color="red")

    def atualizar_tabela():
        for widget in frame_tabela.winfo_children():
            widget.destroy()

        ctk.CTkLabel(frame_tabela, text="Nome", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=0, padx=5, sticky="w")
        ctk.CTkLabel(frame_tabela, text="Telefone", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=1, padx=5, sticky="w")
        ctk.CTkLabel(frame_tabela, text="Email", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=2, padx=5, sticky="w")
        ctk.CTkLabel(frame_tabela, text="Ações", font=ctk.CTkFont(size=12, weight="bold")).grid(row=0, column=3, padx=5, sticky="w")

        for i, (nome, telefone, email) in enumerate(clientes, start=1):
            ctk.CTkLabel(frame_tabela, text=nome).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=telefone).grid(row=i, column=1, sticky="w", padx=5, pady=2)
            ctk.CTkLabel(frame_tabela, text=email).grid(row=i, column=2, sticky="w", padx=5, pady=2)

            frame_botoes = ctk.CTkFrame(frame_tabela, fg_color="transparent")
            frame_botoes.grid(row=i, column=3, padx=5, pady=2)

            ctk.CTkButton(frame_botoes, text="Editar", width=50, height=24, command=lambda i=i: editar_cliente(i)).pack(side="left", padx=2)
            ctk.CTkButton(frame_botoes, text="Excluir", width=50, height=24, fg_color="red", hover_color="#cc0000", command=lambda i=i: excluir_cliente(i)).pack(side="left", padx=2)

    def limpar_campos():
        entrada_nome.delete(0, ctk.END)
        entrada_telefone.delete(0, ctk.END)
        entrada_email.delete(0, ctk.END)

    # Criar janela como Toplevel (janela secundária)
    app = ctk.CTkToplevel()
    app.title("Cadastro de Clientes")
    app.geometry("600x500")

    frame_form = ctk.CTkFrame(app)
    frame_form.pack(pady=10, padx=15, fill="x")

    ctk.CTkLabel(frame_form, text="Nome:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entrada_nome = ctk.CTkEntry(frame_form, width=350)
    entrada_nome.grid(row=0, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame_form, text="Telefone:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entrada_telefone = ctk.CTkEntry(frame_form, width=350)
    entrada_telefone.grid(row=1, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame_form, text="E-mail:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    entrada_email = ctk.CTkEntry(frame_form, width=350)
    entrada_email.grid(row=2, column=1, padx=5, pady=5)

    botao_cadastrar = ctk.CTkButton(frame_form, text="Cadastrar Cliente", command=cadastrar_ou_salvar)
    botao_cadastrar.grid(row=3, column=0, columnspan=2, pady=15)

    resultado = ctk.CTkLabel(app, text="")
    resultado.pack()

    frame_tabela = ctk.CTkFrame(app)
    frame_tabela.pack(padx=15, pady=10, fill="both", expand=True)

    carregar_clientes()
