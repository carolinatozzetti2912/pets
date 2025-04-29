def filtrar_por_nome(produtos, nome):
    nome = nome.lower()
    return [produto for produto in produtos if nome in produto['nome_produto'].lower()]

def filtrar_por_descricao(produtos, descricao):
    descricao = descricao.lower()
    return [produto for produto in produtos if descricao in produto['descricao_produto'].lower()]
