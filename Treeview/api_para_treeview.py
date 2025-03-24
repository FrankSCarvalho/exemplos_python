import tkinter as tk
from tkinter import ttk, messagebox
import requests

def fetch_data():
    try:
        #Fazendo a requisição a API
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        response.raise_for_status()

        data = response.json()

        #Limpa dados antigos da Treeview
        for item in tree.get_children():
            tree.delete(item)

        #Preenchendo a Treeview
        for user in data:
            user_data=(
                user['id'],
                user['name'],
                user['email'],
                user['address']['city'],
                user['phone']
            )
            tree.insert('','end',values=user_data)
    except requests.exceptions.RequestException as e:
        messagebox.showerror('Erro', f'Falha ao Buscar dados: {e}')


#Configurando Janela Principal
root = tk.Tk()
root.title('Dados de usuários')
root.geometry('800x400')

#Criando Treeview
columns = ('id', 'name', 'email', 'city', 'phone')
tree = ttk.Treeview(
    root,
    columns=columns,
    show='headings',
    selectmode='browse'
)

#Configurando cabeçalhos
tree.heading('id', text='id')
tree.heading('name', text='name')
tree.heading('email', text='email')
tree.heading('city', text='city')
tree.heading('phone', text='phone')

#Configurando colunas
tree.column('id', width=50, anchor='center')
tree.column('name', width=150)
tree.column('email', width=200)
tree.column('city', width=150)
tree.column('phone', width=120)

# Adicionando scrollbar
scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side='right', fill='y')

tree.pack(fill='both', expand=True)

# Botão para carregar dados
btn_load = ttk.Button(root, text='Carregar Dados', command=fetch_data)
btn_load.pack(pady=10)

# Executar o loop principal
root.mainloop()