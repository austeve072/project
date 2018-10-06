from peewee import *

db = PostgresqlDatabase('company', user = 'postgres', host = 'localhost', password = 'root')

print("Connection was successful!")

db.connect()
class Project(Model):
    id = AutoField()
    title = CharField()
    type = CharField()
    start_from = DateField()
    end_at = DateField()
    description = TextField()
    amount = DoubleField()
    status = IntegerField()


    class Meta:
        database = db
        table_name = 'projects_1'

Project.create_table(fail_silently=True) #fail silently table will not be created twice


#projectOne = Project(title = 'Dining hall construction',
#                     type = 'internal',
#                     start_from = '2018-09-25',
#                     end_at = '2018-03-25',
#                     description = 'dining hall for boarders',
#                     amount = 800000,
#                     status = 1)
#projectOne.save()

#print('all my records: ', Project.select()) #prints all the records

#get a record where the titlw equals "Dining hal construction"
#row1 = Project.get(Project.title == 'Dining hall construction')

#print(row1.title, row1.start_from)

#for myproject in Project.select():
 #   print(myproject.description, myproject.amount)