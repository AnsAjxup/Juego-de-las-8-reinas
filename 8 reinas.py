print("Juego de las 8 reinas")
class nreinas:

    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.results = 0
        self.resuelve()

    def resuelve(self):
        posicion = [-1] * self.tamaño
        self.poner_reina(posicion, 0)
        print("se encontraron", self.results, "soluciones")

    def poner_reina(self, posicion, fila_objetivo):
        if fila_objetivo == self.tamaño:
            self.muestra_todo_tablero(posicion)
            self.results += 1
        else:
            for columna in range(self.tamaño):
                #cancela las posiciones invalidas
                if self.check_place(posicion, fila_objetivo, columna):
                    posicion[fila_objetivo] = columna
                    self.poner_reina(posicion, fila_objetivo + 1)

    def check_place(self, posicion, fila_ocupada, columna):
        for i in range(fila_ocupada):
            if posicion[i] == columna or \
                posicion[i] - i == columna - fila_ocupada or \
                posicion[i] + i == columna + fila_ocupada:

                return False
        return True

    def muestra_todo_tablero(self, posicion):
        for row in range(self.tamaño):
            line = ""
            for columna in range(self.tamaño):
                if posicion[row] == columna:
                    line += "R "
                else:
                    line += ". "
            print(line)
        print("\n")

def main():
    nreinas(4) #nuemero de reinas

if __name__ == "__main__":
    main()