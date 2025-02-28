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

SenhaEntry = ttk.Entry(RightFrame,width=30,show="*") #Cria um campo de entrada para a senha
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
    EmailLabel.place(x=5,y=40) #Posiciona o label no frame direito
    EmailEntry = ttk.Entry(RightFrame,width=30) #Cria um campo de entrada para o email
    EmailEntry.place(x=120,y=55) #Posiciona o campo de entrada

    #FUNÇÃO PARA REGISTRAR NO BANCO DE DADOS
    def RegistrarNoBanco():
        nome= NomeEntry.get() #Obtem o valor do campo de entrada do nome
        email = EmailEntry.get() #Obtem o valor do campo de entrada do email
        usuario= UsuarioEntry.get() #Obtem o valor do campo de entrada do usuario
        senha = SenhaEntry.get() #Obtem o valor do campo de entrada da senha

        #Verifica se todos os campos estão preenchidos
        if nome == "" or email =="" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro de Registro", message="PREENCHA TODOS OS CAMPOS") #Exibe a mensagem de erro
        else:
            db = Database() #Cria uma instancia da classe Database
            db.RegistrarNoBanco(nome,email,usuario,senha) #Chama o metodo para registrar no banco de dados 
            messagebox.showinfo("Sucesso","Usuario registrado com sucesso!") #Exibe a mensagem de sucesso

            #Limpar os nomes após o registro
            NomeEntry.delete(0,END) #Limpa o campo de entrada do nome
            EmailEntry.delete(0,END) #Limpa o campo de entrada do email
            UsuarioEntry.delete(0,END) #Limpa o campo de entrada do usuario
            SenhaEntry.delete(0,END) #Limpa o campo de entrada da senha

    Register = ttk.Button(RightFrame,text="REGISTRAR",width=15,command=RegistrarNoBanco) #Cria um botão de registro
    Register.place(x=150,y=225) #Posiciona o botão de registro

#FUNÇÃO PARA VOLTAR A TELA DE LOGIN
    def VoltarLogin():
        #REMOVENDO WIDGETS DE CADASTRO
        NomeLabel.place(x=5000) #Move o label do nome para fora da tela
        NomeEntry.place(x=5000) #Move o campo entrada do nome para fora da tela
        EmailLabel.place(x=5000) #Move o label do email para fora da tela
        EmailEntry.place(x=5000) #Move o campo entrada do email para fora da tela
        Register.place(x=5000) #Move o botão de registro para fora da tela
        Voltar.place(x=5000) #Move o botão de voltar para fora da tela

    #TRAZENDO DE VOLTA OS WIDGETS
        LoginButton.place(x=150) #Traz o botão de login de volta para a tela
        RegisterButton.place(x=150) #Traz o botão de registrar de volta para a tela
    Voltar = ttk.Button(RightFrame,text="VOLTAR",width=15,command=VoltarLogin) #Cria um botão de voltar
    Voltar.place(x=150,y=255) #Posiciona o botão de voltar
RegisterButton= ttk.Button(RightFrame,text="REGISTRAR",width=15,command=Registrar) #Cria um botão de registro
RegisterButton.place(x=150,y=255) #Posiciona o botão de registro

#INICIAR O LOOP PRINCIPAL
jan.mainloop() #Inicia o loop principal da aplicação