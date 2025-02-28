import mysql.connector #Importa o modulo mysql.connector para conectar ao banco de dados MySQL

class Database:
    def __init__(self):
        #Conecta ao banco de dados MySQL com as credenciais forncedas
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="vitorgulicz_db"
        )
        self.cursor = self.conn.cursor() #Cria um cursor para executar comandos MySQL
        #Cria uma tabela 'usuario1' se ela não existir
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuario1(
                            idUsuario INT AUTO_INCREMENT PRIMARY KEY,
                            nome TEXT(255),
                            email TEXT(255),
                            usuario TEXT(255),
                            senha TEXT(255)
        );''')
        self.conn.commit() #Confirma a criação da tabela

        print("conectado ao banco de Dados") #Imprime uma mensagem de confirmação

    #Metodo para registrar um novo usuario no banco de dados
    def RegistrarNoBanco(self,nome,email,usuario,senha):
        self.cursor.execute("INSERT INTO usuario1(nome, email, usuario, senha) VALUES(%s, %s, %s, %s)",(nome,email,usuario,senha)) #Insere os dados do usuario na tabela
        self.conn.commit() #Confirma a inserção dos dados

    #Metodo para alterar os dados de uma usuario existente no banco de dados
    def alterar(self,idUsuario,nome,email,usuario,senha):
        self.cursor.execute("UPDATE usuario1 SET nome=%s, email=%s, usuario=%s, senha=%s WHERE idUsuario=%s",
                            (nome,email,usuario,senha,idUsuario)) #Atualiza os dados do usuario com id oferecido
        self.conn.commit() #Confirma a atualização do dados 
    
    #Metodo para excluir um usuario do banco de dados 
    def excluir (self,idUsuario):
        self.cursor.execute("DELETE FROM usuario1 WHERE idUsuario=%s",(idUsuario,)) #Exclui o usuario com o id fornecido
        self.conn.commit() #Confirma a exclusão de dados

    #Metodo para buscar os dados de um usuario no banco de dados
    def buscar(self,idUsuario):
        self.cursor.execute("SELECT * FROM usuario1 WHERE idUsuario=%s",(idUsuario,)) #Seleciona os dados do usuario com o id fornecido
        return self.cursor.fetchone() #Retorna oos dados do usuario encontrado
    
    #Metodo chamado quando a instancia da classe é destruida
    def __del__(self):
        self.conn.close() #Fecha a conexão com o banco de dados