from peewee import *

import datetime

DATABASE = SqliteDatabase('sources.sqlite')

#To connect to Postgres
#DATABASE = PostgresqlDatabase('sources', user='postgres')

#Define Source Model
class Source(Model):
	style = CharField()
	source = CharField()
	lastname=CharField()
	firstname=CharField()
	title = CharField() 
	publisher = CharField()
	date = CharField()
	website = CharField()
	volume = IntegerField()
	issue = IntegerField()
	pages = CharField()
	created_at: DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE #use the db defined above as DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Source], safe=True)
	print("Connected to the DB and created tables if they weren't already there")

	DATABASE.close()