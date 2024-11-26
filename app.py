from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza el formulario sin resultados inicialmente
    return render_template('index.html', resultados={})

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form.get('nombre')
    edad = request.form.get('edad')
    provincia = request.form.get('provincia')
    distrito = request.form.get('distrito')

    # Resultados del test
    resultados = {
        'artistica': request.form.get('pregunta1', 'No respondido'),
        'investigacion': request.form.get('pregunta2', 'No respondido'),
        'realista': request.form.get('pregunta3', 'No respondido'),
        'social': request.form.get('pregunta4', 'No respondido'),
        'empresarial': request.form.get('pregunta5', 'No respondido')
    }

    print(f"Datos del formulario: {resultados}")  # Esto imprimirá los datos en la consola

    return render_template('resultados.html', 
                           nombre=nombre, 
                           edad=edad, 
                           provincia=provincia, 
                           distrito=distrito, 
                           resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
