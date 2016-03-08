#!/usr/bin/env python
import logging

#Klasa odpowiedzialna za sprawdzenie poprawnosci wprowadzonych danych
class InputValidator(object):
    #Metoda sprawdzajaca poprawnosc wprowadzonych danych
    @staticmethod
    def validate(matrix):
        logger = logging.getLogger('myApp.inputValidator.validate')
        logger.info('Sprawdzam poprawnosc parametrow')
        if len(matrix.eqParams) != 2:
            logger.error('Wystapil blad podczas sprawdzania danych:')
            raise Exception('Nieprawidlowa liczba rownan!')
        if len(matrix.eqParams[0]) != len(matrix.eqParams[1]):
            logger.error('Wystapil blad podczas sprawdzania danych:')
            raise Exception('Nieprawidlowa liczba parametrow!')
        try:
            for row in matrix.eqParams:
                for i in row:
                    float(i)
        except ValueError:
            logger.error('Wystapil blad poczas sprawdzania danych:')
            raise
        logger.info('Sprawdzanie parametrow zakonczono sukcesem.')
        matrix.conv_params()
        matrix.det_w()
        if matrix.W == 0.0:
            logger.error('Wystapil blad podczas sprawdzania danych:')
            raise Exception('Uklad nie jest ukladem oznaczonym!')
        logger.info('Walidacja przebiegla pomyslnie')
