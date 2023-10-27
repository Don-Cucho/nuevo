from flask import Flask, request, render_template
from backend_gastos import GestorDeGastosPersonales

app = Flask(__name__, static_url_path='/static')
usuario = GestorDeGastosPersonales()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        opcion = request.form['opcion']
        if opcion == '1':
            return render_template('agregar_gastos.html', lista=usuario.gastos)
        elif opcion == '2':
            return visualizar_gastos()
        elif opcion == '3':
            if len(usuario.gastos) > 0:
                return render_template('resumen_gastos_mensuales.html')
            return render_template('no_gastos.html')
        elif opcion == '4':
            if len(usuario.gastos) > 0:
                return render_template('eliminar_gastos.html', lista=usuario.gastos, lista_len=len(usuario.gastos))
            return render_template('no_gastos.html')
    return render_template('gestor_de_gastos.html')


@app.route('/documentacion')
def documentacion():
    return render_template('documentacion.html')


@app.route('/agregar_gastos', methods=['POST'])
def agregar_gastos():
    categoria = request.form['categoria']
    fecha = request.form['fecha']
    gastos_input = request.form['gastos']
    try:
        gastos = float(gastos_input)
        if gastos != round(gastos, 2):
            error = "El valor de gastos no es un número válido."
            return render_template('agregar_gastos.html', text=error, lista=usuario.gastos)
    except ValueError:
        # Manejo de error si no se pudo convertir a un entero
        error = "El valor de gastos no es un número válido."
        return render_template('agregar_gastos.html', text=error, lista=usuario.gastos)

    output = usuario.agregar_gastos(gastos, fecha, categoria)
    return render_template('agregar_gastos.html', text=f'Gasto agregado con éxito', lista=output)


@app.route('/eliminar_gastos', methods=['POST'])
def eliminar_gastos():
    index_gasto = int(request.form['gasto_a_eliminar'])

    if 0 <= index_gasto < len(usuario.gastos):
        usuario.gastos.pop(index_gasto)
        return render_template('eliminar_gastos.html', text=f'Gasto eliminado correctamente',
                               lista=usuario.gastos, lista_len=len(usuario.gastos))
    else:
        return render_template('eliminar_gastos.html', text='El gasto seleccionado no es válido', lista=usuario.gastos)


@app.route('/visualizar_gastos', methods=['POST'])
def visualizar_gastos():
    categorias = usuario.visualizar_gastos()

    if len(categorias) > 0:
        labels = list(categorias.keys())
        datos = list(categorias.values())
        return render_template('visualizar_gastos.html', labels=labels, datos=datos, categorias=categorias)
    return render_template('no_gastos.html')

@app.route('/resumen_gastos_mensuales', methods=['POST'])
def resumen_gastos_mensuales():
    meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE',
             'NOVIEMBRE', 'DICIEMBRE']
    fecha = request.form['mes']
    mes = fecha.split('-')
    mes = int(mes[1])
    mes = meses[mes - 1]
    resume = usuario.visualizar_resumen_mensual(fecha)
    if len(resume) > 0:
        categorias = list(resume.keys())
        gastos = list(resume.values())
        total = sum(gastos)
        return render_template('grafico.html', categorias=categorias, gastos=gastos, total=total, mes=mes)
    return render_template('no_gastos_mensuales.html')


if __name__ == '__main__':
    app.run()
