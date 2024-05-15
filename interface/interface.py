import customtkinter as tk
import threading
from bot import enviar_para_lista, cancel_event
from utils import show_custom_dialog, show_dialog_temporario

def enviar():
    numeros = entrada_numeros.get("1.0", 'end-1c').split('\n')
    mensagem = entrada_mensagem.get("1.0", 'end-1c')
    if not mensagem:
        show_custom_dialog("Erro", "Por favor, insira uma mensagem.")
    elif not any(numero.strip() for numero in numeros):
        show_custom_dialog("Erro", "Por favor, insira pelo menos um número.")
    else:
        threading.Thread(target=enviar_para_lista, args=(numeros, mensagem)).start()
        show_dialog_temporario("Enviando", "Iniciando envio de mensagens...")

def cancelar():
    cancel_event.set()

def create_interface(root):
    global entrada_numeros, entrada_mensagem

    root.title("Envio de Mensagens WhatsApp")
    root.geometry("600x400")
    root._set_appearance_mode("dark")

    frame = tk.CTkFrame(root)
    frame.pack(padx=10, pady=10)
    frame._set_appearance_mode("dark")

    label_numeros = tk.CTkLabel(frame, text="Números (um por linha):", bg_color=("#2B2B2B"), text_color=("white"))
    label_numeros.grid(row=0, column=0, sticky="w")

    entrada_numeros = tk.CTkTextbox(frame, height=100, width=400, fg_color="#1A1B1C", bg_color="#2B2B2B", text_color=("white"))
    entrada_numeros.grid(row=1, column=0, padx=5, pady=5)

    label_mensagem = tk.CTkLabel(frame, text="Mensagem:", bg_color=("#2B2B2B"), text_color=("white"))
    label_mensagem.grid(row=2, column=0, sticky="w", pady=(10, 0))

    entrada_mensagem = tk.CTkTextbox(frame, height=100, width=400, fg_color="#1A1B1C", bg_color="#2B2B2B", text_color=("white"))
    entrada_mensagem.grid(row=3, column=0, padx=5, pady=5)

    botao_enviar = tk.CTkButton(frame, text="Enviar", command=enviar, bg_color=("#1A1B1C"))
    botao_enviar.grid(row=4, column=0, pady=(10, 0))

    botao_cancelar = tk.CTkButton(frame, text="Cancelar", command=cancelar, bg_color=("#1A1B1C"))
    botao_cancelar.grid(row=6, column=0, pady=(10, 0))

    root.resizable(True, True)
