#!/usr/bin/env python

import json
import sqlalchemy

select_query = """select places.country, count(*) as count_of_people from 
codetest.places as places, 
codetest.people as people
where 
places.city = people.place_of_birth
group by (places.country)"""

# connect to the database
engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
connection = engine.connect()

with open('/data/summary_output.json', 'w') as json_file:
  rows = connection.execute(select_query)
  result = {}
  rows = [result.update({row[0]: row[1]}) for row in rows]
  json.dump(result, json_file, separators=(',', ':'))