class MovimentacaoEstoque:
    def __init__(self, produto_id, tipo_movimentacao, quantidade):
        self._produto_id = produto_id
        self._tipo_movimentacao = tipo_movimentacao
        self._quantidade = quantidade

    def get_produto_id(self):
        return self._produto_id

    def set_produto_id(self, produto_id):
        self._produto_id = produto_id

    def get_tipo_movimentacao(self):
        return self._tipo_movimentacao

    def set_tipo_movimentacao(self, tipo_movimentacao):
        self._tipo_movimentacao = tipo_movimentacao

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade

    def registrar(self, db):
        query = "INSERT INTO movimentacoes (produto_id, tipo_movimentacao, quantidade) VALUES (%s, %s, %s)"
        params = (self._produto_id, self._tipo_movimentacao, self._quantidade)
        db.execute_query(query, params)

    @staticmethod
    def listar_todas(db):
        query = "SELECT * FROM movimentacoes"
        resultados = db.fetch_query(query)
        return resultados
