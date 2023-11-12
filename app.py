from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

menu_items = [
    {
        "id": 1,
        "name": "Cupcake de Morango",
        "price": 8.99
    },
    {
        "id": 2,
        "name": "Cupcake de Chocolate",
        "price": 8.99
    },
    {
        "id": 3,
        "name": "Cupcake de Baunilha",
        "price": 7.99
    },
    {
        "id": 4,
        "name": "Cupcake de Caramelo",
        "price": 7.99
    },
    {
        "id": 5,
        "name": "Cupcake de Doce de Leite",
        "price": 7.99
    }
]

orders = []


# Rota para a página inicial
@app.route('/menu', methods=['GET'])
def index():
    return render_template('site/index.html')


# Rota para a página de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        full_name = request.form.get('full-name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        birth_date = request.form.get('birth-date')
        cpf = request.form.get('cpf')
        address = request.form.get('address')
        number = request.form.get('number')
        neighborhood = request.form.get('neighborhood')
        complement = request.form.get('complement')
        city = request.form.get('city')
        state = request.form.get('state')
        cep = request.form.get('cep')
        cellphone = request.form.get('cellphone')

        # Process the data here, e.g., store it in the database

        return redirect(url_for('registration_success'))

    return render_template('cadastro.html')


# Rota para a página de sucesso de registro
@app.route('/registration-success')
def registration_success():
    return "Registro bem-sucedido!"


# Rota para adicionar um novo cliente
@app.route('/adicionar_cliente', methods=['POST'])
def adicionar_cliente():
    data = request.get_json()
    conn = sqlite3.connect('cupcake_delivery.db')
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO clientes (nome_completo, data_nascimento, cpf, endereco, numero, bairro, complemento, cidade, estado, cep, celular) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (data['nome_completo'], data['data_nascimento'], data['cpf'], data['endereco'], data['numero'],
         data['bairro'], data['complemento'], data['cidade'], data['estado'], data['cep'], data['celular']))

    conn.commit()
    conn.close()
    return jsonify({"message": "Cliente adicionado com sucesso!"}), 201


# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "admin":
            return redirect(url_for('pagamento'))
        else:
            return "Credenciais inválidas. Tente novamente."

    return render_template('login.html')


# Rota para a página de pagamento
@app.route('/pagamento', methods=['GET', 'POST'])
def pagamento():
    if request.method == 'POST':
        selected_payment_option = request.form.get('payment-option')

        if selected_payment_option == "money":
            return "Pedido finalizado! Pagamento na entrega."
        elif selected_payment_option == "credit-card":
            card_number = request.form.get('card-number')
            card_holder = request.form.get('card-holder')
            expiration_date = request.form.get('expiration-date')
            cvv = request.form.get('cvv')

            if card_number and card_holder and expiration_date and cvv:
                order_id = len(orders) + 1
                orders.append(
                    {'order_id': order_id, 'payment_method': 'Cartão de Crédito'})
                return f"Pedido #{order_id} finalizado com sucesso! Método de pagamento: Cartão de Crédito"
            else:
                return "Erro no processamento de pagamento com cartão de crédito. Verifique os detalhes do cartão."

        elif selected_payment_option == "pix":
            return "Processamento de pagamento via PIX"

    return render_template('pagamento.html')


# Rota para a página de pedido concluído
@app.route('/pedido-concluido')
def pedido_concluido():
    return render_template('pedido-concluido.html')


# Rota para a página de finalização do pedido
@app.route('/finalizar-pedido')
def finalizar_pedido():
    return render_template('finalizacao.html')


# Rota para a página de recebimento do pedido
@app.route('/recebimento-pedido')
def recebimento_pedido():
    return "O pedido foi recebido com sucesso. Aguarde a entrega."


if __name__ == '__main__':
    app.run(debug=True)
