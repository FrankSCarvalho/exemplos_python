import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os

class ReportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Relatórios")
        
        # Dados para os relatórios
        self.data = []
        
        # Criar widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Frame de entrada de dados
        input_frame = ttk.LabelFrame(self.root, text="Dados do Relatório")
        input_frame.pack(padx=10, pady=10, fill="x")
        
        # Campos de entrada
        ttk.Label(input_frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Idade:").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = ttk.Entry(input_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = ttk.Entry(input_frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Botões
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Adicionar Registro", command=self.add_record).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Gerar PDF", command=self.generate_pdf).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Gerar CSV", command=self.generate_csv).pack(side=tk.LEFT, padx=5)
        
        # Lista de registros
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
    def add_record(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        email = self.email_entry.get()
        
        if not all([name, age, email]):
            messagebox.showwarning("Campos Vazios", "Preencha todos os campos!")
            return
            
        try:
            int(age)
        except ValueError:
            messagebox.showwarning("Idade Inválida", "A idade deve ser um número!")
            return
            
        record = {
            "Nome": name,
            "Idade": age,
            "Email": email,
            "Data Registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.data.append(record)
        self.listbox.insert(tk.END, f"{name} - {age} anos - {email}")
        self.clear_entries()
        
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        
    def generate_csv(self):
        if not self.data:
            messagebox.showwarning("Dados Vazios", "Adicione registros primeiro!")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")]
        )
        
        if not file_path:
            return
            
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.data[0].keys())
                writer.writeheader()
                writer.writerows(self.data)
            messagebox.showinfo("Sucesso", "Arquivo CSV gerado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar CSV: {str(e)}")
            
    def generate_pdf(self):
        if not self.data:
            messagebox.showwarning("Dados Vazios", "Adicione registros primeiro!")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )
        
        if not file_path:
            return
            
        try:
            c = canvas.Canvas(file_path, pagesize=letter)
            width, height = letter
            
            # Cabeçalho
            c.setFont("Helvetica-Bold", 14)
            c.drawString(72, height - 72, "Relatório de Registros")
            
            # Conteúdo
            y = height - 100
            c.setFont("Helvetica", 12)
            
            for idx, record in enumerate(self.data, 1):
                text = f"{idx}. {record['Nome']} - {record['Idade']} anos - {record['Email']}"
                c.drawString(72, y, text)
                y -= 20
                
                if y < 100:
                    c.showPage()
                    y = height - 50
                    c.setFont("Helvetica", 12)
            
            c.save()
            messagebox.showinfo("Sucesso", "Arquivo PDF gerado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar PDF: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReportApp(root)
    root.mainloop()