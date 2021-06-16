import pdb
from quemado import Quemado

def main():
    print(f"Bienvenidos al juego")
    vidas = input('Ingrese el número de vidas: ')
    quemado = Quemado(int(vidas))
    while True:
        dibujar = quemado.dibujar()
        letra = input('Ingrese una letra ').upper()
        res = quemado.jugar(letra)
    
main()