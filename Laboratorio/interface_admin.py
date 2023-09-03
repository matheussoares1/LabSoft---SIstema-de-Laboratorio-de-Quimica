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



janela = ctk.CTk()

janela.title("Sistema de Laboratorio")
janela.geometry("1366x768")
janela.maxsize(width=1366, height=768)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)


cor1 = "#0061D3" #Azul Menu Lateral
cor2 = "#ffffff" #Cor Letras Menu Lateral - Branca
cor3 = "#2e2d2b" #Preto
cor4 = "#f5df4d" # Amarelo
cor5 = "#20a095" # Verde
cor6 = "#003452" # Azul
cor7 = "#ef5350" # Vermelho
cor8 = "#0075FF" # Azul Botao Selection

#//////////////////////////////////////////////////////////////////////////////////////////////////
#Criando Frames
frame_menu = ctk.CTkFrame(master=janela, width=210, height=768, fg_color=cor1).place(x=-10, y=0)

frame_tabela = ctk.CTkFrame(master=janela, width=1150, height=490).place(x=210, y=200)

frame_tabelal = Frame(janela, width=1150, height=490)
frame_tabelal.grid(row=9, column=0, pady=0, padx=10, sticky=NSEW)
frame_tabelal.place(x=210, y=200)



frame_dados_falta = ctk.CTkFrame(master=janela, width=300, height=180).place(x=230, y=10)

frame_dados_uso = ctk.CTkFrame(master=janela, width=300, height=180).place(x=550, y=10)

frame_dados_inadequados = ctk.CTkFrame(master=janela, width=300, height=180).place(x=870, y=10)

frame_botoes_inserir =ctk.CTkFrame(master=janela, width=160, height=30, fg_color = cor5).place(x=1190, y=10)

frame_botoes_ataulizar =ctk.CTkFrame(master=janela, width=160, height=30, fg_color = cor4).place(x=1190, y=45)

frame_botoes_deletar =ctk.CTkFrame(master=janela, width=160, height=30, fg_color = cor7).place(x=1190, y=80)

frame_pesquisa =ctk.CTkFrame(master=janela, width=160, height=70, fg_color = cor5).place(x=1190, y=120)

def dashboard():
		print("hello")

def vidrarias():
	def abrir_modal_vidrarias():
		nova_janela = ctk.CTkToplevel(janela)
		nova_janela.geometry("1000x600")
		nova_janela.maxsize(width=1366, height=768)
		nova_janela.minsize(width=500, height=300)
		nova_janela.resizable(width=False, height=False)

		enome_nome = ctk.CTkEntry(nova_janela, placeholder_text="CTkEntry", width=100, height=100).place(x=20, y=20)
		enome_quantidade = ctk.CTkEntry(nova_janela, placeholder_text="CTkEntry", height=100).place(x=0, y=20)
		enome_capacidade = ctk.CTkEntry(nova_janela, placeholder_text="CTkEntry").place(x=20, y=60)
		enome_uni_medida = ctk.CTkEntry(nova_janela, placeholder_text="CTkEntry").place(x=0, y=60)
		enome_descricao = ctk.CTkEntry(nova_janela, placeholder_text="CTkEntry").place(x=20, y=200)
		enome_cuidados = ctk.CTkEntry(nova_janela, placeholder_text="CTkEntry").place(x=20, y=400)



		def cadastro_vidrarias():
			nome = enome_nome.get()
			quantidade = enome_quantidade.get()
			capacidade = enome_capacidade.get()
			uni_medida = enome_uni_medida.get()
			descricao = enome_descricao.get()
			cuidados = enome_cuidados.get()


			lista_vidrarias = [nome, quantidade, capacidade, uni_medida, descricao, cuidados]

			# Caso esteja vazio haverá uma tela de insereçao de ddos obrigatórios
			for i in lista_vidrarias:
				if i=="":
					messagebox.showerror('Erro', 'Preencha todos os campos.')
					return

			#Inserindo dados no banco de dados 
			inserir_vidrarias(lista_vidrarias)

			# Mostrando mensagem de sucesso
			messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

			enome_nome.delete(0,END)
			enome_quantidade.delete(0,END)
			enome_capacidade.delete(0,END)
			enome_uni_medida.delete(0,END)
			enome_descricao.delete(0,END)
			enome_cuidados.delete(0,END)

			# Mostrando os valores na tabela
			mostrar_vidrarias()

	def mostrar_vidrarias():
		app_nome = ctk.CTkLabel(frame_tabelal, text="Apresentação de Planejamento", anchor=NW, bg_color=cor1, fg_color=cor4)
		app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

		# creating a treeview with dual scrollbars
		list_header = ['id','Nome', 'Quantidade','Capacidade','Unidade de Medida','Descrição','Cuidados']

		df_list = ver_vidrarias()

		global tree_personais

		tree_personais = ttk.Treeview(frame_tabelal, selectmode="extended",columns=list_header, show="headings")

			# vertical scrollbar
		vsb = ttk.Scrollbar(frame_tabelal, orient="vertical", command=tree_personais.yview)
		# horizontal scrollbar
		hsb = ttk.Scrollbar(frame_tabelal, orient="horizontal", command=tree_personais.xview)

		tree_personais.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
		tree_personais.grid(column=0, row=1, sticky='nsew')
		vsb.grid(column=1, row=1, sticky='ns')
		hsb.grid(column=0, row=2, sticky='ew')
		frame_tabelal.grid_rowconfigure(0, weight=12)
		
		hd=["nw","nw","nw","nw","nw","nw","nw"]
		h=[30,130,130,130,130,130,130]
		n=0
		
		for col in list_header:
   			tree_personais.heading(col, text=col.title(), anchor=NW)
   			tree_personais.column(col, width=h[n],anchor=hd[n])
   			n+=1

		for item in df_list:
			tree_personais.insert('', 'end', values=item)
	
	mostrar_vidrarias()




	botao_inserir_vidrarias = ctk.CTkButton(master=frame_botoes_inserir, text="Inserir",command=abrir_modal_vidrarias, width=160, height=30).place(x=1190, y=10)
	botao_atualizar = ctk.CTkButton(master=frame_botoes_ataulizar, text="Atualizar",command=abrir_modal_vidrarias, width=160, height=30).place(x=1190, y=45)
	botao_deletar = ctk.CTkButton(master=frame_botoes_deletar, text="Deletar",command=abrir_modal_vidrarias, width=160, height=30).place(x=1190, y=80)


