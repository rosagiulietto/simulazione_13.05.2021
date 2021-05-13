import peewee

db = peewee.SqliteDatabase('immobili.db')

class Prestigio(peewee.Model):
    proprietario = peewee.CharField()
    citta = peewee.CharField()
    indirizzo = peewee.TextField()
    mq = peewee.IntegerField()
    costruzione = peewee.IntegerField()
    prezzo = peewee.IntegerField()

    class Meta:
        database = db
        db_table = 'prestigio'

class CasaVacanza(peewee.Model):
    proprietario = peewee.CharField()
    citta = peewee.CharField()
    indirizzo = peewee.TextField()
    mq = peewee.IntegerField()
    costruzione = peewee.IntegerField()
    prezzo = peewee.IntegerField()

    class Meta:
        database = db
        db_table = 'casa vacanza'

class Popolare(peewee.Model):
    proprietario = peewee.CharField()
    citta = peewee.CharField()
    indirizzo = peewee.TextField()
    mq = peewee.IntegerField()
    costruzione = peewee.IntegerField()
    prezzo = peewee.IntegerField()

    class Meta:
        database = db
        db_table = 'popolare'

db.connect()

db.create_tables([Prestigio, CasaVacanza, Popolare])