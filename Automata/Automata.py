import Pila

class Automatapila:
    def __init__(self,palabra):
        self.pila = Pila.Pila()
        self.resultado=[]
        self.transiciones=[]
        self.p_1 = True
        self.q_2 = False
        self.r_final = False
        self.palabra=palabra

    def getP_1(self):
        return self.p_1
    def getQ_2(self):
        return self.q_2
    def getR_final(self):
        return self.r_final

    def activaP_1(self):
        self.p_1=True
        self.q_2=False
        self.r_final=False

    def activaQ_2(self):
        self.q_2=True
        self.p_1=False
        self.r_final=False

    def activaR_final(self):
        self.r_final=True
        self.p_1=False
        self.q_2=False

    #transiciones con b
    def b_b_bb(self):
        self.pila.quitar()
        self.pila.apilar('b')
        self.pila.apilar('b')
        self.activaP_1()

    def b_a_ab(self):
        self.pila.quitar()
        self.pila.apilar('a')
        self.pila.apilar('b')
        self.activaP_1()
    def b_n_nb(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.pila.apilar('b')
        self.activaP_1()
        
    #transiciones con a
    def a_b_ba(self):
        self.pila.quitar()
        self.pila.apilar('b')
        self.pila.apilar('a')
        self.activaP_1()
    def a_n_na(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.pila.apilar('a')
        self.activaP_1()
    def a_a_aa(self):
        self.pila.quitar()
        self.pila.apilar('a')
        self.pila.apilar('a')
        self.activaP_1()
        
    #transiciones con c
    def c_n_n(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.activaQ_2()
    def c_b_b(self):
        self.pila.quitar()
        self.pila.apilar('b')
        self.activaQ_2()
    def c_a_a(self):
        self.pila.quitar()
        self.pila.apilar('a')
        self.activaQ_2()

    def b_b_y(self):
        self.pila.quitar()
        self.activaQ_2()

    def a_a_y(self):
        self.pila.quitar()
        self.activaQ_2()

    def y_n_n(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.activaR_final()

    def validar(self):
        palabra=self.palabra+'  '
        print(palabra)
      

        for caracter in palabra:
            paso = "{:6} |  {:6}  |  {:6} |   {:4} | {:4} ".format(str(self.getP_1()), str(self.getQ_2()),
                                                                                                               str(self.getR_final()),str(caracter),str(self.pila.tope()))
            self.resultado.append(paso)

            if (caracter != 'a' and caracter != 'b' and caracter != 'c'  and caracter != ' '):
                invali='El caracter es invalido!!!'
                self.resultado.append(invali)
                break
            elif (self.getP_1()):
                if (caracter=='b'):
                    if (self.pila.tope()== 'b'):
                        self.b_b_bb()
                        trans='|b/b/bb|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope()== 'a'):
                        self.b_a_ab()
                        trans='|b/a/ab|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope() == '#'):
                        self.b_n_nb()
                        trans='|b/#/#b|'
                        self.transiciones.append('      '+trans)
                elif (caracter ==  'a'):
                    if (self.pila.tope()== 'b'):
                        self.a_b_ba()
                        trans='|a/b/ba|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope()== 'a'):
                        self.a_a_aa()
                        trans='|a/a/aa|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope() == '#'):
                        self.a_n_na()
                        trans='|a/#/#a|'
                        self.transiciones.append('      '+trans)
                elif (caracter == 'c'):
                    if (self.pila.tope()== 'b'):
                        self.c_b_b()
                        trans='|c/b/b|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope()== 'a'):
                        self.c_a_a()
                        trans='|c/a/a|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope() == '#'):
                        self.c_n_n()
                        trans='|c/#/#|'
                        self.transiciones.append('      '+trans)
            elif (self.getQ_2()):
                if (caracter == 'b'):
                    if (self.pila.tope() == 'b'):
                        self.b_b_y()
                        trans='|b/b/y|'
                        self.transiciones.append('      '+trans)
                    else:
                        break
                elif (caracter == 'a'):
                    if (self.pila.tope() == 'a'):
                        self.a_a_y()
                        trans='|a/a/y|'
                        self.transiciones.append('      '+trans)
                    else:
                        break
                elif(caracter == ' '):
                    print('palabra terminada')
                    if (self.pila.tope() == '#' and self.getQ_2()):
                        self.y_n_n()
                        trans='|y/#/#|'
                        self.transiciones.append('      '+trans)


        nega='*No es palondrime*'
        if (self.getR_final()):
            acept='*Es palindrome*'
            self.resultado.append(acept)
        elif(self.getP_1()):
            error='*Deben llevar por lo  menos una C *'
            self.resultado.append(error)
            self.resultado.append(nega)
        else:
            self.resultado.append(nega)

auto=Automatapila("abbcbba")
auto.validar()
print(auto.transiciones)
print(auto.resultado)
