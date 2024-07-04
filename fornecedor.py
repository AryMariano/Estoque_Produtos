class Fornecedor:
    def __init__(self, nome, contato):
        self._nome = nome
        self._contato = contato

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_contato(self):
        return self._contato

    def set_contato(self, contato):
        self._contato = contato

    def salvar(self, db):
        query = "INSERT INTO fornecedores (nome, contato) VALUES (%s, %s)"
        params = (self._nome, self._contato)
        db.execute_query(query, params)

    @staticmethod
    def listar_todos(db):
        query = "SELECT * FROM fornecedores"
        resultados = db.fetch_query(query)
        return resultados
