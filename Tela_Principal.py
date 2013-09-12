from Tkinter import *
import Image, ImageTk
from tkMessageBox import *

root = Tk()

#Funcao para Abrir a Tela do Banco de Dados
def Database():
        master = Tk()

        i=0
        linha = []

        #for i in [0,1,2,3,4,5]:
        coluna1 = Label(master, text="COLUNA1 |").grid(row=i, column=0, sticky=W)
        coluna2 = Label(master, text="COLUNA2 |").grid(row=i, column=1, sticky=W)
        coluna3 = Label(master, text="COLUNA3 |").grid(row=i, column=2, sticky=W)
        coluna4 = Label(master, text="COLUNA4 |").grid(row=i, column=3, sticky=W)
        botaoCarregar = Button(master,text='Carregar').grid(row=i, column=4, sticky=W)
        botaoExcluir = Button(master,text='Excluir',state=DISABLED).grid(row=i, column=5, sticky=W)
        master.mainloop()

#Comando para definir o tamanho e titulo da tela princial
root.geometry("800x600+100+100")
root.title("Projeto Final Processamento de Imagens 2013.1")

# Comando para nao maximizar a tela
root.resizable(width=FALSE, height=FALSE)

#Frame dos Botoes
frame2=Frame(root)
frame2.place(width=530,height=40,x=10,y=540)

#Frame para Steps i
frame3=Frame(root)
frame3.place(x=550,y=540)

#Frame para Steps j
frame4=Frame(root)
frame4.place(x=550,y=575)

#Frame para Pictures i
frame5=Frame(root)
frame5.place(x=650,y=540)

#Frame para Pictures j
frame6=Frame(root)
frame6.place(x=650,y=575)

#Criando o Frame das Imagens e ScrollBar

frame = Frame(root, bd=2, width=500,height=500,background="Red")
frame.place(x=10,y=10)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=E+W)

yscrollbar = Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=N+S)

canvas = Canvas(frame, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)


img1 = ImageTk.PhotoImage(Image.open("foto001.jpg"))
img2 = ImageTk.PhotoImage(Image.open("foto002.jpg"))

canvas.create_image(0,0,image=img1, anchor="nw")
canvas.create_image(510,0,image=img2, anchor="nw")

canvas.config(scrollregion=canvas.bbox(ALL),width=750,height=500)

xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)

#Criando os Botoes
go       = Button(frame2,width=15,text='Go!').pack(side=LEFT)
new      = Button(frame2,width=15,text='New').pack(side=LEFT,padx=10)
save     = Button(frame2,width=15,text='Save').pack(side=LEFT,padx=10)
database = Button(frame2,width=15,text='Database',command=Database).pack(side=LEFT,padx=10)

#Criando os widgets Label e Entry
Label (frame3,text='Steps i:').pack(side=LEFT)
textoStepsi = Entry(frame3,width=10).pack(side=LEFT)
#delete(0,END)
#textoStepsi.insert(0,"Testes")

Label (frame4,text='Steps j:').pack(side=LEFT)
Entry(frame4,width=10).pack(side=LEFT)

Label (frame5,text='Pictures i:').pack(side=LEFT)
Entry(frame5,width=10).pack(side=LEFT)

Label (frame6,text='Pictures j:').pack(side=LEFT)
Entry(frame6,width=10).pack(side=LEFT)





root.mainloop()
