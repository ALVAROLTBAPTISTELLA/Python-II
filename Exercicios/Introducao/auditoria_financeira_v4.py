import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os
import re
import subprocess

LOG_GERAL = "relatorio_auditoria.txt"

CARGOS = [
    "Analista",
    "Supervisor",
    "Gerente",
    "Diretor"
]

CATEGORIAS = {
    "Transporte": 150.00,
    "Alimentação": 85.00,
    "Hospedagem": 450.00
}


class SistemaAuditoria:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Auditoria Financeira v4.0")
        self.root.geometry("650x450")
        self.root.resizable(False, False)

        self.criar_interface()

    # -------------------------------------------------
    # UTILITÁRIOS
    # -------------------------------------------------

    def sanitizar_nome_arquivo(self, texto):
        return re.sub(r'[<>:"/\\|?*]', "_", texto)

    def gerar_parecer(self, categoria, valor):

        if valor <= 0:
            return "NEGADO - valor deve ser maior que zero."

        teto = CATEGORIAS.get(categoria)

        if teto is None:
            return "NEGADO - categoria não reconhecida."

        if valor <= teto:
            return (
                f"APROVADO AUTOMATICAMENTE - dentro do teto de "
                f"{categoria.lower()}."
            )

        return (
            f"REQUER ANÁLISE - ultrapassou o teto de "
            f"{categoria.lower()}."
        )

    # -------------------------------------------------
    # INTERFACE
    # -------------------------------------------------

    def criar_interface(self):

        frame = ttk.Frame(self.root, padding=15)
        frame.pack(fill="both", expand=True)

        politica = (
            "POLÍTICA INTERNA\n\n"
            "Transporte: R$ 150,00\n"
            "Alimentação: R$ 85,00\n"
            "Hospedagem: R$ 450,00\n\n"
            "Cargos permitidos:\n"
            "Analista, Supervisor, Gerente e Diretor"
        )

        ttk.Label(
            frame,
            text=politica,
            justify="left"
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=10)

        ttk.Label(frame, text="Nome").grid(
            row=1,
            column=0,
            sticky="w"
        )

        self.entry_nome = ttk.Entry(frame, width=45)
        self.entry_nome.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Cargo").grid(
            row=2,
            column=0,
            sticky="w"
        )

        self.combo_cargo = ttk.Combobox(
            frame,
            values=CARGOS,
            state="readonly",
            width=42
        )

        self.combo_cargo.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Categoria").grid(
            row=3,
            column=0,
            sticky="w"
        )

        self.combo_categoria = ttk.Combobox(
            frame,
            values=list(CATEGORIAS.keys()),
            state="readonly",
            width=42
        )

        self.combo_categoria.grid(row=3, column=1, pady=5)

        # Requisito 2
        self.combo_categoria.bind(
            "<<ComboboxSelected>>",
            self.saltar_para_valor
        )

        ttk.Label(frame, text="Valor Gasto (R$)").grid(
            row=4,
            column=0,
            sticky="w"
        )

        self.entry_valor = ttk.Entry(frame, width=45)
        self.entry_valor.grid(row=4, column=1, pady=5)

        self.lbl_resultado = ttk.Label(
            frame,
            text="",
            foreground="blue"
        )

        self.lbl_resultado.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=15
        )

        botoes = ttk.Frame(frame)
        botoes.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=10
        )

        ttk.Button(
            botoes,
            text="Processar Pedido",
            command=self.processar
        ).pack(side="left", padx=5)

        ttk.Button(
            botoes,
            text="Ver Todos",
            command=self.abrir_log
        ).pack(side="left", padx=5)

        ttk.Button(
            botoes,
            text="Finalizar Pedido / Limpar Tela",
            command=self.limpar_tela
        ).pack(side="left", padx=5)

    # -------------------------------------------------
    # EVENTOS
    # -------------------------------------------------

    def saltar_para_valor(self, event=None):
        self.entry_valor.focus_set()

    def processar(self):

        try:

            nome = self.entry_nome.get().strip()
            cargo = self.combo_cargo.get().strip()
            categoria = self.combo_categoria.get().strip()

            valor_texto = self.entry_valor.get().replace(",", ".")
            valor = float(valor_texto)

            if not nome:
                raise ValueError("Informe o nome.")

            if not cargo:
                raise ValueError("Selecione o cargo.")

            if not categoria:
                raise ValueError("Selecione a categoria.")

            parecer = self.gerar_parecer(
                categoria,
                valor
            )

            self.lbl_resultado.config(
                text=f"Parecer: {parecer}"
            )

            agora = datetime.now()

            data = agora.strftime("%d-%m-%Y")
            timestamp = agora.strftime("%H%M%S")

            nome_arquivo = (
                f"{nome}_{cargo}_{data}_{timestamp}.txt"
            )

            nome_arquivo = self.sanitizar_nome_arquivo(
                nome_arquivo
            )

            conteudo = (
                "RELATÓRIO DE AUDITORIA\n"
                "======================\n"
                f"Nome: {nome}\n"
                f"Cargo: {cargo}\n"
                f"Categoria: {categoria}\n"
                f"Valor: R$ {valor:.2f}\n"
                f"Parecer: {parecer}\n"
                f"Data: {agora.strftime('%d/%m/%Y %H:%M:%S')}\n"
            )

            # Arquivo individual
            with open(
                nome_arquivo,
                "w",
                encoding="utf-8"
            ) as arq:
                arq.write(conteudo)

            # Log geral
            with open(
                LOG_GERAL,
                "a",
                encoding="utf-8"
            ) as log:
                log.write("\n")
                log.write("=" * 70 + "\n")
                log.write(conteudo)

            messagebox.showinfo(
                "Sucesso",
                f"Pedido registrado.\n\nArquivo:\n{nome_arquivo}"
            )

        except ValueError as erro:

            messagebox.showerror(
                "Erro de Validação",
                str(erro)
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Falha inesperada:\n{erro}"
            )

    def abrir_log(self):

        if not os.path.exists(LOG_GERAL):

            with open(
                LOG_GERAL,
                "w",
                encoding="utf-8"
            ):
                pass

        subprocess.Popen(["notepad.exe", LOG_GERAL])

    def limpar_tela(self):

        self.entry_nome.delete(0, tk.END)

        self.combo_cargo.set("")
        self.combo_categoria.set("")

        self.entry_valor.delete(0, tk.END)

        self.lbl_resultado.config(text="")

        self.entry_nome.focus_set()


def main():

    root = tk.Tk()

    SistemaAuditoria(root)

    root.mainloop()


if __name__ == "__main__":
    main()