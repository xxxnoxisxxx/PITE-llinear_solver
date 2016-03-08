import numpy as np
import logging

#Klasa odpowiadajaca za rozwiazanie naszego rownania
class Solver(object):
    #Metoda wykorzystujaca biblioteke numpy do rozwiazania naszego rownania
    @staticmethod
    def solve(matrix):
        logger = logging.getLogger("myApp.solver.solve")
        logger.info("Rozwiazuje rownanie.")
        a = np.array([row[:-1] for row in matrix.eqParams])
        b = np.array([row[-1] for row in matrix.eqParams])
        matrix.solution = tuple(np.linalg.solve(a, b))
        return

