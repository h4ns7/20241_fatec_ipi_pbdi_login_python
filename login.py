import psycopg
print(psycopg)
class Usuario:
  def __init__(self, login, senha):
    self.login = login
    self.senha = senha

#verifica se o usuário recebido existe na base
def existe(usuario):
  #abrir uma conexão com o PostgreSQL
  #obter uma abstração do tipo "cursor"
  #executar um comando sql
  #verificar o resultado
  #devolver True ou False
  with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="20241_fatec_ipi_pbdi_login_python",
    user="postgres",
    password="123456"
  ) as conexao:
    with conexao.cursor() as cursor:
      cursor.execute(
        'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
        (usuario.login, usuario.senha)
      )
      result = cursor.fetchone()
      #return #se result for igual a None, devolvo False, senão devolvo True
      #return True if result != None else False
      return result != None
    
#def teste():
# print(existe(Usuario('admin', 'admin')))
#
#teste()
    
def adicionar_usuario(usuario):
  with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="20241_fatec_ipi_pbdi_login_python",
    user="postgres",
    password="123456"
  ) as conexao:
    with conexao.cursor() as cursor:
      cursor.execute('INSERT INTO tb_usuario (login, senha) VALUES (%s, %s)',
                     (usuario.login, usuario.senha))
      conexao.commit()
      print("usuario adicionado com sucesso")



def menu ():
  texto = ' 0-Sair\n 1-Login\n 2-Logoff\n 3-Novo usuário\n'
  #usuario ainda não existe
  usuario = None
  op = int(input(texto))
  while op != 0:
      if op ==1:
        login = input("Digite o login")
        senha = input("Digite a senha")
        usuario = Usuario(login, senha)
        #expressão condicional (if/else de uma linha só)
        print('Usuário OK!' if existe(usuario) else 'Usuário NOK')
        pass
      elif op == 2:
        usuario = None
        print("Logoff realizado com sucesso")
      elif op ==3:
        login =input("Digite o novo login:")
        senha = input("Digite a nova senha")
        novo_usuario = Usuario (login, senha)
        adicionar_usuario(novo_usuario)
      else: 
        print('Digite apenas numeros entre 0 e 3')
      op = int(input(texto))


menu()
