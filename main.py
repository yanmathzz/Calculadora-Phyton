# importando tkinter e módulos necessários
from tkinter import *
from tkinter import ttk, messagebox
import math
import json
import os

# cores
cor1 = "#3b3b3b"  # preto/black
cor2 = "#feffff"  # branco/white
cor3 = "#38576b"  # azul carregado
cor4 = "#ECEFF1"  # cinzento
cor5 = "#FFAB40"  # laranja/Orange
cor6 = "#2E7D32"  # verde para memória
cor7 = "#C62828"  # vermelho para limpar

# Configurações
HISTORICO_FILE = "historico_calculadora.json"
MEMORIA_FILE = "memoria_calculadora.txt"

# Variáveis globais
todos_valores = ''
memoria = 0
historico = []
tema_escuro = False

# Lista para armazenar referências dos botões
botoes = []

# Função para carregar histórico
def carregar_historico():
    global historico
    try:
        if os.path.exists(HISTORICO_FILE):
            with open(HISTORICO_FILE, 'r') as f:
                historico = json.load(f)
    except:
        historico = []

# Função para salvar histórico
def salvar_historico():
    try:
        with open(HISTORICO_FILE, 'w') as f:
            json.dump(historico[-50:], f)
    except:
        pass

# Função para carregar memória
def carregar_memoria():
    global memoria
    try:
        if os.path.exists(MEMORIA_FILE):
            with open(MEMORIA_FILE, 'r') as f:
                memoria = float(f.read())
    except:
        memoria = 0

# Função para salvar memória
def salvar_memoria():
    try:
        with open(MEMORIA_FILE, 'w') as f:
            f.write(str(memoria))
    except:
        pass

# Função para alternar tema
def alternar_tema():
    global tema_escuro, cor1, cor2, cor3, cor4, cor5
    
    tema_escuro = not tema_escuro
    
    if tema_escuro:
        # Tema escuro
        cor1 = "#121212"
        cor2 = "#FFFFFF"
        cor3 = "#1E1E1E"
        cor4 = "#2D2D2D"
        cor5 = "#BB86FC"
    else:
        # Tema claro
        cor1 = "#3b3b3b"
        cor2 = "#feffff"
        cor3 = "#38576b"
        cor4 = "#ECEFF1"
        cor5 = "#FFAB40"
    
    # Atualizar cores
    janela.config(bg=cor1)
    frame_tela.config(bg=cor3)
    frame_corpo.config(bg=cor1)
    app_label.config(bg=cor3, fg=cor2)
    
    # Atualizar cores dos botões
    for btn in botoes:
        texto = btn.cget("text")
        if texto in ["C", "CE"]:
            btn.config(bg=cor7, fg=cor2)
        elif texto in ["M+", "M-", "MR", "MC"]:
            btn.config(bg=cor6, fg=cor2)
        elif texto in ["+", "-", "*", "/", "=", "x²", "√", "sin", "cos", "tan", "log", "π", "e", "x^y", "×", "÷"]:
            btn.config(bg=cor5, fg=cor2)
        else:
            btn.config(bg=cor4, fg=cor1)

# Função para adicionar ao histórico
def adicionar_historico(expressao, resultado):
    entrada = f"{expressao} = {resultado}"
    historico.append(entrada)
    salvar_historico()

# Função para mostrar histórico
def mostrar_historico():
    if not historico:
        messagebox.showinfo("Histórico", "Nenhum cálculo no histórico.")
        return
    
    historico_window = Toplevel(janela)
    historico_window.title("Histórico de Cálculos")
    historico_window.geometry("400x400")
    historico_window.config(bg=cor4)
    
    # Frame para lista
    frame_lista = Frame(historico_window, bg=cor4)
    frame_lista.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    # Scrollbar
    scrollbar = Scrollbar(frame_lista)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    # Listbox
    lista = Listbox(frame_lista, yscrollcommand=scrollbar.set, 
                    bg=cor2, fg=cor1, font=('Arial', 10), height=15)
    
    for item in reversed(historico[-20:]):
        lista.insert(END, item)
    
    lista.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=lista.yview)
    
    # Botão para limpar
    btn_limpar = Button(historico_window, text="Limpar Histórico", 
                       command=lambda: limpar_historico(lista),
                       bg=cor7, fg=cor2, font=('Arial', 10))
    btn_limpar.pack(pady=5)

def limpar_historico(lista_widget):
    global historico
    historico = []
    lista_widget.delete(0, END)
    salvar_historico()
    messagebox.showinfo("Histórico", "Histórico limpo com sucesso!")

# Funções de memória
def memoria_mais():
    global memoria, todos_valores
    try:
        if todos_valores:
            resultado = calcular()
            if resultado and resultado != "Erro":
                memoria += float(resultado)
                salvar_memoria()
                atualizar_display_memoria()
    except:
        pass

def memoria_menos():
    global memoria, todos_valores
    try:
        if todos_valores:
            resultado = calcular()
            if resultado and resultado != "Erro":
                memoria -= float(resultado)
                salvar_memoria()
                atualizar_display_memoria()
    except:
        pass

