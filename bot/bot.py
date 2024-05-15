import pyautogui as pg
from time import sleep
import random as rnd
import pyperclip
import threading
from utils import show_custom_dialog

# Global event to signal cancellation
cancel_event = threading.Event()

def abrir_whatsapp():
    sleep(2)
    pg.press('win')
    sleep(2)
    pg.write('whatsapp')
    sleep(3)
    pg.press('enter')
    sleep(5)

def enviar_mensagem(numero, mensagem):
    aleatorio1 = (rnd.randrange(40, 100) / 10)
    if cancel_event.is_set():
        return
    pg.hotkey('ctrl', 'n')
    sleep(3)
    if cancel_event.is_set():
        return
    pg.write(numero)
    sleep(aleatorio1)
    if cancel_event.is_set():
        return
    pg.press('tab')
    sleep(aleatorio1)
    if cancel_event.is_set():
        return
    pg.press('enter')
    sleep(aleatorio1)
    if cancel_event.is_set():
        return
    pyperclip.copy(mensagem)
    pg.hotkey('ctrl', 'v')
    sleep(aleatorio1)
    if cancel_event.is_set():
        return
    pg.press('enter')
    sleep(1)
    if cancel_event.is_set():
        return
    pg.press('esc')
    sleep(2)
    if cancel_event.is_set():
        return

def enviar_para_lista(lista_numeros, mensagem):
    cancel_event.clear()  # Ensure the event is clear at the start
    abrir_whatsapp()
    for numero in lista_numeros:
        if cancel_event.is_set():
            break
        enviar_mensagem(numero, mensagem)
    if not cancel_event.is_set():
        show_custom_dialog("Concluído", "Envio de mensagens concluído com sucesso.")
    else:
        show_custom_dialog("Interrupção", "Envio de mensagens interrompido")
