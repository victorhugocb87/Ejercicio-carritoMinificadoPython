class Productos:
    def __init__(self):
        self.codigo = []
        self.nombre = []
        self.precio_compra = []
        self.precio_venta = []
        self.fecha_fabricacion = []
        self.fecha_vencimiento = []
        self.proveedor = []
        self.estado = []

    def menu(self):
        opciones = """
        **********"MENU PRINCIPAL"**********
        
        1.- AGREGAR PRODUCTO
        2.- MOSTRAR DESCRIPCION
        3.- ACTUALIZAR PRECIO DE VENTA 
        4.- TIEMPO DE VIGENCIA DE PRODUCTO
        5.- TIEMPO DE VALIDEZ DE PRODUCTO
        6.- ELIMINAR PRODUCTO
        7.- DAR DE ALTA PRODUCTO
        8.- DAR DE BAJA PRODUCTO
        9.- MOSTRAR INVENTARIO DE BAJA 
        10.- SALIR
        """
        print(opciones)
        seleccionar = int(input("Seleccione una opcion: \n"))
        if (seleccionar == 1):
            print(self.agregarProducto())
            self.menu()
        elif (seleccionar == 2):
            print(self.verInventarioAlta())
            print(self.volverMenu())
        elif (seleccionar == 3):
            print(self.editarPrecioVenta())
            print(self.volverMenu())
        elif (seleccionar == 4):
            pass
            self.menu()
        elif (seleccionar == 5):
            pass
            self.menu()
        elif (seleccionar == 6):
            print(self.realizarEliminacion())
            print(self.volverMenu())
        elif (seleccionar == 7):
            print(self.realizarAlta())
            print(self.volverMenu())
        elif (seleccionar == 8):
            print(self.realizarBaja())
            print(self.volverMenu())
        elif (seleccionar == 9):
            print(self.verInventarioBaja())
            print(self.volverMenu())
        elif (seleccionar == 10):
            print("Transacciones realizadas exitosamente")
        else:
            print("Seleccione una opcion del menu")
            self.menu()
    def volverMenu(self):
        eleccion = input("Desea volver al menu: y/n \n")
        if (eleccion == 'y' or eleccion == 'Y'):
            self.menu()
        return "---------Transacciones terminadas----------"

    def agregarProducto(self):
        codigo = input("Codigo de producto: \n")
        nombre = input("Nombre de producto: \n")
        precio_compra = int(input("Precio de compra: \n"))
        fecha_fabricacion = input("Fecha de fabricacion: \n")
        fecha_vencimiento = input("Fecha de vencimiento: \n")
        proveedor = input("Nombre de proveedor: \n")
        self.guardarProducto(codigo, nombre, precio_compra, fecha_fabricacion, fecha_vencimiento, proveedor)
        agregarOtro = input("Desea agregar otro producto? y/n \n")
        if (agregarOtro == 'y' or agregarOtro == 'Y'):
            self.agregarProducto()
        return "Productos agregados correctamente"

    def guardarProducto(self, codigo, nombre, precioCompra, fechaFabricacion, fechaVencimiento, proveedor):
        self.codigo.append(codigo)
        self.nombre.append(nombre)
        self.precio_compra.append(precioCompra)
        self.precio_venta.append((precioCompra * 0.4) + precioCompra)
        self.fecha_fabricacion.append(fechaFabricacion)
        self.fecha_vencimiento.append(fechaVencimiento)
        self.proveedor.append(proveedor)
        self.estado.append(1)
        return "Producto {} agregado correctamente".format(nombre)
    def verInventarioAlta(self):
        return self.inventario(1)

    def verInventarioBaja(self):
        return self.inventario(0)

    def inventario(self, estado):
        if (self.nombre):
            for i in range(len(self.nombre)):
                self.descripcion(i, estado)
            return "Inventario cargado Correctamente"
        else:
            return "TODAVIA NO SE AGREGARON PRODUCTOS A LA BASE DE DATOS"

    def descripcion(self, posicion, estado):
        if (self.estado[posicion] == estado):
            print("***************DESCRIPCION DE PRODUCTO {}*****************".format(self.nombre[posicion]))
            print("CODIGO DE PRODUCTO: {}".format(self.codigo[posicion]))
            print("PRECIO DE COMPRA: {} Bs.".format(self.precio_compra[posicion]))
            print("PRECIO DE VENTA: {} Bs.".format(self.precio_venta[posicion]))
            print("FECHA DE FABRICACION: {}".format(self.fecha_fabricacion[posicion]))
            print("FECHA DE VENCIMIENTO: {}".format(self.fecha_vencimiento[posicion]))
            print("PROVEEDOR: {}".format(self.proveedor[posicion]))
            print("*********************************************")
            pass
    def editarPrecioVenta(self):
        print("******************ACTUALIZAR PRECIO DE VENTA**********************")
        posicion = self.buscarProducto(1)
        self.descripcion(posicion)
        nuevo_precio = int(input("Digite el nuevo preciode venta del producto {}: \n".format(self.nombre[posicion])))
        print(self.modificarPrecioVenta(posicion, nuevo_precio))
        self.descripcion(posicion)
        return "Modificacion de precio de venta completado"

    def modificarPrecioVenta(self, posicion, pvn):
        self.precio_venta[posicion] = pvn
        return "Precio de Venta del Producto {} Modificado Correctamente".format(self.nombre[posicion])
    def realizarEliminacion(self):
        print("******************SELECCIONAR EL PRODUCTO A ELIMINAR*********************")
        posicion = self.buscarProducto(1)
        return self.eliminar(posicion)

    def buscarProducto(self, estado):
        print(self.inventario(estado))
        eleccion = input("Digite el codigo del Producto: \n")
        posicion = self.codigo.index(eleccion)
        return posicion

    def eliminar(self, posicion):
        cod = self.codigo[posicion]
        self.codigo.pop(posicion)
        self.nombre.pop(posicion)
        self.precio_compra.pop(posicion)
        self.precio_venta.pop(posicion)
        self.fecha_fabricacion.pop(posicion)
        self.fecha_vencimiento.pop(posicion)
        self.proveedor.pop(posicion)
        self.estado.pop(posicion)
        return "Eliminacion Realizada del producto {}".format(cod)

    def realizarAlta(self):
        print("**************DAR DE ALTA UN PRODUCTO*************")
        posicion = self.buscarProducto(0)
        return self.darAlta(posicion)

    def darAlta(self, posicion):
        self.estado[posicion] = 1
        return "El producto {} esta de Alta..!!".format(self.nombre[posicion])

    def realizarBaja(self):
        print("**************DAR DE BAJA UN PRODUCTO*************")
        posicion = self.buscarProducto(1)
        return self.darBaja(posicion)

    def darBaja(self, posicion):
        self.estado[posicion] = 0
        return "El producto {} esta de Baja..!!".format(self.nombre[posicion])
productos = Productos()
productos.guardarProducto('A101', 'CAFE 240 GR', 7, '03-03-2020', '05-06-2021', 'IDEAL S.A.')
productos.guardarProducto('A102', 'LECHE PIL 1LT', 5, '03-07-2020', '05-09-2021', 'PIL ANDINA S.A.')
productos.guardarProducto('A103', 'CAFE COROICO 290GR', 8, '03-05-2020', '05-02-2021', 'COROICO S.A.')
productos.menu()
