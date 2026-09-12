from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    numero1 = float(request.form['numero1'])
    numero2 = float(request.form['numero2'])
    operacao = request.form['operacao']

    if operacao == 'soma':
        resultado = numero1 + numero2

    elif operacao == 'subtração':
        resultado = numero1 - numero2

    elif operacao == 'multiplicação':
        resultado = numero1 * numero2

    elif operacao == 'divisão':
        if numero2 == 0:
            resultado = 'Não é possível dividir por zero.'
        else:
            resultado = numero1 / numero2

    return render_template(
        'resultado.html',
        resultado=resultado
    )

if __name__ == '__main__':
    app.run(debug=True)