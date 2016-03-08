#!/usr/bin/env python
import logging

#Klasa odpowiedzialna za wczytywanie parametrow z pliku
class InputReader(object):
    #Metoda wczytujaca nasze parametry rownania z pliku i zapisuje je w obiekcie matrix
    @staticmethod
    def read_from_file(matrix):
        logger = logging.getLogger("myApp.inputReader.read_from_file")
        logger.info("Rozpoczynam wczytywanie parametrow z pliku.")
        try:
            with open(input('Podaj nazwe pliku\n'), 'r') as readFile:
                for line in readFile:
                    matrix.eqParams.append(line.strip().split(','))
        except IOError:
            logger.error('Wystapil blad podczas odczytywania pliku.')
            raise
        logger.info('Odczytywanie parametrow zakonczone sukcesem.')
