import peewee
from gestore_db import *

# OPERAZIONI CRUD SU DATABASE IMMOBILI.DB

def menu():
    """ Stampa a video del menu """
    print('1 - Seleziona catalogo') # Stampa a video degli immobili selezionati
    print('2 - Inserisci nuovo immobile')
    print('3 - Ricerca immobile')
    print('4 - Modifica immobile')
    print('5 - Elimina immobile')
    print('6 - Esci')

def inserisci(peewee_model, prop, citta, ind, mq, costr, pr):
    """ Inserimento nuovo immobile in database """

    db = peewee.SqliteDatabase('immobili.db')
    db.connect()

    nuovo_immobile = peewee_model(proprietario=prop, citta=citta, indirizzo=ind, mq=mq, costruzione = costr, prezzo=pr)
    nuovo_immobile.save()

    db.close()
    
    msg = 'Immobile inserito con successo!'
    return msg

immobili = []

def seleziona(peewee_model):
    """ Lettura immobili di un certo catalogo"""

    db = peewee.SqliteDatabase('immobili.db')
    db.connect()

    for immobile in peewee_model.select():
        immobili.append(immobile)

    db.close()


