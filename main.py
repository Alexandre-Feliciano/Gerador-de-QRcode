# Primeiro instalar o qrcode pillow

# importar os modulos

import qrcode, PIL
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# fazendo as funções

def criar_QRcode(*args):
    ...
    
def salvar_QRcode():
    ...
    
# criando interface gráfica do usuário

root = tk.Tk()
root.title("Gerador de QRcode")
root.geometry("480x510") #width x height

# configurando a janela

root.config(bg="#1D1C1A")
root.resizable(0,0)

# adicionando frames a tela

frame1 = tk.Frame(root, bd = 2, relief = tk.RAISED)
frame1.place(x = 50, y = 20, width = 380, height = 350) 

frame2 = tk.Frame(root, bd = 2, relief = tk.RAISED)
frame2.place(x = 50, y = 390, width = 380, height = 100) 

# Criando o canvas do QRcode

img = tk.PhotoImage(file = "img/logo.png")


qr_code = tk.Canvas(frame1)
qr_code.create_image(0,0, anchor= tk.NW, image = img )

# qr_code = tk.Pack(fill = tk.BOTH)

# adicionando input de texto

input_texto = ttk.Entry(frame2, width = 40, font= "Arial", justify= tk.CENTER)
input_texto.place( x= 5, y=5)

# adicionando botões

button_create= ttk.Button(frame2, text= "Criar", width=10, command= criar_QRcode)
button_create.place(x=25, y=50)

button_save= ttk.Button(frame2, text= "Salvar", width=10, command= salvar_QRcode)
button_save.place(x=100, y=50)

button_exit= ttk.Button(frame2, text= "Sair", width=10,command= root.quit)
button_exit.place(x=175, y=50)


root.mainloop()

