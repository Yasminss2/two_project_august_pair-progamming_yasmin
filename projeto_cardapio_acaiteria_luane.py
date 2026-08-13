import tkinter as tk
from tkinter import ttk, messagebox

# 1. DADOS DO CARDÁPIO
produtos = [
    {"id": 1, "nome": "Açaí tradicional - 300ml", "preço": 10.00},
    {"id": 2, "nome": "Açaí premium - 500ml", "preço": 15.00},
    {"id": 3, "nome": "Açaí especial - 1,5L", "preço": 25.00},
    {"id": 4, "nome": "El Açaízon 2,5L", "preço": 35.00}
]

adicionais = [
    {"nome": "Granola", "preço": 2.00},
    {"nome": "Paçoca", "preço": 2.50},
    {"nome": "Leite em Pó", "preço": 3.00},
    {"nome": "Nutella", "preço": 5.00},
    {"nome": "Leite Condensado", "preço": 3.00},
    {"nome": "Morango", "preço": 2.80},
    {"nome": "Banana", "preço": 2.80}
]

bebidas = [
    {"nome": "Água Mineral - 500ml", "preço": 4.00},
    {"nome": "Suco de Laranja - 400ml", "preço": 8.50},
    {"nome": "Refrigerante Lata - 300ml", "preço": 6.00}
]

# --- PALETA DE CORES ---
COR_FUNDO = "#2C1135"         # Roxo escuro
COR_CARD = "#3D1A48"          # Roxo médio para seções
COR_TEXTO = "#F4E8F8"         # Lilás bem claro
COR_TEXTO_ESCURO = "#2C1135"  # Para entradas
COR_DESTAQUE = "#8A2BE2"      # Roxo vivo / Seleção de aba
COR_BOTAO = "#27AE60"         # Verde confirmação
COR_BOTAO_HOVER = "#219150"   # Verde escuro no hover

# 3. JANELA PRINCIPAL
janela = tk.Tk()
janela.title("Cardápio de Açaí")
janela.geometry("480x620")
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False) # Impede redimensionar para manter o design centralizado

# VARIÁVEIS DE CONTROLE
produto_selecionado = tk.IntVar(value=1)
adicionais_selecionados = {}
bebidas_selecionadas = {}

# --- CABEÇALHO (Fixo no topo) ---
header = tk.Label(
    janela, 
    text="🍇 CARDÁPIO DE AÇAÍ 🍇", 
    font=("Arial", 16, "bold"), 
    bg=COR_FUNDO, 
    fg="#E0AAFF",
    pady=12
)
header.pack()

# -------------------------------------------------------------
# ESTILIZAÇÃO DAS ABAS (TTK NOTEBOOK)
# -------------------------------------------------------------
style = ttk.Style()
style.theme_use('default')

style.configure('TNotebook', background=COR_FUNDO, borderwidth=0)
style.configure(
    'TNotebook.Tab', 
    background=COR_CARD, 
    foreground=COR_TEXTO, 
    padding=[12, 6], 
    font=('Arial', 10, 'bold'),
    borderwidth=0
)
style.map(
    'TNotebook.Tab', 
    background=[('selected', COR_DESTAQUE)], 
    foreground=[('selected', 'white')]
)

notebook = ttk.Notebook(janela)
notebook.pack(padx=20, pady=5, fill="both", expand=True)

# -------------------------------------------------------------
# ABA 1: AÇAÍS
# -------------------------------------------------------------
aba_acai = tk.Frame(notebook, bg=COR_FUNDO)
notebook.add(aba_acai, text=" 🍧 Açaís ")

frame_produtos = tk.Frame(aba_acai, bg=COR_CARD, padx=20, pady=15)
frame_produtos.pack(anchor="center", fill="x", padx=15, pady=15)

tk.Label(
    frame_produtos, 
    text="Escolha o Tamanho/Opção:", 
    font=("Arial", 11, "bold"), 
    bg=COR_CARD, 
    fg=COR_TEXTO
).pack(anchor="w", pady=(0, 10))

for prod in produtos:
    texto = f"{prod['nome']} - R$ {prod['preço']:.2f}"
    rb = tk.Radiobutton(
        frame_produtos, 
        text=texto, 
        value=prod['id'], 
        variable=produto_selecionado, 
        font=("Arial", 10),
        bg=COR_CARD,
        fg=COR_TEXTO,
        selectcolor=COR_DESTAQUE,
        activebackground=COR_CARD,
        activeforeground=COR_TEXTO
    )
    rb.pack(anchor="w", pady=4)

# -------------------------------------------------------------
# ABA 2: ADICIONAIS
# -------------------------------------------------------------
aba_adicionais = tk.Frame(notebook, bg=COR_FUNDO)
notebook.add(aba_adicionais, text=" 🍫 Adicionais ")

frame_adicionais = tk.Frame(aba_adicionais, bg=COR_CARD, padx=20, pady=15)
frame_adicionais.pack(anchor="center", fill="x", padx=15, pady=15)

tk.Label(
    frame_adicionais, 
    text="Escolha os Adicionais:", 
    font=("Arial", 11, "bold"), 
    bg=COR_CARD, 
    fg=COR_TEXTO
).pack(anchor="w", pady=(0, 10))

for add in adicionais:
    var = tk.BooleanVar()
    adicionais_selecionados[add["nome"]] = var
    texto_add = f"{add['nome']} (+R$ {add['preço']:.2f})"
    cb = tk.Checkbutton(
        frame_adicionais, 
        text=texto_add, 
        variable=var, 
        font=("Arial", 10),
        bg=COR_CARD,
        fg=COR_TEXTO,
        selectcolor=COR_DESTAQUE,
        activebackground=COR_CARD,
        activeforeground=COR_TEXTO
    )
    cb.pack(anchor="w", pady=2)