def memoria_recall():
    global todos_valores
    todos_valores += str(memoria)
    valor_texto.set(todos_valores)

def memoria_clear():
    global memoria
    memoria = 0
    salvar_memoria()
    atualizar_display_memoria()

def atualizar_display_memoria():
    if memoria != 0:
        label_memoria.config(text=f"M: {memoria:.2f}", fg=cor5)
    else:
        label_memoria.config(text="", fg=cor5)

# Função simplificada para calcular
def calcular():
    global todos_valores
    if not todos_valores:
        return None
    
    try:
        # Converter símbolos especiais
        expressao = todos_valores
        expressao = expressao.replace('π', str(math.pi))
        expressao = expressao.replace('e', str(math.e))
        expressao = expressao.replace('x²', '**2')
        expressao = expressao.replace('^', '**')
        expressao = expressao.replace('√', 'math.sqrt')
        expressao = expressao.replace('×', '*')
        expressao = expressao.replace('÷', '/')
        
        # Funções especiais (simplificado)
        if 'sin(' in expressao:
            expressao = expressao.replace('sin(', 'math.sin(math.radians(')
        if 'cos(' in expressao:
            expressao = expressao.replace('cos(', 'math.cos(math.radians(')
        if 'tan(' in expressao:
            expressao = expressao.replace('tan(', 'math.tan(math.radians(')
        if 'log(' in expressao:
            expressao = expressao.replace('log(', 'math.log10(')
        
        # Calcular
        resultado = eval(expressao, {"__builtins__": {}}, 
                        {"math": math, "sqrt": math.sqrt})
        
        # Formatar resultado
        if isinstance(resultado, float):
            if resultado.is_integer():
                resultado = int(resultado)
            else:
                # Limitar casas decimais
                resultado = round(resultado, 10)
        
        adicionar_historico(todos_valores, resultado)
        todos_valores = str(resultado)
        valor_texto.set(resultado)
        return str(resultado)
        
    except Exception as e:
        valor_texto.set("Erro")
        todos_valores = ''
        return "Erro"

# Função para entrar valores
def entrar_valores(valor):
    global todos_valores
    todos_valores = todos_valores + str(valor)
    valor_texto.set(todos_valores)

# Função para apagar último caractere
def backspace():
    global todos_valores
    todos_valores = todos_valores[:-1]
    valor_texto.set(todos_valores if todos_valores else '0')

# Função para alternar parênteses
def alternar_parenteses():
    global todos_valores
    if todos_valores.count('(') > todos_valores.count(')'):
        todos_valores += ')'
    else:
        todos_valores += '('
    valor_texto.set(todos_valores)

# Funções limpar
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('0')

def limpar_entrada():
    global todos_valores
    todos_valores = ''
    valor_texto.set('0')

# Funções matemáticas especiais
def raiz_quadrada():
    global todos_valores
    todos_valores += '√('
    valor_texto.set(todos_valores)

def quadrado():
    global todos_valores
    todos_valores += 'x²'
    valor_texto.set(todos_valores)

def potencia():
    global todos_valores
    todos_valores += '^'
    valor_texto.set(todos_valores)

def seno():
    global todos_valores
    todos_valores += 'sin('
    valor_texto.set(todos_valores)

def cosseno():
    global todos_valores
    todos_valores += 'cos('
    valor_texto.set(todos_valores)

def tangente():
    global todos_valores
    todos_valores += 'tan('
    valor_texto.set(todos_valores)

def logaritmo():
    global todos_valores
    todos_valores += 'log('
    valor_texto.set(todos_valores)

def inserir_pi():
    global todos_valores
    todos_valores += 'π'
    valor_texto.set(todos_valores)

def inserir_e():
    global todos_valores
    todos_valores += 'e'
    valor_texto.set(todos_valores)

# Configuração da janela principal
janela = Tk()
janela.title("Calculadora Avançada")
janela.geometry("355x480")  # Ajustado para caber melhor
janela.config(bg=cor1)

# Carregar dados
carregar_historico()
carregar_memoria()

# Criando frames
frame_tela = Frame(janela, width=355, height=70, bg=cor3)
frame_tela.grid(row=0, column=0, columnspan=5, padx=2, pady=2)

frame_corpo = Frame(janela, width=355, height=380, bg=cor1)
frame_corpo.grid(row=1, column=0, columnspan=5, padx=2, pady=2)

# Criando Label para display
valor_texto = StringVar()
valor_texto.set('0')

