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
        self.points = 0 #i funksjonen som skal telle alle poengene må jeg huske på å sette self.points = 0

    def add_brikke(self, rad, kolonne, brikke:Brikke):
        if type(brikke) != Brikke:
            raise TypeError('Kan kun legge in Objekter av typen Brikke på brettet')

        if self.brett_liste[rad][kolonne] == None:
            self.brett_liste[rad][kolonne] = brikke
        else:
            #jeg bør nok lage en annen error en dette, slik at den kan fortsette å prøve å legge på plass
            raise IndexError('Det ligger en brikke på rad {}, kolonne {} fra før'.format(rad,kolonne))

    
    #lager en funksjone for å telle poeng diagonal_1
    def count_diagonal_1(self):
        count = 0
        diag_sum = 0
        for del_list in self.brett_liste:
            if type(del_list[0]) == Brikke:
                første_verdi_diag = del_list[0].diagonal_1
            else: første_verdi_diag = -1 #Hvis det ikke ligger en brikke der bruker jeg denne logikken 
            
            for brikke in del_list:
                if type(brikke) == Brikke:
                    count = brikke.diagonal_1
                else: count = 0

                #sjekker om verdiene i raden er lik. Disse vil også være ulike hvis det ikke er noen brikke der    
                if count == første_verdi_diag: 
                    diag_sum += count
                else:
                    diag_sum = 0
                    break

            self.points += diag_sum #Oppdaterer poengene

    #lager en funksjon for å telle poeng loddrett
    def count_loddrett(self):
        #lager en ny liste slik at jeg kan bruke samme logikk som for diagonal_1
        L = self.brett_liste
        loddrett_list = [ [  L[0][0],L[1][0], L[2][0]  ], 
                          [  L[0][1], L[1][1], L[2][1], L[3][0]  ],
                          [  L[0][2], L[1][2], L[2][2], L[3][1], L[4][0]  ],
                          [  L[1][3], L[2][3], L[3][2], L[4][1]  ],
                          [  L[2][4],L[3][3], L[4][2]  ]  ]
        #print(loddrett_list)

        count = 0
        diag_sum = 0
        for del_list in loddrett_list:
            if type(del_list[0]) == Brikke:
                første_verdi_diag = del_list[0].loddrett
            else: første_verdi_diag = -1 #Hvis det ikke ligger en brikke der bruker jeg denne logikken 
            
            for brikke in del_list:
                if type(brikke) == Brikke:
                    count = brikke.loddrett
                else: count = 0

                #sjekker om verdiene i raden er lik. Disse vil også være ulike hvis det ikke er noen brikke der    
                if count == første_verdi_diag: 
                    diag_sum += count
                else:
                    diag_sum = 0
                    break

            self.points += diag_sum #Oppdaterer poengene



def main():
    brikke1 = Brikke(9,2,8)
    brikke2 = Brikke(9,2,3)
    brikke3 = Brikke(5,2,4)

    brett = Brett()
    brett.add_brikke(0,0,brikke1)
    brett.add_brikke(0,1,brikke2)
    brett.add_brikke(1,0,brikke2)
    brett.add_brikke(0,2,brikke2)
    brett.add_brikke(2,0,brikke3)

    #print(brett.brett_liste)
    brett.count_diagonal_1()
    brett.count_loddrett()
    print(brett.points)

if __name__ == '__main__':
	main()