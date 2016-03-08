#!/usr/bin/env python
from applicationMgr import *
from inputReader import *
from inputValidator import *
from solutionWriter import *
from solver import *
from matrix import *
import logging


# Glowny program do wykonania
def main():
    app = ApplicationMgr(InputReader(), InputValidator(), SolutionWriter(), Matrix(), Solver())
    try:
        app.read_linear_equations()
        app.validate_linear_equations()
        app.print_linear_equations()
        app.solve_linear_equations()
        app.print_solution()
        app.save_and_plot_linear_equations()
    except Exception as e:
        logger.error(e)
        print('Wystapil blad, sprawdz plik myApp.log')


# Inicjalizacja loggera i uruchomienie naszego programu
if __name__ == '__main__':
    logger = logging.getLogger('myApp')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('myApp.log', mode='w')
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info('Rozpoczecie dzialania programu!')
    main()
    logger.info('Koncze dzialanie programu!')
