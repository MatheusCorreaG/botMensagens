import customtkinter as tk

def show_custom_dialog(title, message):
    dialog = tk.CTk()
    dialog.title(title)
    dialog.geometry("300x100")
    label = tk.CTkLabel(dialog, text=message)
    label.pack(pady=10)
    button = tk.CTkButton(dialog, text="OK", command=dialog.destroy)
    button.pack(pady=5)
    dialog.mainloop()

def show_dialog_temporario(title, message):
    dialog = tk.CTk()
    dialog.title(title)
    dialog.geometry("300x100")
    label = tk.CTkLabel(dialog, text=message)
    label.pack(pady=10)
    dialog.after(2000, dialog.destroy)
    dialog.mainloop()