def reagentes():
	botao_inserir_vidrarias = ctk.CTkButton(master=frame_botoes_inserir, text="TESTE", width=160, height=30).place(x=1190, y=10)

	print("Hello World")

def maquinas():
	print("Hello World")

def epis():
	print("Hello World")


def control(i):
	#CADASTRO DE CLIENTE
	if i == 'dashboard':

#		for widget in frame_botoes_inserir.winfo_children():
#			widget.destroy()

#		for widget in frame_tabela.winfo_children():
#			widget.destroy()

		dashboard()

	if i == 'vidrarias':
		print("Hello World!")
		vidrarias()

	if i == 'reagentes':
		reagentes()

	if i == 'maquinas':
		maquinas()

	if i == 'epis':
		epis()






#/////////////////////////////////////////////////////////////////////////////////////////////////////
#inserindo botoes menu

#Dashoard
img_dashboard = ctk.CTkImage(light_image=Image.open("./Imagens/dashboard.png"),dark_image=Image.open("./Imagens/dashboard.png"),size=(30, 30))
botao_dashboard = ctk.CTkButton(master=frame_menu, text="Dashboard",command=lambda:control('dashboard'), image=img_dashboard, width=210, height=40,corner_radius=0, hover_color=cor8, fg_color=cor1).place(x=-10, y=200) 
#Vidrarias
img_vidrarias = ctk.CTkImage(light_image=Image.open("./Imagens/vidrarias.png"),dark_image=Image.open("./Imagens/vidrarias.png"),size=(30, 30))
botao_vidrarias = ctk.CTkButton(master=frame_menu, text="Vidrarias",command=lambda:control('vidrarias'),image=img_vidrarias, width=210, height=40,corner_radius=0, hover_color=cor8, fg_color=cor1).place(x=-10, y=250) 
#Reagentes
img_reagentes = ctk.CTkImage(light_image=Image.open("./Imagens/reagentes.png"),dark_image=Image.open("./Imagens/reagentes.png"),size=(30, 30))
botao_reagentes = ctk.CTkButton(master=frame_menu, text="Reagentes",command=lambda:control('reagentes'),image=img_reagentes, width=210, height=40,corner_radius=0, hover_color=cor8, fg_color=cor1).place(x=-10, y=300) 
#Maquinas
img_maquinas = ctk.CTkImage(light_image=Image.open("./Imagens/maquinas.png"),dark_image=Image.open("./Imagens/maquinas.png"),size=(30, 30))
botao_maquinas = ctk.CTkButton(master=frame_menu, text="Maquinas",command=lambda:control('maquinas'),image=img_maquinas, width=210, height=40,corner_radius=0, hover_color=cor8, fg_color=cor1).place(x=-10, y=350) 
#EPIs
img_epis = ctk.CTkImage(light_image=Image.open("./Imagens/epis.png"),dark_image=Image.open("./Imagens/epis.png"),size=(30, 30))
botao_epis = ctk.CTkButton(master=frame_menu, text="EPIs",command=lambda:control('epis'), image=img_epis, width=210, height=40,corner_radius=0, hover_color=cor8, fg_color=cor1).place(x=-10, y=400) 




#def abrir_modal():
#	nova_janela = ctk.CTkToplevel(janela)
#	nova_janela = geometry("200x200")

#botao = ctk.CTkButton(master=frame_botoes_inserir, text="abrir janela",command=abrir_modal, width=150, height=30).place(x=0, y=0) 


dashboard()
janela.mainloop()