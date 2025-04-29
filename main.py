from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1, "nome_produto": "Coleira", "descricao_produto": "Coleira para cachorro de pequeno porte", "preco_produto": 23.90, "foto_produto": "", "quantidade_estoque": 26},
    {"id": 2, "nome_produto": "Ração para cães adultos", "descricao_produto": "Ração premium para cães adultos de médio porte", "preco_produto": 119.90, "foto_produto": "", "quantidade_estoque": 40},
    {"id": 3, "nome_produto": "Areia para gatos", "descricao_produto": "Areia higiênica com controle de odor para gatos", "preco_produto": 35.00, "foto_produto": "", "quantidade_estoque": 60},
    {"id": 4, "nome_produto": "Brinquedo de borracha", "descricao_produto": "Brinquedo mordedor em formato de osso", "preco_produto": 15.00, "foto_produto": "", "quantidade_estoque": 75},
    {"id": 5, "nome_produto": "Comedouro duplo", "descricao_produto": "Comedouro e bebedouro acoplado para cães e gatos", "preco_produto": 29.90, "foto_produto": "", "quantidade_estoque": 30},
    {"id": 6, "nome_produto": "Tapete higiênico", "descricao_produto": "Tapete absorvente para cães", "preco_produto": 39.90, "foto_produto": "", "quantidade_estoque": 45},
    {"id": 7, "nome_produto": "Shampoo para cães", "descricao_produto": "Shampoo neutro para cães com pele sensível", "preco_produto": 22.50, "foto_produto": "", "quantidade_estoque": 50},
    {"id": 8, "nome_produto": "Antipulgas", "descricao_produto": "Medicamento antipulgas em comprimido para cães", "preco_produto": 89.00, "foto_produto": "", "quantidade_estoque": 20},
    {"id": 9, "nome_produto": "Caixa de transporte", "descricao_produto": "Caixa de transporte tamanho médio", "preco_produto": 150.00, "foto_produto": "", "quantidade_estoque": 12},
    {"id": 10, "nome_produto": "Osso de couro", "descricao_produto": "Osso natural para mastigação", "preco_produto": 9.90, "foto_produto": "", "quantidade_estoque": 80},
    {"id": 11, "nome_produto": "Cama para cachorro", "descricao_produto": "Cama acolchoada tamanho G", "preco_produto": 120.00, "foto_produto": "", "quantidade_estoque": 18},
    {"id": 12, "nome_produto": "Ração para gatos filhotes", "descricao_produto": "Ração específica para crescimento saudável", "preco_produto": 92.00, "foto_produto": "", "quantidade_estoque": 34},
    {"id": 13, "nome_produto": "Bebedouro automático", "descricao_produto": "Fonte com filtro para cães e gatos", "preco_produto": 99.90, "foto_produto": "", "quantidade_estoque": 22},
    {"id": 14, "nome_produto": "Escova de pelos", "descricao_produto": "Escova com cerdas macias para remoção de pelos mortos", "preco_produto": 18.90, "foto_produto": "", "quantidade_estoque": 55},
    {"id": 15, "nome_produto": "Brinquedo de pelúcia", "descricao_produto": "Brinquedo com apito para cães", "preco_produto": 25.00, "foto_produto": "", "quantidade_estoque": 48},
    {"id": 16, "nome_produto": "Coleira peitoral", "descricao_produto": "Coleira tipo peitoral para cães médios", "preco_produto": 35.00, "foto_produto": "", "quantidade_estoque": 27},
    {"id": 17, "nome_produto": "Ração para roedores", "descricao_produto": "Alimento completo para hamster e porquinho da índia", "preco_produto": 19.90, "foto_produto": "", "quantidade_estoque": 38},
    {"id": 18, "nome_produto": "Areia sílica para gatos", "descricao_produto": "Areia higiênica de sílica com alta absorção", "preco_produto": 42.00, "foto_produto": "", "quantidade_estoque": 32},
    {"id": 19, "nome_produto": "Pente para pulgas", "descricao_produto": "Pente de aço para remoção de pulgas e ovos", "preco_produto": 14.90, "foto_produto": "", "quantidade_estoque": 44},
    {"id": 20, "nome_produto": "Bolinha de tênis", "descricao_produto": "Brinquedo resistente para cães", "preco_produto": 12.00, "foto_produto": "", "quantidade_estoque": 70},
    {"id": 21, "nome_produto": "Ração para cães filhotes", "descricao_produto": "Ração específica para cães em fase de crescimento", "preco_produto": 110.00, "foto_produto": "", "quantidade_estoque": 37},
    {"id": 22, "nome_produto": "Coleira com plaquinha", "descricao_produto": "Coleira com plaquinha de identificação gravável", "preco_produto": 28.50, "foto_produto": "", "quantidade_estoque": 29},
    {"id": 23, "nome_produto": "Petisco dental", "descricao_produto": "Snack para limpeza dos dentes", "preco_produto": 20.00, "foto_produto": "", "quantidade_estoque": 65},
    {"id": 24, "nome_produto": "Toca para gatos", "descricao_produto": "Toca de tecido para gatos dormirem confortavelmente", "preco_produto": 95.00, "foto_produto": "", "quantidade_estoque": 16},
    {"id": 25, "nome_produto": "Roupinha para cachorro", "descricao_produto": "Roupa de frio tamanho P", "preco_produto": 45.00, "foto_produto": "", "quantidade_estoque": 35},
    {"id": 26, "nome_produto": "Limpador de patas", "descricao_produto": "Copo com cerdas para lavar as patas dos cães", "preco_produto": 30.00, "foto_produto": "", "quantidade_estoque": 28},
    {"id": 27, "nome_produto": "Tesoura para unhas", "descricao_produto": "Tesoura especial para cortar unhas de pets", "preco_produto": 17.90, "foto_produto": "", "quantidade_estoque": 50},
    {"id": 28, "nome_produto": "Coleira refletiva", "descricao_produto": "Coleira com fita refletiva para segurança noturna", "preco_produto": 32.00, "foto_produto": "", "quantidade_estoque": 23},
    {"id": 29, "nome_produto": "Ração úmida para gatos", "descricao_produto": "Sachê com pedaços de carne em molho", "preco_produto": 4.90, "foto_produto": "", "quantidade_estoque": 100},
    {"id": 30, "nome_produto": "Desinfetante pet", "descricao_produto": "Desinfetante seguro para uso em ambientes com animais", "preco_produto": 24.90, "foto_produto": "", "quantidade_estoque": 40},
    {"id": 31, "nome_produto": "Shampoo para gatos", "descricao_produto": "Shampoo seco para higiene de gatos", "preco_produto": 27.00, "foto_produto": "", "quantidade_estoque": 33},
    {"id": 32, "nome_produto": "Arranhador pequeno", "descricao_produto": "Arranhador de papelão reciclável", "preco_produto": 59.00, "foto_produto": "", "quantidade_estoque": 21},
    {"id": 33, "nome_produto": "Escova dental", "descricao_produto": "Escova dupla para higiene bucal de cães e gatos", "preco_produto": 13.50, "foto_produto": "", "quantidade_estoque": 46},
    {"id": 34, "nome_produto": "Mordedor com corda", "descricao_produto": "Brinquedo resistente com corda para puxar", "preco_produto": 19.00, "foto_produto": "", "quantidade_estoque": 36},
    {"id": 35, "nome_produto": "Porta petiscos", "descricao_produto": "Brinquedo dispenser de petiscos", "preco_produto": 49.90, "foto_produto": "", "quantidade_estoque": 27},
    {"id": 36, "nome_produto": "Fonte para gatos", "descricao_produto": "Fonte elétrica com filtro para gatos beberem mais água", "preco_produto": 135.00, "foto_produto": "", "quantidade_estoque": 14},
    {"id": 37, "nome_produto": "Casinha plástica", "descricao_produto": "Casinha para cães pequenos", "preco_produto": 180.00, "foto_produto": "", "quantidade_estoque": 10},
    {"id": 38, "nome_produto": "Spray educador", "descricao_produto": "Spray para evitar xixi fora do lugar", "preco_produto": 34.90, "foto_produto": "", "quantidade_estoque": 24},
    {"id": 39, "nome_produto": "Tapete gelado", "descricao_produto": "Tapete refrescante para dias quentes", "preco_produto": 79.90, "foto_produto": "", "quantidade_estoque": 19},
    {"id": 40, "nome_produto": "Luva removedora de pelos", "descricao_produto": "Luva que remove pelos soltos durante o carinho", "preco_produto": 21.90, "foto_produto": "", "quantidade_estoque": 42},
    {"id": 41, "nome_produto": "Bolsa para transporte", "descricao_produto": "Bolsa acolchoada para gatos e cães de pequeno porte", "preco_produto": 99.00, "foto_produto": "", "quantidade_estoque": 13},
    {"id": 42, "nome_produto": "Cinto de segurança", "descricao_produto": "Cinto que prende o pet no carro com segurança", "preco_produto": 36.00, "foto_produto": "", "quantidade_estoque": 25},
    {"id": 43, "nome_produto": "Colônia pet", "descricao_produto": "Colônia com fragrância suave para pets", "preco_produto": 26.00, "foto_produto": "", "quantidade_estoque": 30},
    {"id": 44, "nome_produto": "Cortador elétrico de pelos", "descricao_produto": "Máquina para tosa caseira de cães e gatos", "preco_produto": 199.00, "foto_produto": "", "quantidade_estoque": 9},
    {"id": 45, "nome_produto": "Brinquedo interativo", "descricao_produto": "Jogo de inteligência para cães e gatos", "preco_produto": 89.00, "foto_produto": "", "quantidade_estoque": 18},
    {"id": 46, "nome_produto": "Guia retrátil", "descricao_produto": "Guia extensível para passeios", "preco_produto": 59.90, "foto_produto": "", "quantidade_estoque": 31},
    {"id": 47, "nome_produto": "Ração para peixe beta", "descricao_produto": "Ração específica para peixes ornamentais", "preco_produto": 8.90, "foto_produto": "", "quantidade_estoque": 50},
    {"id": 48, "nome_produto": "Termômetro aquático", "descricao_produto": "Termômetro para controle da temperatura em aquários", "preco_produto": 12.00, "foto_produto": "", "quantidade_estoque": 20},
    {"id": 49, "nome_produto": "Filtro para aquário", "descricao_produto": "Filtro de carvão ativado para aquários", "preco_produto": 45.00, "foto_produto": "", "quantidade_estoque": 15},
    {"id": 50, "nome_produto": "Luz UV para aquário", "descricao_produto": "Iluminação UV para aquários", "preco_produto": 59.00, "foto_produto": "", "quantidade_estoque": 8}
]

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    preco_asc = request.args.get('preco_asc')
    preco_desc = request.args.get('preco_desc')
    descricao_parcial = request.args.get('descricao_parcial')

    produtos_filtrados = produtos

    if preco_asc == 'true':
        produtos_filtrados = sorted(produtos_filtrados, key=lambda x: x['preco_produto'])

    if preco_desc == 'true':
        produtos_filtrados = sorted(produtos_filtrados, key=lambda x: x['preco_produto'], reverse=True)

    if descricao_parcial:
        produtos_filtrados = [p for p in produtos_filtrados if descricao_parcial.lower() in p['descricao_produto'].lower()]

    return jsonify(produtos_filtrados)

@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto_por_id(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if produto:
        return jsonify(produto)
    else:
        return jsonify({"mensagem": "Produto não encontrado"}), 404

@app.route('/produtos/baratos', methods=['GET'])
def listar_produtos_baratos():
    produtos_baratos = [p for p in produtos if p['preco_produto'] < 50]
    return jsonify(produtos_baratos)

if __name__ == '__main__':
    app.run(debug=True)
