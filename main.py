import peewee
from funzioni import *
from gestore_db import *



class Immobile():
    def __init__(self, proprietario, citta, indirizzo, mq, costruzione, prezzo):
        self.proprietario = proprietario
        self.citta = citta
        self.indirizzo = indirizzo
        self.mq = mq
        self.costruzione = costruzione
        self.prezzo = prezzo

    def modifica_prezzo(self):
        pass
    
    def modifica_proprietario(self):
        pass



your_choice= 0
while your_choice != 6:
    menu()
    your_choice=int(input('Seleziona un comando: '))
    print('------------------------------')
    if your_choice==1:

        scelta = int(input('Quale catalogo vuoi vedere?\n 1 - Prestigio\n 2 - CasaVacanza\n 3 - Popolare\n'))

        if scelta == 1:
            seleziona(Prestigio)
            for im in immobili:
                print('Immobile ', im)
                print('Proprietario:', im.proprietario, '\nCitta: ', im.citta, '\nIndirizzo: ', im. indirizzo, '\nPrezzo: ', im. prezzo)
                print('------------------------------')

        if scelta == 2:
            seleziona(CasaVacanza)
            for im in immobili:
                print('Immobile ', im)
                print('Proprietario:', im.proprietario, '\nCitta: ', im.citta, '\nIndirizzo: ', im. indirizzo, '\nPrezzo: ', im. prezzo)
                print('------------------------------')

        if scelta == 3:
            seleziona(Popolare)
            for im in immobili:
                print('Immobile ', im)
                print('Proprietario:', im.proprietario, '\nCitta: ', im.citta, '\nIndirizzo: ', im. indirizzo, '\nPrezzo: ', im. prezzo)
                print('------------------------------')

    elif your_choice==2:
        proprietario = input('Proprietario: ')
        citta = input('Citta: ')
        indirizzo = input('Indirizzo: ')
        mq = int(input('Metri quadrati: '))
        costruzione = int(input('Anno di costruzione: '))
        prezzo = int(input('Prezzo: '))
        if prezzo > 500000: #OK
            inserisci(Prestigio, proprietario, citta, indirizzo, mq, costruzione, prezzo)
        elif prezzo > 150000 & prezzo < 500000: # OK
            inserisci(CasaVacanza, proprietario, citta, indirizzo, mq, costruzione, prezzo)
        elif prezzo < 150000:
            inserisci(Popolare, proprietario, citta, indirizzo, mq, costruzione, prezzo)
