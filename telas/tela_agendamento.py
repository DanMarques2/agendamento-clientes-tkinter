from datetime import datetime
import customtkinter as ctk
import csv
import os

arquivo_csv = "dados/agendamentos.csv"
agendamentos = []

def abrir_tela_agendamento():
    modo_edicao = False
    indice_edicao = None

    def carregar_agendamentos():
        if os.path.exists(arquivo_csv):
            with open(arquivo_csv, mode="r", newline="", encoding="utf-8") as f:
                leitor = csv.reader(f)
                for linha in leitor:
                    if len(linha) == 4:
                        agendamentos.append(tuple(linha))
            atualizar_lista()

    def salvar_todos_agendamentos_csv():
        os.makedirs("dados", exist_ok=True)
        with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerows(agendamentos)

    def adicionar_ou_editar_agendamento():
        nonlocal modo_edicao, indice_edicao

        nome = entrada_nome.get().strip()
        data = entrada_data.get().strip()
        horario = entrada_horario.get().strip()
        servico = combo_servico.get()

        if not nome or not data or not horario or servico == "":
            resultado.configure(text="Preencha todos os campos!", text_color="red")
            return

        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            resultado.configure(text="Data inválida! Use o formato dd/mm/aaaa.", text_color="red")
            return

        try:
            datetime.strptime(horario, "%H:%M")
        except ValueError:
            resultado.configure(text="Horário inválido! Use o formato hh:mm (24h).", text_color="red")
            return

        if modo_edicao:
            agendamentos[indice_edicao] = (nome, data, horario, servico)
            resultado.configure(text="Agendamento atualizado!", text_color="green")
            modo_edicao = False
            indice_edicao = None
            botao_adicionar.configure(text="Agendar")
        else:
            agendamentos.append((nome, data, horario, servico))
            resultado.configure(text="Agendamento realizado!", text_color="green")

        salvar_todos_agendamentos_csv()
        atualizar_lista()
        limpar_campos()

    def editar_agendamento(indice):
        nonlocal modo_edicao, indice_edicao
        nome, data, horario, servico = agendamentos[indice]
        entrada_nome.delete(0, ctk.END)
        entrada_nome.insert(0, nome)
        entrada_data.delete(0, ctk.END)
        entrada_data.insert(0, data)
        entrada_horario.delete(0, ctk.END)
        entrada_horario.insert(0, horario)
        combo_servico.set(servico)

        modo_edicao = True
        indice_edicao = indice
        botao_adicionar.configure(text="Salvar Edição")
        resultado.configure(text="Editando agendamento...", text_color="orange")

    def excluir_agendamento(indice):
        agendamentos.pop(indice)
        salvar_todos_agendamentos_csv()
        atualizar_lista()
        resultado.configure(text="Agendamento removido.", text_color="red")

    def limpar_campos():
        entrada_nome.delete(0, ctk.END)
        entrada_data.delete(0, ctk.END)
        entrada_horario.delete(0, ctk.END)
        combo_servico.set("")

    def atualizar_lista():
        for widget in frame_lista.winfo_children():
            widget.destroy()

        headers = ["Nome", "Data", "Horário", "Serviço", "Ações"]
        for col, text in enumerate(headers):
            ctk.CTkLabel(frame_lista, text=text, font=ctk.CTkFont(weight="bold")).grid(row=0, column=col, padx=5)

        for i, (nome, data, horario, servico) in enumerate(agendamentos, start=1):
            ctk.CTkLabel(frame_lista, text=nome).grid(row=i, column=0, padx=5, pady=2, sticky="w")
            ctk.CTkLabel(frame_lista, text=data).grid(row=i, column=1, padx=5, pady=2, sticky="w")
            ctk.CTkLabel(frame_lista, text=horario).grid(row=i, column=2, padx=5, pady=2, sticky="w")
            ctk.CTkLabel(frame_lista, text=servico).grid(row=i, column=3, padx=5, pady=2, sticky="w")

            botoes = ctk.CTkFrame(frame_lista, fg_color="transparent")
            botoes.grid(row=i, column=4, padx=5)

            ctk.CTkButton(botoes, text="Editar", width=50, command=lambda i=i: editar_agendamento(i)).pack(side="left", padx=2)
            ctk.CTkButton(botoes, text="Excluir", width=50, fg_color="red", hover_color="#cc0000", command=lambda i=i: excluir_agendamento(i)).pack(side="left", padx=2)

    # Interface
    app = ctk.CTk()
    app.title("Agendamento de Horários")
    app.geometry("700x500")

    frame_form = ctk.CTkFrame(app)
    frame_form.pack(pady=15, padx=15, fill="x")

    ctk.CTkLabel(frame_form, text="Nome do cliente:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entrada_nome = ctk.CTkEntry(frame_form, width=250)
    entrada_nome.grid(row=0, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame_form, text="Data (dd/mm/aaaa):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entrada_data = ctk.CTkEntry(frame_form, width=150)
    entrada_data.grid(row=1, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame_form, text="Horário (hh:mm):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    entrada_horario = ctk.CTkEntry(frame_form, width=150)
    entrada_horario.grid(row=2, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame_form, text="Serviço:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    combo_servico = ctk.CTkComboBox(frame_form, values=["Corte", "Barba", "Sobrancelha", "Hidratação"])
    combo_servico.grid(row=3, column=1, padx=5, pady=5)
    combo_servico.set("")

    botao_adicionar = ctk.CTkButton(frame_form, text="Agendar", command=adicionar_ou_editar_agendamento)
    botao_adicionar.grid(row=4, column=0, columnspan=2, pady=15)

    resultado = ctk.CTkLabel(app, text="")
    resultado.pack()

    frame_lista = ctk.CTkFrame(app)
    frame_lista.pack(padx=15, pady=10, fill="both", expand=True)

    carregar_agendamentos()

    app.mainloop()


    ...

