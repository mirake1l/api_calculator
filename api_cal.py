from flask import Flask, request, jsonify 

app = Flask(__name__)

@app.route('/add', methods=['POST']) #Сложение
def add():
    data = request.get_json()
    result = data['num1'] + data['num2']
    return jsonify({'result': result})

@app.route('/subtract', methods=['POST']) #Вычитание
def subtract():
    data = request.get_json()
    result = data['num1'] - data['num2']
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST']) #Умножение
def multiply():
    data = request.get_json()
    result = data['num1'] * data['num2']
    return jsonify({'result': result})

@app.route('/divide', methods=['POST']) #Деление
def divide():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    if num2 == 0:
        return jsonify({'error': 'Division by zero is not allowed'})
    result = num1 / num2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host ="0.0.0.0",debug=True)
