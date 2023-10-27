class GestorDeGastosPersonales:
    def __init__(self):
        self.gastos = []
        self.diccionarioGastos=[]
        self.categorias = ["Alimentación", "Transporte", "Entretenimiento", "Salud", "educacion", "cucho"]
        print('---------------Bienvenido a su gestor de gastos---------------')

    def operaciones(self):

        self.opcion = int(input('''
        ---------------------------------------
        1. agregar gastos
        2. Agregar categorias de gastos
        3. visualizar gastos por categorias
        4. gatos mensuales
        5. SAlIR
        ingrese digito: '''))
        self.control=0
        while self.control==0:
            if self.opcion==1:
                self.AgregarGastos()
            elif self.opcion==2:
                self.CategoriasDeGastos()
            elif self.opcion==3:
                self.VisualizarDECategorias()
            elif self.opcion ==4:
                self.GatosMensualesResumen()
            elif self.opcion==5:
                self.Salir()
                self.control=1
            else:
                print('Opcion invalida intente de nuevo')
                self.operaciones()

    def AgregarGastos(self):
        cantidad=float(input('ingrese cantidad de gasto: '))
        fecha= input('ingrese la fecha del gasto (YYYY-MM-DD): ')
        categoria= input('ingrese categoria del gasto: ').lower()
        if categoria not in self.categorias:
            print(f'La categoría {categoria} no es válida. Las categorías válidas son: {", ".join(self.categorias)}')
            self.operaciones()
        else:
            self.gastos.append({"cantidad": cantidad, "fecha": fecha, "categoria": categoria})
            print("Gasto agregado con éxito!")
            self.operaciones()
    def CategoriasDeGastos(self):
        agregar = input('ingrese categoria:').lower()
        if agregar not in self.categorias:
            self.categorias.append(agregar)
            print(self.categorias)
            self.operaciones()
        else:
            print(f'La categoría {agregar} ya se encuentra disponible')
            self.operaciones()

    def VisualizarDECategorias(self):
        sumaCategorias = {}
        for categorias in self.gastos:
            categoria = categorias['categoria']
            cantidad = categorias['cantidad']
            if categoria in sumaCategorias:
                sumaCategorias[categoria] += cantidad
            else:
                sumaCategorias[categoria] = cantidad

        for categoria, cantidad in sumaCategorias.items():
            print(f'{categoria}: ${cantidad}')

        self.operaciones()

    def GatosMensualesResumen(self):
        pass

    def Salir(self):
        pass

# usuario=GestorDeGastosPersonales()
# usuario.operaciones()