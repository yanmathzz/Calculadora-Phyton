#importando tkinter
from tkinter import *
from tkinter import ttk

#cores

cor1 = "#3b3b3b" #preto/black
cor2 = "#feffff" #branco/white 
cor3 = "#38576b" #azul carregado
cor4 = "#ECEFF1" #cinzento
cor5 = "#FFAB40" #laranja/Orange


janela =Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)


#criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#criando botoes 

b_1 = Button(frame_corpo, text="C", width=11, height=2)
b_1.place(x=0, y=0)
b_1 = Button(frame_corpo, text="%", width=11, height=2)
b_1.place(x=100, y=0)
b_1 = Button(frame_corpo, text="/", width=11, height=2)
b_1.place(x=177, y=0)


janela.mainloop()
