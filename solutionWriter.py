#!/usr/bin/env python
import os
import stat
import logging

#Klasa odpowiedzialna za zapisywanie i przedstawienie graficzne naszego rozwiazania
class SolutionWriter(object):
    #Metoda zapisujaca nasze rownanie oraz jego rozwiazanie do pliku solution.dat, wykorzystuje skrypt plot.sh do rysowania wykresu
    @staticmethod
    def save_and_plot(matrix):
        file_name = 'solution.dat'
        logger = logging.getLogger('myApp.solutionWriter.save_and_plot')
        logger.info('Zapisuje rozwiazanie do pliku ' + file_name )
        with open(file_name, 'w') as file:
            file.write(matrix.get_equations() + '\n')
            file.write(str(matrix.solution))

        logger.info('Przygotowanie odpowiedniej postaci rownania do rysowania')
        eq_list = []
        for row in matrix.eqParams:
            eq = str(row[0]) + '*x/' + str((-1)*row[1])
            val = row[2]/row[1]
            if val >= 0.:
                eq += '+' + str(val)
            else:
                eq += str(val)
            eq_list.append(eq)

        logger.info('Tworze graficzne rozwiazanie problemu.')
        os.chmod('plot.sh', stat.S_IRWXU)
        os.system('./plot.sh %s %s %s %s' % (eq_list[0], eq_list[1], str(matrix.solution[0]), str(matrix.solution[1])))
        print('Rozwiazanie zostalo zapisane w pliku ' + file_name + ' oraz ' + 'solution.png')
        return
