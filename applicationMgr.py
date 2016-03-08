#!/usr/bin/env python


#Klasa menager zarzadzajaca naszymi operacjami
class ApplicationMgr(object):
    #Konstruktor inicjalizujacy skladowe naszej klasy
    def __init__(self, input_reader, input_validator, solution_writer, matrix, solver):
    	#Zmienna przechowujaca obiekt odpowiedzialny za wczytywanie pliku
        self.input_reader = input_reader
        #Zmienna przechowujaca obiekt odpowiedzialny za sprawdzanie poprawnosci danych
        self.input_validator = input_validator
        #Zmienna przechowujaca obiekt odpowiedzialny za rozwiazanie naszego ukladu rownan
        self.solver = solver
        #Zmienna przechowujaca obiekt odpowiedzialny za zapisywanie naszego rozwiazania
        self.solution_writer = solution_writer
        #Zmienna przechowujaca obiekt zawierajacy informacje o naszym ukladzie rownan
        self.matrix = matrix
    #Wywoluje metode odpowiedzialna za odczytanie z pliku naszych parametrow rownania
    def read_linear_equations(self):
        self.input_reader.read_from_file(self.matrix)
    #Wywoluje metode odpowiedzialna za sprawdzanie poprawnosci wczytywanych danych
    def validate_linear_equations(self):
        self.input_validator.validate(self.matrix)
    #Wywoluje metode odpowiedzialna za rozwiazanie naszego rownania
    def solve_linear_equations(self):
        self.solver.solve(self.matrix)
    #Wypisuje nam poprawnie wczytane rownanie
    def print_linear_equations(self):
        print('Wczytano rownanie:\n' + self.matrix.get_equations())
    #Wypisuje roziwazanie rownania
    def print_solution(self):
        print('Rozwiazanie ukladu to para (x,y): ' + str(self.matrix.solution))
    #Wywoluje metode odpowiedzialna za zapisanie naszego rozwiazania oraz przedstawienie go w formie graficznej
    def save_and_plot_linear_equations(self):
        self.solution_writer.save_and_plot(self.matrix)

