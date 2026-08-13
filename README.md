# Sistema de Pedidos: Cardápio de Açaí

## 📋 Panorama Geral
Este projeto consiste em uma aplicação desktop desenvolvida em Python para a automação de um sistema de pedidos de uma loja de açaí. O objetivo é oferecer uma interface intuitiva onde o cliente (ou atendente) possa selecionar o tamanho do produto e adicionar acompanhamentos, finalizando com o cálculo automático do valor total do pedido.

O software foi estruturado para demonstrar conceitos fundamentais de interface gráfica (GUI), manipulação de eventos e estruturas de dados em Python.

## 🚀 Funcionalidades Principais
*   **Seleção de Produtos:** Interface com botões de rádio (*Radiobuttons*) para escolha do tamanho do açaí, garantindo que apenas uma opção seja selecionada por vez.
*   **Personalização do Pedido:** Sistema de caixas de seleção (*Checkbuttons*) para adicionar acompanhamentos (Granola, Paçoca, Leite em Pó, Nutella) ao pedido.
*   **Cálculo Dinâmico:** Processamento do valor total baseado na soma do item principal com os adicionais selecionados.
*   **Feedback ao Usuário:** Exibição de um resumo do pedido através de uma janela de mensagem (*pop-up*) após a finalização.

## 🛠️ Tecnologias Utilizadas
*   **Python:** Linguagem base para a lógica do sistema.
*   **Tkinter:** Biblioteca padrão do Python utilizada para criar a interface gráfica (janelas, botões e controles de seleção).
*   **Pillow (PIL):** (Opcional/Preparado) Utilizada para manipulação e exibição de imagens na interface.
*   **Faker:** Biblioteca incluída para possível geração de dados fictícios ou testes.

## 💻 Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as bibliotecas necessárias caso não as possua:
   ```bash
   pip install pillow faker
