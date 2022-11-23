import random
from link import Link
from neuro import Neuro

class Network:
    def __init__(self, *args):
        self.__nlayers = len(args)          #число слоев
        self.__neuros = args                #число нейронов в кажом слое
        self.__layers = []


        #создаю нейроны в каждом слое
        for i in range(self.__nlayers):
            self.__layers.append( [Neuro([],[]) for n in range(self.__neuros[i])] )

        #создаю связи между нейронами
        for i in range( self.__nlayers ):
            for neuro in self.__layers[i]: #Перебераем нейроны i-го слоя
                list_in = 0 if i == 0 else [ Link(n_in, neuro, random.random()) for n_in in self.__layers[i-1] ]
                list_out = 0 if i == self.__nlayers-1 else [Link(neuro, n_out, random.random()) for n_out in self.__layers[i+1]]
                neuro.list_in = list_in
                neuro.list_out = list_out



    def run(self, v):
        #подаем на вход нейронной сети сигнал v
        for neuro, inp in zip(self.__layers[0], v):
            neuro.value = neuro.list_in = inp


        #проводим сигнал по нейронной сети
        for i in range(1, self.__nlayers):
            for neuro in self.__layers[i]: #перебераем нейроны i-го слоя
                v = [(link.n_in.value*link.w) for link in neuro.list_in]
                neuro.value = neuro.act( sum(v) )

    def output(self):
        return [ neuro.value for neuro in self.__layers[-1] ]
