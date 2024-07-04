class Produto:
    def __init__(self, nome, fornecedor_id, quantidade):
        self._nome = nome
        self._fornecedor_id = fornecedor_id
        self._quantidade = quantidade

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_fornecedor_id(self):
        return self._fornecedor_id

    def set_fornecedor_id(self, fornecedor_id):
        self._fornecedor_id = fornecedor_id

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade

    def salvar(self, db):
        query = "INSERT INTO produtos (nome, fornecedor_id, quantidade) VALUES (%s, %s, %s)"
        params = (self._nome, self._fornecedor_id, self._quantidade)
        db.execute_query(query, params)

    @staticmethod
    def listar_todos(db):
        query = "SELECT * FROM produtos"
        resultados = db.fetch_query(query)
        return resultados
