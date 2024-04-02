#!/usr/bin/env python

import csv
import json
import sqlalchemy

# connect to the database
engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
connection = engine.connect()

metadata = sqlalchemy.schema.MetaData(engine)

# make ORM objects to refer to the table
Places = sqlalchemy.schema.Table('places', metadata, autoload=True, autoload_with=engine)
People = sqlalchemy.schema.Table('people', metadata, autoload=True, autoload_with=engine)

# load csv data into DB
def read_from_places_csv_into_db():
  with open('/data/places.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
      connection.execute(Places.insert().values(city=row[0], county=row[1], country=row[2]))

def read_from_people_csv_into_db():
  with open('/data/people.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
      connection.execute(People.insert().values(given_name=row[0], family_name=row[1], date_of_birth=row[2], place_of_birth=row[3]))

read_from_places_csv_into_db()
read_from_people_csv_into_db()
