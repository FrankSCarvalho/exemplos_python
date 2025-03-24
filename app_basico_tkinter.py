import tkinter as tk
from tkinter import messagebox


root = tk.Tk()

def acao():
    messagebox.showinfo('Clicou', 'Obrigado por clicar!')
    return

root.title("Aplicativo Básico Tkinter")
root.geometry("600x400")

label = tk.Label(root, text="Label teste")
entry = tk.Entry(root,show="Entry teste", width=50)
botao = tk.Button(root, text="Clique aqui", command=acao)

#Posicionando widgets
label.grid(row=0,column=0,padx=10)
entry.grid(row=0, column=1)
botao.grid(row=1, column=0,columnspan=2,sticky='NSEW',pady=10,padx=10)

root.mainloop()