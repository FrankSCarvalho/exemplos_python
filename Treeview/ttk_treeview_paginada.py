import tkinter as tk
from tkinter import ttk

# --- Configuração inicial ---
root = tk.Tk()
root.title("Treeview Paginada Otimizada")

# Dados de exemplo (500 itens)
data = [
    {"Nome": f"Item {i}", "Idade": i + 20} 
    for i in range(1, 500000)
]

# Variáveis de controle
page_size = 10
current_page = 0
max_visible_buttons = 5  # Número máximo de botões visíveis

# --- Cria a Treeview ---
tree = ttk.Treeview(root, columns=("ID", "Nome", "Idade"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.pack(padx=10, pady=10)

# --- Funções de paginação ---
def update_treeview():
    global current_page, page_size
    
    # Limpa a Treeview
    tree.delete(*tree.get_children())
    
    # Calcula os índices da página atual
    start_idx = current_page * page_size
    end_idx = start_idx + page_size
    current_data = data[start_idx:end_idx]
    
    # Insere os dados
    for idx, item in enumerate(current_data, start=start_idx):
        tree.insert("", "end", values=(idx + 1, item["Nome"], item["Idade"]))
    
    # Atualiza os botões de página
    update_page_buttons()

def update_page_buttons():
    # Remove os botões antigos
    for widget in page_buttons_frame.winfo_children():
        widget.destroy()
    
    total_pages = (len(data) + page_size - 1) // page_size
    
    # Calcula o intervalo de páginas visíveis
    start_page = max(0, current_page - max_visible_buttons // 2)
    end_page = min(total_pages, current_page + max_visible_buttons // 2 + 1)
    
    # Botão para primeira página
    if start_page > 0:
        create_page_button(0)
        if start_page > 1:
            ttk.Label(page_buttons_frame, text="...").pack(side=tk.LEFT)
    
    # Botões do intervalo visível
    for page in range(start_page, end_page):
        create_page_button(page)
    
    # Botão para última página
    if end_page < total_pages:
        if end_page < total_pages - 1:
            ttk.Label(page_buttons_frame, text="...").pack(side=tk.LEFT)
        create_page_button(total_pages - 1)

def create_page_button(page):
    btn = ttk.Button(
        page_buttons_frame,
        text=str(page + 1),
        command=lambda p=page: go_to_page(p),
        width=6
    )
    if page == current_page:
        btn.state(["disabled"])
    btn.pack(side=tk.LEFT, padx=2)

def go_to_page(page_number):
    global current_page
    current_page = page_number
    update_treeview()

def next_page():
    global current_page
    if (current_page + 1) * page_size < len(data):
        current_page += 1
        update_treeview()

def prev_page():
    global current_page
    if current_page > 0:
        current_page -= 1
        update_treeview()

# --- Interface ---
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

# Botões de navegação
btn_prev = ttk.Button(btn_frame, text="◀ Anterior", command=prev_page)
btn_prev.pack(side=tk.LEFT, padx=2)

page_buttons_frame = tk.Frame(btn_frame)
page_buttons_frame.pack(side=tk.LEFT, padx=2)

btn_next = ttk.Button(btn_frame, text="Próximo ▶", command=next_page)
btn_next.pack(side=tk.LEFT, padx=2)

# Campo para pular para uma página específica
ttk.Label(btn_frame, text="Ir para:").pack(side=tk.LEFT, padx=5)
page_entry = ttk.Entry(btn_frame, width=5)
page_entry.pack(side=tk.LEFT)
ttk.Button(btn_frame, text="Ir", command=lambda: jump_to_page()).pack(side=tk.LEFT)

def jump_to_page():
    try:
        page = int(page_entry.get()) - 1
        total_pages = (len(data) + page_size - 1) // page_size
        if 0 <= page < total_pages:
            go_to_page(page)
    except:
        pass

# --- Inicialização ---
update_treeview()
root.mainloop()