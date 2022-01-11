from tkinter import *
import tkinter as tk
from tkinter import colorchooser
import time

telaInicial = tk.Tk()

localImagem = 0 #has

def importarImagem():

    def novaTela():
        global localImagem #has

        localImagem = str(novaImagem.get())

        global telaInicial #has
        global labelFundo #has

        imageFundo = PhotoImage(file=(f"{localImagem}"))
        labelFundo.configure(image=imageFundo) #has

        bt2.destroy()
        bt1.destroy()
        btn6.destroy()
        novaImagem.destroy()
        labelAscii.destroy()
        labePython.destroy()
        entradaCor.destroy()

        telaInicial.mainloop()

    def inicio(calculo):
        global x1, y1
        x1 = calculo.x
        y1 = calculo.y

    def fimPlace(arg, telaInicial):
        global x1, y1
        print(f'.place(width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1})')

        telaInicial.clipboard_clear()
        telaInicial.clipboard_append(f'.place(width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1})')

    def paraGeometry(telaInicial):
        print(f'.geometry("{telaInicial.geometry()}")')

        telaInicial.clipboard_clear()
        telaInicial.clipboard_append(f'.geometry("{telaInicial.geometry()}")')

    tempo = print('''****PROGRAMA PARA MAPEAMENTO DE CONSTRUÇÃO DE TELA****\n

     1 - A tela gráfica é expansivo

     2 - Clica com o botão esquerdo do mouse em qualquer ponto da tela e arraste na outra direção: 

     mostrará as coordenadas do width/height e os valores do eixo x/y

     3 - Clica com o botão scroll (meio do mouse) para obter o valor da geometry

    ''')

    time.sleep(0.5)

    novaImagem = Entry(telaInicial, width=30, bg='white')
    novaImagem.place(x=458, y=225)

    btn6 = Button(telaInicial, text=('OK'), command=novaTela)
    btn6.place(width=28, height=20, x=650, y=225)
    btn6.place()

    novaImagem.delete(0, END)

    x1 = y1 = 0

    def cliqueMapeamento(retorno):
        print(f'X={retorno.x} / Y={retorno.y}')

    telaInicial.bind("<Button-1>", cliqueMapeamento)
    telaInicial.bind('<Button-1>', inicio)
    telaInicial.bind('<ButtonRelease-1>', lambda arg: fimPlace(arg, telaInicial))
    telaInicial.bind('<Button-2>', lambda arg: paraGeometry(telaInicial))

    telaInicial.mainloop()

def sairMenu():
    telaInicial.destroy() #has

def menu():
    btn3 = Button(telaInicial, text="Padrão", command=xY1)

    btn3.place(width=115, height=30, x=558, y=108)
    btn3.place()

    btn4 = Button(telaInicial, text="Importar Imagem", command=importarImagem)
    btn4.place(width=115, height=30, x=558, y=139)
    btn4.place()

    btn5 = Button(telaInicial, text="Sair", command=sairMenu)
    btn5.place(width=115, height=30, x=558, y=172)
    btn5.place()

#-------- DIMENSIONAMENTO DE WIDGHTS ---------#

def xY1():
    telaInicial = tk.Tk()

    x1 = y1 = 0

    def inicio(calculo):
        global x1, y1
        x1 = calculo.x
        y1 = calculo.y

    def fimPlace(arg, telaInicial):
        global x1, y1
        print(f'.place(width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1})')

        telaInicial.clipboard_clear()
        telaInicial.clipboard_append(f'.place(width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1})')

    def paraGeometry(telaInicial):
        print(f'.geometry("{telaInicial.geometry()}")')
        telaInicial.clipboard_clear()
        telaInicial.clipboard_append(f'.geometry("{telaInicial.geometry()}")')

    tempo = print('''****PROGRAMA PARA MAPEAMENTO DE CONSTRUÇÃO DE TELA****\n

     1 - A tela gráfica é expansivo

     2 - Clica com o botão esquerdo do mouse em qualquer ponto da tela e arraste na outra direção: 

     mostrará as coordenadas do width/height e os valores do eixo x/y

     3 - Clica com o botão scroll (meio do mouse) para obter o valor da geometry

    ''')

    time.sleep(2)

# --------------- PRINCIPAL xY ----------------#

    telaInicial.title("DIMENSIONAMENTO")
    telaInicial.resizable(0,0)#width=False, height=False)
    telaInicial.config(bg="#030303")
    telaInicial.geometry('600x200')
    telaInicial.resizable(width=True, height=True)
    telaInicial.attributes('-alpha', 0.7)

    def cliqueMapeamento(retorno):
        print(f'X={retorno.x} / Y={retorno.y}')

    telaInicial.bind("<Button-1>", cliqueMapeamento)
    telaInicial.bind('<Button-1>', inicio)
    telaInicial.bind('<ButtonRelease-1>', lambda arg: fimPlace(arg, telaInicial))
    telaInicial.bind('<Button-2>', lambda arg: paraGeometry(telaInicial))

    telaInicial.mainloop()

#------------------ CORES ASCII-----------------------------------#

def obterCor1():
    aSCII = colorchooser.askcolor()
    cor = aSCII[1].upper()
    labelAscii['bg'] = cor

    entradaCor.delete(0, END)
    entradaCor.insert(0, cor)

    telaInicial.clipboard_clear()
    telaInicial.clipboard_append(cor)

    entradaCor["bg"] = cor

def inicio(calculo):
    global x1, y1
    x1 = calculo.x
    y1 = calculo.y

# --------------- PRINCIPAL -----------------#

telaInicial.title("                                                                                     ***F E R R A M E N T A***")
telaInicial.resizable(width=False, height=False)

imageFundo = PhotoImage(file=r"E:\Python\PycharmProjects3\Projeto_Mega_Sena\imagem_tela_pai2.png")

labelFundo = Label(telaInicial, image=imageFundo)
labelFundo.pack()

labePython = Label(telaInicial, bg="#00010F", fg='green', text="PYTHON", font=('calibri', '15', 'bold'))
labePython.place(width=150, height=20, x=270, y=199)

labelAscii = Label(telaInicial, bg='#d9d9d9')

bt1 = Button(telaInicial, text='OK', command=obterCor1)
bt1.place(width=47, height=26, x=73, y=167)

entradaCor = Entry(telaInicial, justify='center')
entradaCor.place(width=133, height=25, x=29, y=125)

bt2 = Button(telaInicial, text="DIMENSIONAMENTO", font=('arial', '8', 'bold'), justify='center', command=menu)
bt2.place(width=111, height=30, x=560, y=139)

telaInicial.bind('<Button-1>', inicio)

telaInicial.mainloop()