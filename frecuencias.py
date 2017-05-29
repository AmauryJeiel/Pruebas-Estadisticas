import random
class Frecuencias():
    muestraN=None
    h0=None
    h1=None
    k=None
    n=None


    tamanoIntervalos=[]
    tuplaIntervalos = []
    eI=None
    numeroOi = []
    restaOiEi=[]
    restaOiEi2=[]

    xi2=0.0

    def __init__(self,n,h0,h1,randoms,k):
        self.h0=h0
        self.h1=h1
        self.muestraN=randoms
        self.k=k
        self.n=n

    def definirIntervalos(self):
        tupla=[]
        self.tamanoIntervalos.append(0.0)
        tamanoIntervalo= float(1/float(self.k))
        for i in range(self.k):
            dato=float(self.tamanoIntervalos[i])
            self.tamanoIntervalos.append(float(dato+tamanoIntervalo))

        numElementos=len(self.tamanoIntervalos)

        for i in range(numElementos-1):
            rango = (self.tamanoIntervalos[i],self.tamanoIntervalos[i+1])
            tupla.append(rango)

        for i in range(self.k):
            self.numeroOi.append(0)

        self.tuplaIntervalos=tupla

    def frecuenciaEsperada(self):
        tamanoN=float(len(self.muestraN))
        self.eI=float( tamanoN / float(self.k))

    def frecuenciaObservada(self):
        aleatorio=0.0
        intervalo1=0
        intervalo2=0
        incremento =0
        for i in range(len(self.muestraN)):
            aleatorio =float(self.muestraN[i])
            for j in range(len(self.tuplaIntervalos)):
                intervalo1=self.tuplaIntervalos[j][0]
                intervalo2=self.tuplaIntervalos[j][1]

                if aleatorio > intervalo1 and aleatorio < intervalo2:
                    self.numeroOi[j] +=1

    def diferenciaOiEi(self):
        resta=0
        for i in range(len(self.numeroOi)):
            resta =float(self.eI-self.numeroOi[i])
            self.restaOiEi.append(resta)

    def diferenciaOiEi2(self):
        potencia=0
        for i in range(len(self.restaOiEi)):
            potencia= float(self.restaOiEi[i]**2)
            self.restaOiEi2.append(potencia)


    def calcularX2(self):
        elemento=0
        for i in range(len(self.restaOiEi2)):
            elemento= float(self.restaOiEi2[i])
            self.xi2 += elemento

        self.xi2=float(self.xi2/self.eI)

if __name__ == '__main__':
    print '''
            Bienvenido. 
        Prueba de Frecuencias.
    '''
    n=int(raw_input('Total de numeros aleatorios que quieres:\n-->'))
    numerosR=[]
    for i in range(n):
        numerosR.append(random.random()*1)

    h0=str(raw_input('Plantea a H0:\n-->'))
    h1= str(raw_input('Plantea a H0:\n-->'))
    k=int(raw_input('Cuantos intervalos quieres para tu prueba:\n-->'))

    prueba=Frecuencias(n,h0,h1,numerosR,k)
    prueba.definirIntervalos()
    prueba.frecuenciaEsperada()
    prueba.frecuenciaObservada()
    prueba.diferenciaOiEi()
    prueba.diferenciaOiEi2()
    prueba.calcularX2()
