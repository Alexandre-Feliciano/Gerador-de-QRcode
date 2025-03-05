import qrcode
from PIL import Image, ImageTk  
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

root = tk.Tk()
root.title("Gerador de QRcode")
root.geometry("480x510")  

root.config(bg="#1D1C1A")
root.resizable(0, 0)

frame1 = tk.Frame(root, bd=2, relief=tk.RAISED)
frame1.place(x=50, y=20, width=380, height=350)

frame2 = tk.Frame(root, bd=2, relief=tk.RAISED)
frame2.place(x=50, y=390, width=380, height=100)


cover_img = tk.PhotoImage(file="img/logo.png")

qr_canvas = tk.Canvas(frame1, width=380, height=350)
qr_canvas.create_image(190, 175, anchor=tk.CENTER, image=cover_img)
qr_canvas.image = cover_img
qr_canvas.bind("<Double-1>", lambda e: salvar_QRcode())
qr_canvas.pack(fill=tk.BOTH)

def criar_QRcode(*args):
    global img_tk  # Variável global para manter a referência da imagem

    dados = input_texto.get()
    
    if dados:
        img = qrcode.make(dados)  
        img = img.convert("RGB")  
        
        img = img.resize((350, 350), Image.Resampling.LANCZOS)

        img_tk = ImageTk.PhotoImage(img) 

        qr_canvas.delete("all") 
        qr_canvas.create_image(190, 175, anchor=tk.CENTER, image=img_tk)
        qr_canvas.image = img_tk 

def salvar_QRcode():
    dados = input_texto.get()
    if not dados:
        messagebox.showwarning("Aviso", "Insira um texto antes de salvar o QR Code.")
        return

    img = qrcode.make(dados)
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")]
    )

    if file_path:
        img.save(file_path)
        messagebox.showinfo("Sucesso", "QR Code salvo com sucesso!")

input_texto = ttk.Entry(frame2, width=40, font="Arial", justify=tk.CENTER)
input_texto.bind("<Return>", criar_QRcode)
input_texto.place(x=5, y=5)

button_create = ttk.Button(frame2, text="Criar", width=10, command=criar_QRcode)
button_create.place(x=25, y=50)

button_save = ttk.Button(frame2, text="Salvar", width=10, command=salvar_QRcode)
button_save.place(x=100, y=50)

button_exit = ttk.Button(frame2, text="Sair", width=10, command=root.quit)
button_exit.place(x=175, y=50)

root.mainloop()
