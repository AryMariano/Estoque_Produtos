from database import Database
from loja import Loja
from fornecedor import Fornecedor
from produto import Produto
from movimentacao_estoque import MovimentacaoEstoque

def cadastrar_loja(db):
    nome = input("Digite o nome da loja: ")
    endereco = input("Digite o endereço da loja: ")
    loja = Loja(nome, endereco)
    loja.salvar(db)
    print("Loja cadastrada com sucesso!")

def cadastrar_fornecedor(db):
    nome = input("Digite o nome do fornecedor: ")
    contato = input("Digite o contato do fornecedor: ")
    fornecedor = Fornecedor(nome, contato)
    fornecedor.salvar(db)
    print("Fornecedor cadastrado com sucesso!")

def cadastrar_produto(db):
    nome = input("Digite o nome do produto: ")
    fornecedor_id = int(input("Digite o ID do fornecedor: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produto = Produto(nome, fornecedor_id, quantidade)
    produto.salvar(db)
    print("Produto cadastrado com sucesso!")

def registrar_entrada_estoque(db):
    produto_id = int(input("Digite o ID do produto: "))
    quantidade = int(input("Digite a quantidade de entrada: "))
    movimentacao = MovimentacaoEstoque(produto_id, 'entrada', quantidade)
    movimentacao.registrar(db)
    print("Entrada de estoque registrada com sucesso!")

def registrar_saida_estoque(db):
    produto_id = int(input("Digite o ID do produto: "))
    quantidade = int(input("Digite a quantidade de saída: "))
    movimentacao_saida = MovimentacaoEstoque(produto_id, 'saida', quantidade)
    movimentacao_saida.registrar(db)
    print("Saída de estoque registrada com sucesso!")

def listar_todos(db):
    print("\nLojas:")
    lojas = Loja.listar_todas(db)
    for loja in lojas:
        print(loja)

    print("\nFornecedores:")
    fornecedores = Fornecedor.listar_todos(db)
    for fornecedor in fornecedores:
        print(fornecedor)

    print("\nProdutos:")
    produtos = Produto.listar_todos(db)
    for produto in produtos:
        print(produto)

    print("\nMovimentações de Estoque:")
    movimentacoes = MovimentacaoEstoque.listar_todas(db)
    for movimentacao in movimentacoes:
        print(movimentacao)

def menu():
    db = Database()
    while True:
        print("\n1. Cadastrar Loja")
        print("2. Cadastrar Fornecedor")
        print("3. Cadastrar Produto")
        print("4. Registrar Entrada de Estoque")
        print("5. Registrar Saída de Estoque")
        print("6. Listar Todos os Dados")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_loja(db)
        elif escolha == '2':
            cadastrar_fornecedor(db)
        elif escolha == '3':
            cadastrar_produto(db)
        elif escolha == '4':
            registrar_entrada_estoque(db)
        elif escolha == '5':
            registrar_saida_estoque(db)
        elif escolha == '6':
            listar_todos(db)
        elif escolha == '7':
            break
        else:
            print("Opção inválida, por favor, escolha novamente.")

if __name__ == "__main__":
    menu()
