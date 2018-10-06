from peewee import *

db = PostgresqlDatabase('company', user = 'postgres', host = 'localhost', password = 'root')

db.connect()
class User(Model):
    id = AutoField()
    name = CharField()
    email = CharField()
    password = CharField()


    class Meta:
        database = db
        table_name = 'users'

User.create_table(fail_silently=True) #fail silently table will not be created twice

