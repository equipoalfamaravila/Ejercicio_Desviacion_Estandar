import statistics
import unittest
import os

class Estadisticas:

    def __init__(self):
        self.numeros = self.obtener_numeros()

    def obtener_numeros(self):
        numeros = []
        while True:
            try:
                cantidad = int(input("Introduce la cantidad de números que deseas ingresar: "))
                if cantidad <= 0:
                    print("Por favor, introduce un número entero positivo.")
                    continue
                break
            except ValueError:
                print("Por favor, introduce un número entero válido.")
        
        for _ in range(cantidad):
            while True:
                try:
                    numero = float(input("Introduce un número: "))
                    numeros.append(numero)
                    break
                except ValueError:
                    print("Por favor, introduce un número válido.")
        return numeros

    def calcularMedia(self):

        if not self.numeros:
            return 0.0
        media = statistics.mean(self.numeros)
        return media 

    def calcularDesviacion_estandar(self):

        if len(self.numeros) < 2:
            return 0.0
        desviacion = statistics.pstdev(self.numeros)
        return desviacion
    
    def mostrarDatos(self): 
        cMedia=self.calcularMedia()
        cDesviacion=self.calcularDesviacion_estandar()
        os.system("cls")
        print("----------RESULTADOS----------")
        print("")
        print("Los datos ingresados son : ",self.numeros)
        print("La media es:               ",cMedia)
        print("La desviacion estandar es: ",cDesviacion)
        print("")

calcular = Estadisticas()
calcular.mostrarDatos()

class TestEstadisticas(unittest.TestCase):
    
    def test_media(self):

        lista=calcular.numeros
        esperado = statistics.mean(lista)
        actual = calcular.calcularMedia()
        self.assertAlmostEqual(esperado, actual)
    
    def test_desviacion_estandar(self):

        lista = calcular.numeros
        esperado = statistics.pstdev(lista)
        actual = calcular.calcularDesviacion_estandar()
        self.assertAlmostEqual(esperado, actual)

if __name__ == '__main__':
    unittest.main()