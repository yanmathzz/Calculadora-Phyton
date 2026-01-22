# Calculadora Avançada em Python 🧮

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Ativo-success)

Uma calculadora completa desenvolvida em Python com interface gráfica Tkinter, oferecendo operações básicas, científicas e recursos avançados.

### 🎨 **Temas Personalizáveis**
- Tema Claro (padrão)
- Tema Escuro
- Botão para alternância rápida

### 📚 **Histórico de Cálculos**
- Armazenamento automático em arquivo JSON
- Visualização em janela separada
- Limpeza seletiva do histórico
- Mantém últimos 50 cálculos

### 💾 **Sistema de Memória**
- **MC** - Memória Clear (Limpar)
- **MR** - Memória Recall (Recuperar)
- **M+** - Memória Plus (Adicionar)
- **M-** - Memória Minus (Subtrair)
- Persistente entre sessões

### 🔬 **Funções Científicas**
- **√** Raiz quadrada
- **x²** Quadrado
- **x^y** Potência
- **sin/cos/tan** Funções trigonométricas
- **log** Logaritmo base 10
- **π** Constante Pi (3.14159...)
- **e** Constante de Euler (2.71828...)

### ⌨️ **Atalhos de Teclado**
- **Teclas numéricas**: 0-9
- **Operadores**: +, -, *, /, .
- **Enter** ou **=**: Calcular
- **Escape**: Limpar tudo
- **Backspace**: Apagar caractere
- **Delete**: Limpar entrada
- **P**: Inserir π
- **E**: Inserir e

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Instalação e Execução
```bash
# Clone o repositório
git clone https://github.com/yanmathzz/Calculadora-Phyton.git

# Acesse o diretório
cd Calculadora-Phyton

# Execute a calculadora
python calculadora.py
```

### Execução Rápida
```bash
python calculadora.py
```

## 🎮 Como Usar

### Interface Gráfica
- Clique nos botões com o mouse
- Use atalhos de teclado para maior velocidade
- O resultado é exibido no display superior

### Operações Básicas
1. Digite os números
2. Selecione a operação (+, -, ×, ÷)
3. Pressione "=" para calcular

### Funções Avançadas
- **Histórico**: Clique em "Hist" para ver cálculos anteriores
- **Memória**: Use os botões MC, MR, M+, M-
- **Temas**: Clique em "Tema" para alternar claro/escuro
- **Funções Científicas**: Use os botões na parte superior

## 📁 Estrutura do Projeto

```
Calculadora-Phyton/
├── calculadora.py          # Código principal
├── README.md              # Documentação
├── historico_calculadora.json  # Histórico (criado automaticamente)
├── memoria_calculadora.txt     # Memória (criado automaticamente)
└── LICENSE                # Licença MIT
```

### Arquivos Gerados Automaticamente:
- `historico_calculadora.json` - Armazena histórico de cálculos
- `memoria_calculadora.txt` - Armazena valor da memória

## 🔧 Tecnologias Utilizadas

- **Python 3** - Linguagem principal
- **Tkinter** - Interface gráfica
- **JSON** - Armazenamento de histórico
- **Math** - Funções matemáticas

## 📊 Funcionalidades Detalhadas

### Operações Suportadas
- **Aritméticas**: Adição, Subtração, Multiplicação, Divisão
- **Científicas**: Potenciação, Raiz, Trigonometria, Logaritmos
- **Especiais**: Porcentagem, Constantes matemáticas
- **Utilitárias**: Memória, Histórico, Temas

### Interface
- Display grande com fonte clara
- Botões coloridos por categoria
- Layout organizado em grades
- Feedback visual em botões
- Indicador de memória ativa

## ⚙️ Personalização

### Modificar Cores
Edite as variáveis no início do código:
```python
cor1 = "#3b3b3b"  # Cor de fundo
cor2 = "#feffff"  # Cor do texto
cor3 = "#38576b"  # Cor do display
cor4 = "#ECEFF1"  # Cor dos botões normais
cor5 = "#FFAB40"  # Cor dos botões de operação
cor6 = "#2E7D32"  # Cor dos botões de memória
cor7 = "#C62828"  # Cor dos botões de limpeza
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨💻 Autor

**Yan Matheus** - [@yanmathzz](https://github.com/yanmathzz)
