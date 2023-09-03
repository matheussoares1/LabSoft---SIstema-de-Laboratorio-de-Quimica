#Importando Biblioteca
import customtkinter as ctk
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd


# importando pillow
from PIL import ImageTk, Image


# Importando VIew

from view import *



nova_janela = ctk.CTk()
nova_janela.title("Vidrarias")
nova_janela.geometry("1000x600")
nova_janela.maxsize(width=1366, height=768)
nova_janela.minsize(width=500, height=300)
nova_janela.resizable(width=False, height=False)

#nova_janela = ctk.set_appearance_mode("light")

label = Label(nova_janela, text="Nome da Vidraria")
label.place(x=50, y=30)
enome_nome = ctk.CTkEntry(nova_janela, width=400, height=40).place(x=50, y=50)

label = Label(nova_janela, text="Nome da Vidraria")
label.place(x=550, y=30)
enome_quantidade = ctk.CTkEntry(nova_janela, width=400,height=40).place(x=550, y=50)

label = Label(nova_janela, text="Nome da Vidraria")
label.place(x=50, y=100)
enome_capacidade = ctk.CTkEntry(nova_janela,width=400, height=40).place(x=50, y=120)

label = Label(nova_janela, text="Nome da Vidraria")
label.place(x=550, y=100)
enome_uni_medida = ctk.CTkEntry(nova_janela, width=400, height=40).place(x=550, y=120)

label = Label(nova_janela, text="Nome da Vidraria")
label.place(x=50, y=180)
enome_descricao = ctk.CTkEntry(nova_janela,  width=900, height=150).place(x=50, y=200)

label = Label(nova_janela, text="Nome da Vidraria")
label.place(x=50, y=360)
enome_cuidados = ctk.CTkEntry(nova_janela, width=900, height=150).place(x=50, y=380)


nova_janela.mainloop()