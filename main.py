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

    def modifica_prezzo(self, nuovo_prezzo):
        self.prezzo = nuovo_prezzo
    
    def modifica_proprietario(self, nuovo_proprietario):
        self.proprietario = nuovo_proprietario


immobile_1 = Immobile('giulio', 'grosseto', 'via santissima 12', 90, 1990, 100000)
immobile_2 = Immobile('carlo', 'siena', 'via dei fgsrta 12', 120, 1923, 500000)


your_choice= 0
while your_choice != 6:
    menu()
    your_choice=int(input('Seleziona un comando: '))
    print('------------------------------')
    if your_choice==1: # SELEZIONE

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

    elif your_choice==2: # INSERIMENTO
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
            
        else: # NON FUNZIONA: INSERIMENTO ERRONEO
            inserisci(Popolare, proprietario, citta, indirizzo, mq, costruzione, prezzo)
    
    elif your_choice==4: # MODIFICA
        
        print('Immobile 1:')
        for key, value in immobile_1.__dict__.items():
            print(key, ':', value)

        print('\nImmobile 2:')
        for key, value in immobile_2.__dict__.items():
            print(key, ':', value)

        scelta = int(input('\nQuale immobile vuoi modificare? '))
        if scelta == 1:

            nuovo_prezzo = int(input('\nQuale è il nuovo prezzo? '))
            immobile_1.modifica_prezzo(nuovo_prezzo)
            print('Prezzo modificato: \n', immobile_1.__dict__)

        elif scelta == 2:
            nuovo_prezzo = int(input('\nQuale è il nuovo prezzo? '))
            immobile_2.modifica_prezzo(nuovo_prezzo)
            print('Prezzo modificato: \n', immobile_2.__dict__['prezzo'])
            