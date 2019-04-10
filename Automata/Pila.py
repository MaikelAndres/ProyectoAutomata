class Pila:
    def __init__(self):
        self.pila= []
        self.pila.append('#')

    def apilar(self, x):
        self.pila.append(x)

    def quitar(self):
        if(self.vacia()):
            print('la pila esta vacia')
        else:
            return self.pila.pop()

    def tope(self):
        return self.pila[len(self.pila)-1]

    def vacia(self):
        if (self.pila == []):
            return True
        else:
            return False
