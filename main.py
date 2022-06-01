import mysql.connector

conexao = mysql.connector.connect( #criando conexão com o banco mysql
    host='localhost',
    user='root',
    password='1234',
    database='bdyoutube',
)
def menu():
    print("1 - Cadastrar")
    print("2 - Atualizar")
    print("3 - Exibir")
    print("4 - Apagar")
    print("5 - Sair")
menu()
op = int(input("Escolha a opção desejada: "))
while op > 5:
    print("Opção inválida!")
    menu()
    op = int(input("Digite uma opção correta: "))

#executar os comandos da conexão

if op == 1:
    # Create
    cursor = conexao.cursor()
    nome_produto=input("Digite o nome do produto: ")
    valor = float(input("Digite o valor: "))
    cursor = conexao.cursor()#executar os comandos da conexão
    comando =f'INSERT INTO vendas (nome_produto,valor) VALUES("{nome_produto}",{valor}) ' #instrução do que vai acontecer no BD
    cursor.execute(comando) #executar o meu comando
    conexao.commit()#editar o BD'''
elif op == 2:
    # Update
    cursor = conexao.cursor()
    nome_produto = input("Qual produto que deseja atualizar? ")
    valor = float(input("Digite o novo valor:" ))
    comando = F'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)  # executar o meu comando
    conexao.commit()
elif op == 3:
    # Read
    cursor = conexao.cursor()
    nome_produto = input("Qual produto deseja consultar? ")
    comando = F'SELECT nome_produto, valor FROM vendas WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)  # executar o meu comando
    resultado = cursor.fetchall()  # lendo o BD
    print("Nome:",resultado[0][0],"Valor: R$ ",resultado[0][1])
elif op == 4:
    # Deletar
    cursor = conexao.cursor()
    nome_produto = input("Qual produto deseja apagar? ")
    comando = f'DELETE FROM vendas where nome_produto ="{nome_produto}"'
    cursor.execute(comando) #executar o meu comando
    conexao.commit()
else:
    exit()

cursor.close() #fecha o cursor
conexao.close() #fecha a conexão


#Create
'''nome_produto="cafe"
valor = 5
cursor = conexao.cursor()#executar os comandos da conexão
comando =f'INSERT INTO vendas (nome_produto,valor) VALUES("{nome_produto}",{valor}) ' #instrução do que vai acontecer no BD
cursor.execute(comando) #executar o meu comando
conexao.commit()#editar o BD'''

#Read
'''
comando = F'SELECT * FROM vendas'
cursor.execute(comando) #executar o meu comando

resultado = cursor.fetchall()#lendo o BD
print(resultado)'''

#Update
'''
nome_produto = "cafe"
valor= 10
comando = F'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando) #executar o meu comando
conexao.commit()
'''
#Delete
'''
cursor = conexao.cursor()#executar os comandos da conexão
nome_produto ="0"
comando = f'DELETE FROM vendas where nome_produto ="{nome_produto}"'
cursor.execute(comando) #executar o meu comando
conexao.commit()'''


