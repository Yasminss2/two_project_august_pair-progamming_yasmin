'''
Objetivo: Apresentar a história da primeira grande 
investidora brasileira usando uma interface gráfica simples (tkinter).

Conceitos: História financeira do Brasil, diversificação 
internacional no século XIX, interfaces visuais (GUI).

COLOR_AZUL_ESC = "#004d6e"  # AE (Fundo da tela)
COLOR_AZUL_MED = "#0081ab"  # AM (Bordas e detalhes)
COLOR_AZUL_CLA = "#00b1cd"  # AC (Destaque do texto da senha)
COLOR_VERDE    = "#a6c844"  # V  (Botão Principal / Gerar)
COLOR_ROSA     = "#b83764"  # R  (Acentos e alertas de erro)
COLOR_AMARELO  = "#edce01"  # A  (Botão Copiar / Destaque)
COLOR_ACO      = "#4a3336"  # B  (Fundo dos campos e cards)

'''
import io
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk


# 1. Função que exibe a mensagem do evento
def mostrar_fato(detalhe):
    messagebox.showinfo("História de Eufrásia", detalhe)


# 2. Configuração da Janela Principal
janela = tk.Tk()
janela.title("História Financeira: Eufrásia Teixeira Leite")
janela.geometry("480x800")  # Ajustado o tamanho da tela
janela.configure(bg="#262a86")

# 3. Título e Subtítulo
lbl_titulo = tk.Label(
    janela,
    text="Eufrásia Teixeira Leite",
    font=("Times New Roman", 26, "bold"),
    bg="#262a86",
    fg="#850505",
)
lbl_titulo.pack(pady=7)
# lbl_titulo.pack(pady=120)

lbl_subtitulo = tk.Label(
    janela,
    text="Uma mulher que escolheu sua liberdade e fez dela parte do seu legado",
    font=("Arial", 10, "italic"),
    bg="#262a86",
    fg="#e5c701",
)
lbl_subtitulo.pack(pady=2)

# 4. Carregando Imagem da Internet
url_imagem = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3gbIi1DCAoEmDzTJ34sXyO7HiOnA9LcoA2rmbS7zRbg&s=10"
# url_imagem = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Tarsila_do_Amaral%2C_ca._1925.jpg/960px-Tarsila_do_Amaral%2C_ca._1925.jpg"

# Criando variável global da foto para o Tkinter não apagar da memória
foto_eufrasia = None

try:
    # Headers para simular um navegador comum (evita bloqueios)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    resposta = requests.get(url_imagem, headers=headers, timeout=5)
    resposta.raise_for_status()  # Confirma que o download deu certo (status 200)

    dados_imagem = resposta.content

    # Processando a imagem com Pillow
    imagem_pil = Image.open(io.BytesIO(dados_imagem))
    imagem_pil = imagem_pil.resize(
        (130, 160), Image.Resampling.LANCZOS
    )  # Redimensiona

    foto_eufrasia = ImageTk.PhotoImage(imagem_pil)

    # Exibindo no Label
    lbl_imagem = tk.Label(janela, image=foto_eufrasia, bg="#f4f4f9")
    lbl_imagem.image = foto_eufrasia  # Guarda a referência da imagem
    lbl_imagem.pack(pady=10)

except Exception as erro:
    # Caso aconteça algum problema de conexão, exibe um aviso em texto na tela
    print(f"Erro ao carregar imagem: {erro}")
    lbl_erro = tk.Label(
        janela,
        text="[Foto de Eufrásia Teixeira Leite - Indisponível sem internet]",
        font=("Arial", 9, "italic"),
        fg="gray",
        bg="#262a86",
    )
    lbl_erro.pack(pady=10)

# 5. Dados da Linha do Tempo (Dicionário)
eventos = {
    "1850 - Nascimento": "Nasceu em Vassouras (RJ), em uma família rica e ligada na produção de café.",
    "1872 - Herança & Europa": "Após perder os pais, herdou uma grande fortuna, se mudou para Paris e investiu em diferentes áreas.",
    "1873-1930 - Carteira Global": "Investiu em títulos, ações e ferrovias em 13 países e 7 moedas diferentes.",
    "1930 - Legado": "Faleceu deixando sua fortuna para causas sociais e educacionais no Brasil.",
    "1930-1950 - Construindo a Herança": "O Patrimônio incluía ímoveis, dinheiro, ações, investimentos no Brasil e no exterior.",
    "1873-1887 - Relacionamento": "Vivendo um romance com Joaquim Nabuco, chegaram a ficar noivos, mas nunca se casaram. Eufrásia pensava em administrar seus investimentos e queria permanecer na Europa, enquanto Nabuco desejava permanecer no Brasil."
}

# 6. Criação dos Botões
for data, detalhe in eventos.items():
    btn = tk.Button(
        janela,
        text=data,
        font=("Arial", 11),
        bg="#850505",
        fg="white",
        relief="flat",
        command=lambda d=detalhe: mostrar_fato(d),
    )
    btn.pack(fill="x", padx=40, pady=6)

# 7. Loop Principal
janela.mainloop()