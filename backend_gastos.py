class GestorDeGastosPersonales:
    def __init__(self):
        # Lista donde se almaceraran todos los datos agregados y el cual funcionara para todas las funciones
        self.gastos = [
                    # {'gasto': 50.0, 'fecha': '2023-10-13', 'categoria': 'Educación'},
                    # {'gasto': 52.0, 'fecha': '2023-10-06', 'categoria': 'Otros'},
                    # {'gasto': 50.0, 'fecha': '2023-10-13', 'categoria': 'Educación'},
                    # {'gasto': 52.0, 'fecha': '2023-10-06', 'categoria': 'Otros'},
                    # {'gasto': 50.0, 'fecha': '2023-10-13', 'categoria': 'Educación'},
                    # {'gasto': 52.0, 'fecha': '2023-10-06', 'categoria': 'Otros'},
                    # {'gasto': 50.0, 'fecha': '2023-10-13', 'categoria': 'Educación'},
                    # {'gasto': 52.0, 'fecha': '2023-10-06', 'categoria': 'Otros'},
                    # {'gasto': 50.0, 'fecha': '2023-10-13', 'categoria': 'Educación'},
                    # {'gasto': 52.0, 'fecha': '2023-10-06', 'categoria': 'Otros'}
                       ]
    #Creamos el método que servirá para agregar los gastos en una lista de diccionarios
    def agregar_gastos(self, gastos, fecha, categoria):
        self.gastos.append({"gasto": gastos, "fecha": fecha, "categoria": categoria})
        #Devuelve que se agregaron los datos a la lista
        return self.gastos

    #Este método obtiene todos los datos de la lista  self.datos y los organiza por categorías en un diccionario
    def visualizar_gastos(self):
        #Verifica si la lista de gastos contiene elementos
        if len(self.gastos) > 0:
            sumaCategorias = {}
            for categorias in self.gastos:
                # Obtiene la categoria y la cantidad de cada gasto
                categoria = categorias['categoria']
                cantidad = categorias['gasto']
                #Si la cagegoria no existe en el diccionario, suma la cantidad
                if categoria in sumaCategorias:
                    sumaCategorias[categoria] += cantidad
                else:
                    #Si la categoria no existe en el diccionario, la agrega
                    sumaCategorias[categoria] = cantidad
            #Devuelve el diccionario con todos sus valores
            return sumaCategorias
        else:
            #Devuelve un diccionario vacio para validar y presentrar el html
            return {}

    def visualizar_resumen_mensual(self, mes):
        VerificarGastos = False
        if len(self.gastos) > 0:
            mes_anio = mes
            resumen_mensual = {'Alimentación': 0,
                               'Transporte': 0,
                               'Entretenimiento': 0,
                               'Salud': 0,
                               'Educación': 0,
                               'Otros': 0}
            for gasto in self.gastos:
                fecha_gasto = gasto['fecha']
                if fecha_gasto.startswith(mes_anio):
                    VerificarGastos=True
                    categoria = gasto['categoria']
                    cantidad = gasto['gasto']
                    if categoria in resumen_mensual:
                        resumen_mensual[categoria] += cantidad
            if VerificarGastos:
                return resumen_mensual
            else:
                return {}
        else:
            return {}