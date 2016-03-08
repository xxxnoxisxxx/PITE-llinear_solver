#!/usr/bin/env python
import logging

#Klasa przechowujaca nasz uklad rownan
class Matrix(object):
    #Konstruktor podstawowy
    def __init__(self):
        #Przechowuje parametry naszego ukladu rownan
        self.eqParams = []
        #Przechowuje rozwiazanie naszego ukladu rownan
        self.solution = ()
        #Przechowuje wyznacznik macierzy naszego ukladu rownan
        self.W = 0
    #Metoda obliczajaca wyznacznik naszej macierzy
    def det_w(self):
        logger = logging.getLogger('myApp.matrix.det_w')
        logger.info('Obliczam wyznacznik macierzy')
        self.W = float(self.eqParams[0][0]*self.eqParams[1][1] - self.eqParams[1][0]*self.eqParams[0][1])
        return
    #Metoda konwertujaca wczytane parametry na float
    def conv_params(self):
        logger = logging.getLogger('myApp.matrix.conv_params')
        logger.info('Konwertuje parametry macierzy na float')
        self.eqParams = [list(map(float, row)) for row in self.eqParams]
        return
    #Metoda zwracajaca wyglad naszego ukladu rownan
    def get_equations(self):
        eq = ''
        for row in self.eqParams:
            eq = eq + str(row[0]) + '*x '
            if row[1] >= 0.:
                eq = eq + '+ ' + str(row[1]) + '*y'
            else:
                eq = eq + '- ' + str((-1.)*row[1]) + '*y'
            eq = eq + ' = ' + str(row[2]) + '\n'
        return eq
    #Nadpisanie metody str
    '''def __str__(self):
        return ''.join(str(row)+'\n' for row in self.eqParams)'''