app_label = Label(frame_tela, textvariable=valor_texto, width=20, height=2, padx=7,
                  relief=FLAT, anchor='e', justify=RIGHT, font=('Arial 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# Label para memória
label_memoria = Label(frame_tela, text="", font=('Arial 9'), bg=cor3, fg=cor5)
label_memoria.place(x=300, y=5)
atualizar_display_memoria()

# ========== BOTÕES ==========

# Função auxiliar para criar botões e adicionar à lista
def criar_botao(texto, comando, x, y, cor_fundo=cor4, cor_texto=cor1, largura=5):
    btn = Button(frame_corpo, text=texto, command=comando, width=largura, height=2,
                 bg=cor_fundo, fg=cor_texto, font=('Arial 10 bold'),
                 relief=RAISED, overrelief=RIDGE)
    btn.place(x=x, y=y)
    botoes.append(btn)
    return btn

# Linha 1: Limpar, Histórico e Tema
b_1 = criar_botao("C", limpar_tela, 5, 5, cor7, cor2)
b_ce = criar_botao("CE", limpar_entrada, 70, 5, cor7, cor2)
b_hist = criar_botao("Hist", mostrar_historico, 135, 5)
b_theme = criar_botao("Tema", alternar_tema, 200, 5)
b_backspace = criar_botao("⌫", backspace, 265, 5)

# Linha 2: Memória
b_mc = criar_botao("MC", memoria_clear, 5, 60, cor6, cor2)
b_mr = criar_botao("MR", memoria_recall, 70, 60, cor6, cor2)
b_m_plus = criar_botao("M+", memoria_mais, 135, 60, cor6, cor2)
b_m_minus = criar_botao("M-", memoria_menos, 200, 60, cor6, cor2)
b_parenteses = criar_botao("()", alternar_parenteses, 265, 60)

# Linha 3: Funções científicas
b_sqrt = criar_botao("√", raiz_quadrada, 5, 115, cor5, cor2)
b_pow = criar_botao("x^y", potencia, 70, 115, cor5, cor2)
b_sin = criar_botao("sin", seno, 135, 115, cor5, cor2)
b_cos = criar_botao("cos", cosseno, 200, 115, cor5, cor2)
b_tan = criar_botao("tan", tangente, 265, 115, cor5, cor2)

# Linha 4: Mais funções
b_log = criar_botao("log", logaritmo, 5, 170, cor5, cor2)
b_pi = criar_botao("π", inserir_pi, 70, 170, cor5, cor2)
b_e = criar_botao("e", inserir_e, 135, 170, cor5, cor2)
b_quadrado = criar_botao("x²", quadrado, 200, 170, cor5, cor2)
b_percent = criar_botao("%", lambda: entrar_valores("%"), 265, 170)

# Linha 5: Números 7, 8, 9
b_7 = criar_botao("7", lambda: entrar_valores("7"), 5, 225)
b_8 = criar_botao("8", lambda: entrar_valores("8"), 70, 225)
b_9 = criar_botao("9", lambda: entrar_valores("9"), 135, 225)
b_mult = criar_botao("×", lambda: entrar_valores("×"), 200, 225, cor5, cor2)
b_div = criar_botao("÷", lambda: entrar_valores("÷"), 265, 225, cor5, cor2)

# Linha 6: Números 4, 5, 6
b_4 = criar_botao("4", lambda: entrar_valores("4"), 5, 280)
b_5 = criar_botao("5", lambda: entrar_valores("5"), 70, 280)
b_6 = criar_botao("6", lambda: entrar_valores("6"), 135, 280)
b_sub = criar_botao("-", lambda: entrar_valores("-"), 200, 280, cor5, cor2)

# Linha 7: Números 1, 2, 3
b_1_num = criar_botao("1", lambda: entrar_valores("1"), 5, 335)
b_2_num = criar_botao("2", lambda: entrar_valores("2"), 70, 335)
b_3_num = criar_botao("3", lambda: entrar_valores("3"), 135, 335)
b_add = criar_botao("+", lambda: entrar_valores("+"), 200, 335, cor5, cor2)

# Linha 8: Número 0, ponto, igual
b_0 = criar_botao("0", lambda: entrar_valores("0"), 5, 390, largura=11)
b_point = criar_botao(".", lambda: entrar_valores("."), 135, 390)
b_equals = criar_botao("=", calcular, 200, 390, cor5, cor2, largura=11)

# ========== ATALHOS DE TECLADO ==========
def tecla_pressionada(event):
    key = event.char
    keysym = event.keysym
    
    if key in '0123456789':
        entrar_valores(key)
    elif key in '+-*/.':
        entrar_valores(key)
    elif key == '%':
        entrar_valores('%')
    elif keysym == 'Return' or key == '=':
        calcular()
    elif keysym == 'Escape':
        limpar_tela()
    elif keysym == 'BackSpace':
        backspace()
    elif keysym == 'Delete':
        limpar_entrada()
    elif key == '(' or key == ')':
        entrar_valores(key)
    elif key == 'p' or key == 'P':
        inserir_pi()
    elif key == 'e' or key == 'E':
        inserir_e()

# Vincular eventos de teclado
janela.bind('<Key>', tecla_pressionada)

# Focar na janela principal
janela.focus_set()

# Iniciar loop principal
print("=== CALCULADORA INICIADA ===")
print("Funcionalidades disponíveis:")
print("1. Operações básicas: +, -, ×, ÷")
print("2. Funções científicas: sin, cos, tan, log, √")
print("3. Memória: MC, MR, M+, M-")
print("4. Histórico: botão 'Hist'")
print("5. Temas: botão 'Tema'")
print("6. Atalhos de teclado disponíveis")

janela.mainloop()
