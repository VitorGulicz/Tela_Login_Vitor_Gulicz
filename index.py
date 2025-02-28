#Importar as biblotecas
from tkinter import * #IMporta todos os modulos do tkinter
from tkinter import messagebox #importa o modulo de caixas de de mensagens do tkinter 
from tkinter import ttk #Importa a classe Database do modulo DataBase

#CRIAR A JANELA
jan=Tk() # Cria uma instancia da janela principal
jan.title("SL Sytens - Painel de Acesso") #Define o titulo da janela
jan .geometry("600x300") #Define o tamanho da janela
jan.configure(background="white") #Configura a cor de fundo da janela
jan.resizable(width=False,height=False) #Impede que a janela seja redimensionada

#COMANDO PARA DEIXAR A TELA TRANSPARENTE
jan.attributes("-alpha",0.9) #Define a transparencia da janela (0.0 a 1.0)

#DEFINIR O ICONE DA JANELA
#jan.iconbitmap(default="icons/1LogoIcon.ico") #Define o icone da janela

#CARREGAR A IMAGEM
logo = PhotoImage(file="icons/Vitor_Gulicz.png") #Carrega a imagem da logo

#CRIAR FRAME
LeftFrame = Frame(jan,width=200,height=300,bg="MIDNIGHTBLUE",relief="raise") #Cria um frame a esquerda
LeftFrame.pack(side=LEFT) #Posiciona o frame à esquerda

RightFrame = Frame(jan,width=395,height=300,bg="MIDNIGHTBLUE",relief="raise") #Cria um frame a direita
RightFrame.pack(side=RIGHT) #Posiciona o frame à direita

#ADICIONAR A LOGO
LogoLabel = Label(LeftFrame,image=logo,bg="MIDNIGHTBLUE") #Cria um label para a imagem da logo
LogoLabel.place(x=50,y=100) #Posiciona o label no frame esquerdo

#ADICIONAR CAMPOS DE USUARIO E SENHA
UsuarioLabel = Label(RightFrame,text="Usuario: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White") #Cria um label para usuario
UsuarioLabel.place(x=5,y=100) #Posiciona o label no frame direito

UsuarioEntry = ttk.Entry(RightFrame,width=30) #Cria um campo de entrada para o usuario
UsuarioEntry.place(x=120,y=115) #Posiciona o campo de entrada

SenhaLabel = Label(RightFrame,text="Senha: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White") #Cria um label para a senha
SenhaLabel.place(x=5,y=150) #Posiciona o label no frame direito

SenhaEntry = ttk.Entry(RightFrame,width=30,show="°") #Cria um campo de entrada para a senha
SenhaEntry.place(x=120,y=165) #Posiciona o campo de entrada

#FUNÇÃO DE LOGIN
def Login():
    usuario = UsuarioEntry.get() #Obtem o valor do campo de entrada do usuario
    senha = SenhaEntry.get() #Obtem o valor do campo de entrada senha

    #Conectar o banco de dado
    db= Database() #Cria uma instancia da classe Database
    db.cursor.execute("""
    SELECT * FROM usuario1
    WHERE usuario = %s AND senha = %s""",(usuario,senha)) #Executa a consulta SQL para verificar o usuario e a senha
    VerifyLogin = db.cursor.fetchone() #Obtem o resultado da consulta

    #Verificar se o usuario foi encontrado
    if VerifyLogin:
        messagebox.showinfo(title="INFO LOGIN", message="Acesso Confirmado. Bem Vindo! ") #Exibe mensagem de sucesso
    else:
        messagebox.showinfo(title="INFO LOGIN",message="Acesso Negado. Verifique se está cadastrado no Sistema! ") #Exibe a mensagem de errro 

#CRIANDO BOTÕES
LoginButton = ttk.Button(RightFrame,text="LOGIN",width=15,command=Login) #Cria um botão de login
LoginButton.place(x=150,y=225) #Posiciona o botão de login

#FUNÇÃO PARA REGISTRAR NOVO USUARIO
def Registrar():
    #REMOVENDO BOTÕES DE LOGIN
    LoginButton.place(x=5000) # Move o botão de login para fora da tela
    RegisterButton.place(x=5000) #Move o botão de registro para fora da tela

    #INSERINDO WIDGETS DE CADASTRO
    NomeLabel = Label(RightFrame,text="Usuario: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White") #Cria um label para o nome
    NomeLabel.place(x=5,y=5) #Posiciona o label no frame direito
    NomeEntry = ttk.Entry(RightFrame,width=30) #Cria um campo de entrada para o nome
    NomeEntry.place(x=120,y=20) #Posiciona o campo de entrada

    EmailLabel = Label(RightFrame,text="Usuario: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White") #Cria um label para o email
    EmailLabelLabel.place(x=5,y=5) #Posiciona o label no frame direito