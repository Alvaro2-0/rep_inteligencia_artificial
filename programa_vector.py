class Vector:
    def __init__(self, tamano):
        self.tamano = tamano
        self.datos = self.solicitar_datos()

    def solicitar_datos(self):
        datos = []
        for i in range(self.tamano):
            dato = float(input(f"Ingrese el dato {i + 1}: "))
            datos.append(dato)
        return datos

    def ordenar(self):
        return sorted(self.datos)

    def calcular_promedio(self):
        return sum(self.datos) / self.tamano

    def mostrar_vector(self, mensaje, vector):
        print(f"{mensaje}: {vector}")


class Aplicacion:
    def __init__(self):
        self.tamano = self.solicitar_tamano()
        self.vector = Vector(self.tamano)

    def solicitar_tamano(self):
        return int(input("Ingrese el tamaño del vector: "))

    def ejecutar(self):
        # Mostrar el vector original
        self.vector.mostrar_vector("Vector original", self.vector.datos)
        
        # Mostrar el vector ordenado
        vector_ordenado = self.vector.ordenar()
        self.vector.mostrar_vector("Vector ordenado", vector_ordenado)
        
        # Calcular y mostrar el promedio
        promedio = self.vector.calcular_promedio()
        print("El promedio de los valores es:", promedio)


# ¿entrada
if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()