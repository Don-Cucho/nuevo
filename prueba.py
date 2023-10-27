# leelele = {"Alimentacion": 2000}
#
# print(leelele.keys())
# print(leelele.values())


# ... (otras importaciones y configuraciones de Flask)

@app.route('/agregar_gastos', methods=['POST'])
def agregar_gastos():
    categoria = request.form['categoria']
    fecha = request.form['fecha']
    gastos_input = request.form['gastos']
    try:
        gastos = float(gastos_input)
        if gastos != round(gastos, 2):
            error = "El valor de gastos no es un número válido."
            return render_template('agregar_gastos.html', text=error, categorias=[])
    except ValueError:
        # Manejo de error si no se pudo convertir a un entero
        error = "El valor de gastos no es un número válido."
        return render_template('agregar_gastos.html', text=error, categorias=[])

    # Aquí deberías llamar a tu función 'usuario.agregar_gastos' y obtener la lista de categorías
    # y luego pasarla a la plantilla
    categorias = obtener_categorias_desde_usuario()  # Reemplaza con tu lógica real

    return render_template('agregar_gastos.html', text='Gasto agregado con éxito', categorias=categorias)

if __name__ == '__main__':
    app.run()
