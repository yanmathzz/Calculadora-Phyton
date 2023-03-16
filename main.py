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

frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)


janela.mainloop()
