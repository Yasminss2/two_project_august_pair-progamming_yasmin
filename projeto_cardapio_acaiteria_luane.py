import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import faker

produtos = [
    
    {
    "id": 1,
    "nome": "Açaí tradicional",
    "preço": 16.50,
    "estoque": 50,
    "descrição": "Açaí tradicional 300ml, um clássico que nunca falha."
     },
    
     {
    "id": 2,
    "nome": "Açaí premium",
    "preço": 24.50,
    "estoque": 50,
    "descrição": "Açaí premium, 500ml de pura tentação!"
     },
     
    { 
    "id": 3,
    "nome": "Açaí especial",
    "preço": 35.00,
    "estoque": 50,
    "descrição": "Açaí especial, um tigelão de 1,5L feito para quem não brinca em serviço!."
     },
    
    {
    "id": 4,
    "nome": "El Açaízon ",
    "preço": 35.00,
    "estoque": 50,
    "descrição": "O gigante da casa! 2,5L de açaí super cremoso para compartilhar (ou devorar sozinho)."
     }
    
]

# 2. LISTA DE ADICIONAIS
adicionais = [
    {"nome": "Granola", "preço": 2.00},
    {"nome": "Paçoca", "preço": 2.50},
    {"nome": "Leite em Pó", "preço": 3.00},
    {"nome": "Nutella", "preço": 5.00}
]

# 3. JANELA PRINCIPAL
janela = tk.Tk()
janela.title("Cardápio de Açaí")
janela.geometry("400x500")

# 4. VARIÁVEIS DE CONTROLE DO TKINTER
produto_selecionado = tk.IntVar(value=1)
adicionais_selecionados = {}

# 5. CONSTRUÇÃO DA INTERFACE VISUAL
tk.Label(janela, text="Selecione o Tamanho:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)

for prod in produtos:
    texto = f"{prod['nome']} - R$ {prod['preço']:.2f}"
    # COMPLETE AQUI: Crie o tk.Radiobutton para cada produto
    # Dica: text=texto, value=prod['id'], variable=produto_selecionado

tk.Label(janela, text="Selecione os Adicionais:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=(15, 5))

for add in adicionais:
    var = tk.BooleanVar()
    adicionais_selecionados[add["nome"]] = var
    texto_add = f"{add['nome']} (+R$ {add['preço']:.2f})"
    # COMPLETE AQUI: Crie o tk.Checkbutton para cada adicional
    # Dica: text=texto_add, variable=var

# 6. FUNÇÃO DE FINALIZAR PEDIDO
def finalizar_pedido():
    total = 0.0
    resumo = "=== SEU PEDIDO ===\n\n"
    
    # Busca o produto escolhido pelo ID
    id_escolhido = produto_selecionado.get()
    for prod in produtos:
        if prod["id"] == id_escolhido:
            resumo += f"Açaí: {prod['nome']}\nPreço: R$ {prod['preço']:.2f}\n"
            total += prod["preço"]
            break
            
    resumo += "\nAdicionais:\n"
    # Percorre os adicionais marcados
    for add in adicionais:
        nome_add = add["nome"]
        # Se o Checkbutton estiver marcado (True)
        if adicionais_selecionados[nome_add].get():
            resumo += f"- {nome_add} (+R$ {add['preço']:.2f})\n"
            total += add["preço"]
            
    resumo += f"\nTOTAL FINAL: R$ {total:.2f}"
    
    # Exibe o pop-up com o resumo
    messagebox.showinfo("Pedido Finalizado", resumo)

# 7. BOTÃO DE CONFIRMAÇÃO
btn_confirmar = tk.Button(janela, text="Finalizar Pedido", command=finalizar_pedido, bg="purple", fg="white", font=("Arial", 11, "bold"))
btn_confirmar.pack(pady=20)

janela.mainloop()