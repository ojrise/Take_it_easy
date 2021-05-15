import numpy as np

class Brikke:
    ''' Klassen som representerer en brikke med verdier på loddrett akse og de to diagonalene'''
    def __init__(self, loddrett, diagonal_1, diagonal_2) -> None:
        #Sørger for at kun gyldige tall blir sendt inn
        if loddrett == 5 or loddrett == 1 or loddrett == 9:
            self.loddrett = loddrett
        else:
            raise ValueError('loddrett kan kun ta inn tallene 1, 5 eller 9. Du ga inn {}'.format(loddrett))

        if diagonal_1 == 6 or diagonal_1 == 7 or diagonal_1 == 2:
            self.diagonal_1 = diagonal_1
        else:
            raise ValueError('diagonal_1 kan kun ta inn tallene 2, 6 eller 7. Du ga inn {}'.format(diagonal_1))


        if diagonal_2 == 3 or diagonal_2 == 4 or diagonal_2 == 8:
            self.diagonal_2 = diagonal_2
        else:
            raise ValueError('diagonal_2 kan kun ta inn tallene 3, 4 eller 8. Du ga inn {}'.format(diagonal_2))


class Brett:
    '''Denne klassen representerer spillbrettet med en liste av lister der hvert element er en mulig plassering på brettet
       Første element i listen er brikken øverst til venstre også går den oppover skrått mot venstre'''
    def __init__(self) -> None:
        self.brett_liste = [ [None]*3, [None]*4, [None]*5, [None]*4, [None]*3 ]

    def add_brikke(self, rad, kolonne, brikke:Brikke):
        if type(brikke) != Brikke:
            raise TypeError('Kan kun legge in Objekter av typen Brikke på brettet')

        if self.brett_liste[rad][kolonne] == None:
            self.brett_liste[rad][kolonne] = brikke
        else:
            #jeg bør nok lage en annen error en dette, slik at den kan fortsette å prøve å legge på plass
            raise IndexError('Det ligger en brikke på rad {}, kolonne {} fra før'.format(rad,kolonne))


def main():
    brikke1 = Brikke(1,6,8)

    brikke2 = Brikke(9,2,3)

    brett = Brett()
    brett.add_brikke(1,2,brikke2)
    brett.add_brikke(2,2,brikke1)

    print(brett.brett_liste[1][2].loddrett)

if __name__ == '__main__':
	main()