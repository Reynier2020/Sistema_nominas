from biblioteca import *
from libro import *

biblioteca = Biblioteca("motivos de son", "Maria Moreno", "12-6")
libro1 = Libro("ABC", "REY", "ciencia ficcion", 2023, False, True)
libro2 = Libro("Cuerda de acero", "Richard", "aventura", 2020, True, False)
libro3 = Libro("Sombras del pasado", "Richard", "aventura", 2021, True, False)
libro4 = Libro("Nicola Tesla", "REY", "ciencia ficcion", 2021, True, False)
libro5 = Libro("La cantina", "REY", "ciencia ficcion", 2023, False, True)

biblioteca.insertar_libro(libro1)
biblioteca.insertar_libro(libro2)
biblioteca.insertar_libro(libro3)
biblioteca.insertar_libro(libro4)
biblioteca.insertar_libro(libro5)

cantidad_libros = len(biblioteca.libros_digitales) + len(biblioteca.libros_digitales)
# print(cantidad_libros)
print(biblioteca.genero_dig_abundante())
svswvser