# -------------------------------------------------------------
# ABA 3: BEBIDAS
# -------------------------------------------------------------
aba_bebidas = tk.Frame(notebook, bg=COR_FUNDO)
notebook.add(aba_bebidas, text=" 🥤 Bebidas ")

frame_bebidas = tk.Frame(aba_bebidas, bg=COR_CARD, padx=20, pady=15)
frame_bebidas.pack(anchor="center", fill="x", padx=15, pady=15)

tk.Label(
    frame_bebidas, 
    text="Bebidas para Acompanhar:", 
    font=("Arial", 11, "bold"), 
    bg=COR_CARD, 
    fg=COR_TEXTO
).pack(anchor="w", pady=(0, 10))

for beb in bebidas:
    var = tk.BooleanVar()
    bebidas_selecionadas[beb["nome"]] = var
    texto_beb = f"{beb['nome']} (+R$ {beb['preço']:.2f})"
    cb = tk.Checkbutton(
        frame_bebidas, 
        text=texto_beb, 
        variable=var, 
        font=("Arial", 10),
        bg=COR_CARD,
        fg=COR_TEXTO,
        selectcolor=COR_DESTAQUE,
        activebackground=COR_CARD,
        activeforeground=COR_TEXTO
    )
    cb.pack(anchor="w", pady=4)

# -------------------------------------------------------------
# PAINEL INFERIOR FIXO (QUANTIDADE, OBSERVAÇÃO E FINALIZAR)
# -------------------------------------------------------------
frame_inferior = tk.Frame(janela, bg=COR_FUNDO)
frame_inferior.pack(fill="x", padx=25, pady=(0, 15))

# Linha de Quantidade
frame_qtd = tk.Frame(frame_inferior, bg=COR_FUNDO)
frame_qtd.pack(anchor="center", pady=5)

tk.Label(
    frame_qtd, 
    text="Quantidade de Açaís:", 
    font=("Arial", 10, "bold"), 
    bg=COR_FUNDO, 
    fg=COR_TEXTO
).pack(side="left", padx=(0, 8))

spin_quantidade = tk.Spinbox(
    frame_qtd, 
    from_=1, 
    to=10, 
    width=4, 
    font=("Arial", 10, "bold"),
    bg="#F0F0F0",
    fg=COR_TEXTO_ESCURO,
    buttonbackground="#DDD"
)
spin_quantidade.pack(side="left")

# Observações
tk.Label(
    frame_inferior, 
    text="Observações do Pedido:", 
    font=("Arial", 10, "bold"), 
    bg=COR_FUNDO, 
    fg=COR_TEXTO
).pack(anchor="center", pady=(5, 2))

entry_obs = tk.Entry(
    frame_inferior, 
    width=38, 
    font=("Arial", 10),
    bg="#F0F0F0",
    fg=COR_TEXTO_ESCURO,
    relief="flat",
    highlightthickness=2,
    highlightbackground=COR_DESTAQUE
)
entry_obs.pack(anchor="center", pady=2)

# LÓGICA DO PEDIDO
def finalizar_pedido():
    try:
        qtd = int(spin_quantidade.get())
        if qtd <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira uma quantidade válida.")
        return

    subtotal_acai = 0.0
    resumo = "=== SEU PEDIDO ===\n\n"
    
    # 1. Açaí Selecionado
    id_escolhido = produto_selecionado.get()
    for prod in produtos:
        if prod["id"] == id_escolhido:
            resumo += f"Açaí: {prod['nome']} (R$ {prod['preço']:.2f})\n"
            subtotal_acai += prod["preço"]
            break
            
    # 2. Adicionais
    resumo += "\nAdicionais:\n"
    tem_adicional = False
    for add in adicionais:
        nome_add = add["nome"]
        if adicionais_selecionados[nome_add].get():
            resumo += f"- {nome_add} (+R$ {add['preço']:.2f})\n"
            subtotal_acai += add["preço"]
            tem_adicional = True
            
    if not tem_adicional:
        resumo += "- Nenhum adicional\n"

    # Total Açaís + Adicionais multiplicado pela Quantidade
    total_acais = subtotal_acai * qtd
    resumo += f"\nQtd de Açaís: {qtd}x (Subtotal: R$ {total_acais:.2f})\n"

    # 3. Bebidas (Calculadas por fora do multiplicador de açaí)
    resumo += "\nBebidas:\n"
    total_bebidas = 0.0
    tem_bebida = False
    for beb in bebidas:
        nome_beb = beb["nome"]
        if bebidas_selecionadas[nome_beb].get():
            resumo += f"- {nome_beb} (+R$ {beb['preço']:.2f})\n"
            total_bebidas += beb["preço"]
            tem_bebida = True

    if not tem_bebida:
        resumo += "- Nenhuma bebida\n"

    # 4. Observações e Total Final
    obs = entry_obs.get().strip()
    resumo += f"\nObservação: {obs if obs else "\n- Nenhuma observação"}"

    total_final = total_acais + total_bebidas
    resumo += f"\n\n--------------------------\nTOTAL FINAL: R$ {total_final:.2f}"
    
    messagebox.showinfo("Resumo do Pedido", resumo)

# Botão de Confirmação
btn_confirmar = tk.Button(
    frame_inferior, 
    text="FINALIZAR PEDIDO", 
    command=finalizar_pedido, 
    bg=COR_BOTAO, 
    fg="white", 
    font=("Arial", 11, "bold"),
    activebackground=COR_BOTAO_HOVER,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=15,
    pady=8
)
btn_confirmar.pack(anchor="center", pady=(12, 0))

janela.mainloop()