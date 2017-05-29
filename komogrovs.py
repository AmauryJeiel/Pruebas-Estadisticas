import random
import openpyxl as excel

class Kolmogrovs():
    n=0
    h0=None
    h1=None

    numerosRandom=[]
    ordenNumeros=[]
    probabilidades=[]
    tuplaRestaPRi=[]
    restaPri=[]

    maximo=0

    def __init__(self,numerosR,h0,h1,n):
        self.numerosRandom=numerosR
        self.h0=h0
        self.h1=h1
        self.n=n

    def ordenOyRi(self):
        for i in range(len(self.numerosRandom)):
            self.ordenNumeros.append(int(1))

        self.numerosRandom.sort()
        dato1=0
        dato2=None
        incremento =0
        contador=0
        tamano=len(self.ordenNumeros)-1
        for i in range(tamano):
            dato1=float(self.numerosRandom[incremento])
            dato2 =self.numerosRandom[incremento+1]

            if dato1 == dato2:
                contador +=1
                self.numerosRandom.remove(dato1)
                self.ordenNumeros.pop(contador)
                self.ordenNumeros[contador-1] +=1
                incremento +=0
                contador -=1
            else:
                contador +=1
                incremento +=1

        print self.ordenNumeros
        print self.numerosRandom

    def definirProbabildiad(self):
        r = 0
        for i in range(len(self.numerosRandom)):
            r = random.uniform(0.1, 1.01)
            r= '%.3f'%r
            self.probabilidades.append(float(r))
        self.probabilidades.sort()

        print self.probabilidades

    def tuplaDiferenciaPRi(self):
        datoR=0
        datoP=0
        tupla=None
        for i in range(len(self.numerosRandom)):
            datoR=self.numerosRandom[i]
            datoP=self.probabilidades[i]
            tupla =(datoP,datoR)
            self.tuplaRestaPRi.append(tupla)

        print self.tuplaRestaPRi

    def diferenciaPRi(self):
        dato1=0
        dato2=0

        diferencia=0
        for i in range(len(self.tuplaRestaPRi)):
            dato1=self.tuplaRestaPRi[i][0]
            dato2=self.tuplaRestaPRi[i][1]

            diferencia =abs(float((dato1-dato2)))
            self.restaPri.append(diferencia)

        print self.restaPri
        self.maximo=max(self.restaPri)
        print self.maximo

class TransExcel():

    def launchExcel(self,n,orden,aleatorios,propabilidad,tostadas,maximos):
        libro=excel.load_workbook('TablaRegistros.xlsx')
        hojaT=libro['Hoja1']
        n2=n+2
        rangoOrden=hojaT['B3:B%d'%n2]

        incrementoDato=0
        cel=3

        for fila in rangoOrden:
            for celda in fila:
                hojaT['B%d'%cel] =orden[incrementoDato]
                incrementoDato +=1
                cel +=1

        rangoOrden = hojaT['C3:C%d' % n2]
        incrementoDato=0
        cel=3

        for fila in rangoOrden:
            for celda in fila:
                hojaT['C%d'%cel] =aleatorios[incrementoDato]
                incrementoDato +=1
                cel +=1

        rangoOrden = hojaT['D3:D%d' % n2]
        incrementoDato = 0
        cel = 3

        for fila in rangoOrden:
            for celda in fila:
                hojaT['D%d' % cel] = propabilidad[incrementoDato]
                incrementoDato += 1
                cel += 1


        rangoOrden = hojaT['E3:E%d' % n2]
        incrementoDato = 0
        cel = 3

        for fila in rangoOrden:
            for celda in fila:
                dat1=float(tostadas[incrementoDato][0])
                dat2=float(tostadas[incrementoDato][1])

                hojaT['E%d' % cel] = '%f - %f'% (dat1,dat2)
                incrementoDato += 1
                cel += 1


        rangoOrden = hojaT['F3:F%d' % n2]

        incrementoDato = 0
        cel = 3

        for fila in rangoOrden:
            for celda in fila:
                hojaT['F%d' % cel] = maximos[incrementoDato]
                incrementoDato += 1
                cel += 1

        libro.save('TablaRegistros.xlsx')

if __name__ == '__main__':
    print '''
               Bienvenido. 
           Prueba de Komogrov-s.
       '''
    n = int(raw_input('Total de numeros aleatorios que quieres para tu prueba:\n-->'))
    numerosR = []
    rand=0
    for i in range(n):
        rand=random.random()*1
        rand = '%.5f' %rand
        numerosR.append(float(rand))

    h0 = str(raw_input('Plantea a H0:\n-->'))
    h1 = str(raw_input('Plantea a H0:\n-->'))

    numerosR.sort()
    prueba1=Kolmogrovs(numerosR,h0,h1,n)
    prueba1.ordenOyRi()
    prueba1.definirProbabildiad()
    prueba1.tuplaDiferenciaPRi()
    prueba1.diferenciaPRi()

    exc=TransExcel()
    exc.launchExcel(n,prueba1.ordenNumeros,prueba1.numerosRandom,prueba1.probabilidades,prueba1.tuplaRestaPRi,prueba1.restaPri)



