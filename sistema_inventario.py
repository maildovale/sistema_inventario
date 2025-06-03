class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser un número positivo.")
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad: int):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser un número positivo o cero.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Total: ${self.calcular_valor_total():.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre: str) -> Producto:
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        raise LookupError("Producto no encontrado.")

    def calcular_valor_inventario(self) -> float:
        return sum(p.calcular_valor_total() for p in self.productos)

    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu_principal(inventario: Inventario):
    while True:
        print("\nMenú de Inventario")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ").strip()
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad disponible: "))
                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("Producto agregado correctamente.")
            elif opcion == "2":
                nombre = input("Nombre del producto a buscar: ").strip()
                producto = inventario.buscar_producto(nombre)
                print(producto)
            elif opcion == "3":
                inventario.listar_productos()
            elif opcion == "4":
                total = inventario.calcular_valor_inventario()
                print(f"Valor total del inventario: ${total:.2f}")
            elif opcion == "5":
                break
            else:
                print("Opción no válida.")
        except ValueError as ve:
            print(f"Error de entrada: {ve}")
        except LookupError as le:
            print(le)
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)