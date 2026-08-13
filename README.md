# 🐍 Projetos Educacionais em Python - Finanças, História e Sistemas Interativos

Este repositório contém uma coleção de aplicações gráficas desenvolvidas em **Python** utilizando **Tkinter**. Os projetos foram elaborados com foco didático para capacitação profissional e alunos de programas educacionais (como **Jovem Aprendiz** / **Programa Vocação**), integrando conceitos de **programação procedural**, **educação financeira**, **história do Brasil** e **sistemas de atendimento/vendas (PDV)**.

---

## 🎯 Objetivos Didáticos

* **Lógica Procedural:** Estruturação de código sem o uso de Orientação a Objetos (POO), facilitando a assimilação inicial de funções, parâmetros, manipulação de coleções (listas e dicionários) e escopo global (`global`).
* **Interface Gráfica (GUI):** Construção de telas interativas com `tkinter` e componentes modernos (`ttk.Notebook`, `Listbox`, `Frame`, `Spinbox`, `Radiobutton`, `Checkbutton`).
* **Tratamento de Exceções & Validação:** Uso de blocos `try/except` para validação de entradas numéricas e prevenção de erros em tempo de execução.
* **Consumo de Requisições HTTP e Manipulação de Imagens:** Integração com a web (`requests`) e tratamento/redimensionamento de imagens (`Pillow`).

---

## 🚀 Projetos Incluídos

### 1. 📜 Linha do Tempo: Eufrásia Teixeira Leite (`historia_financas_with_eufrasia_luane.py`)
Uma interface interativa sobre **Eufrásia Teixeira Leite** (1850–1930), a primeira investidora global do Brasil.
* **O que faz:** Apresenta a trajetória histórica de Eufrásia por meio de uma linha do tempo interativa com botões e exibe a foto da biografada baixada diretamente da internet.
* **Destaques & Lógica:**
  * Download e exibição de imagem via requisições HTTP (`requests` e `Pillow`).
  * Tratamento resiliente de erros (`try/except`) para garantir o funcionamento da aplicação mesmo em modo offline.
  * Estruturação de eventos em dicionários e criação dinâmica de botões com funções `lambda`.

---

### 2. 💵 Simulador de Rendas e Aportes (`financas_aportes_bankb3_luane.py`)
Uma calculadora de fluxo de caixa simplificada para ensinar operações de depósito e saque com respostas visuais instantâneas.
* **O que faz:** Permite simular entradas e saídas financeiras com atualização de saldo em tempo real.
* **Destaques & Lógica:**
  * Controle e manipulação de saldo via escopo global (`global`).
  * Validação para impedir depósitos inválidos ou saques superiores ao saldo disponível.
  * Tratamento de exceções com `try/except ValueError` e respostas com `messagebox`.

---

### 3. 📊 Dashboard Financeiro - Padrão B3 (`financas_dashboard_bankb3.py`)
Um painel completo com identidade visual inspirada no ambiente da Bolsa de Valores brasileira (**B3**).
* **O que faz:** Gerencia a vida financeira do usuário dividida em abas: **Conta Corrente**, **Criptoativos** e **Extrato**.
* **Destaques & Lógica:**
  * Interface moderna baseada em abas interativas utilizando `ttk.Notebook` e estilização customizada com `ttk.Style`.
  * Simulação de ativos digitais com cálculo de frações de Bitcoin (BTC) a partir da cotação simulada.
  * Histórico dinâmico de transações atualizado em tempo real via `tk.Listbox`.

---

### 4. 🍇 Sistema de Pedidos: Cardápio de Açaí (`projeto_cardapio_acaiteria_luane.py`)
Uma aplicação desktop para automação de atendimento e ponto de venda (PDV) em lojas de açaí.
* **O que faz:** Permite selecionar o tamanho do açaí, escolher acompanhamentos/adicionais e bebidas, definir a quantidade de itens, adicionar observações personalizadas e gerar um comprovante com o cálculo automático do valor total do pedido.
* **Destaques & Lógica:**
  * Organização modular do cardápio em abas (`ttk.Notebook`) separando **Açaís**, **Adicionais** e **Bebidas**.
  * **Seleção de Produtos:** Botões de rádio (`Radiobutton`) para escolha exclusiva do tamanho principal.
  * **Personalização do Pedido:** Caixas de seleção (`Checkbutton`) para múltiplos adicionais (Granola, Paçoca, Leite em Pó, Nutella, Frutas, etc.) e bebidas.
  * **Cálculo Dinâmico:** Processamento do valor total acumulado baseado no item principal + adicionais multiplicados pela quantidade escolhida, somados às bebidas selecionadas.
  * **Feedback ao Usuário:** Geração de um resumo detalhado do pedido via janela de mensagem (`messagebox.showinfo`).

---

## 🛠️ Pré-requisitos e Instalação

Para executar os projetos, você precisará do **Python 3.10+** instalado em sua máquina.

### Instalar as dependências do projeto
Abra o terminal ou prompt de comando e execute:

```bash
pip install requests pillow faker
