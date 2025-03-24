import tkinter as tk

def comando_novo():
    print("Novo arquivo criado!")

def comando_sair():
    root.destroy()

# Cria a janela principal
root = tk.Tk()
root.title("Menu Tkinter")

# Cria uma barra de menu
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# Menu "Arquivo"
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_arquivo.add_command(label="Novo", command=comando_novo, accelerator="Ctrl+N")
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=comando_sair)

submenu_exportar = tk.Menu(menu_arquivo, tearoff=0)
menu_arquivo.add_cascade(label="Exportar", menu=submenu_exportar)
submenu_exportar.add_command(label="PDF", command=lambda: print("Exportando PDF..."))
submenu_exportar.add_command(label="Imagem", command=lambda: print("Exportando Imagem..."))

# Menu "Ajuda"
menu_ajuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)
menu_ajuda.add_command(label="Sobre", command=lambda: print("Versão 1.0"))

# Loop principal
root.mainloop()