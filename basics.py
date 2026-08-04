from sqlalchemy import create_engine, text, MetaData, Column, Integer, String, Table, Float, ForeignKey, func

engine = create_engine('postgresql+psycopg2://postgres:HINDI@localhost:5432/satutorialdatabase',echo=True)

meta = MetaData()

people = Table(
    "people",
    meta,
    Column('id',Integer, primary_key=True),
    Column('name',String,nullable=False),
    Column('age',Integer)
)

things = Table(
    "things",
    meta,
    Column('id',Integer, primary_key=True),
    Column('description',String,nullable=False),
    Column('value',Float),
    Column('owner',Integer,ForeignKey('people.id'))

)
 
meta.create_all(engine)

conn = engine.connect()

"""insert_people = people.insert().values([
    {'name':'Mike','age':30},
    {'name':'john','age':35},
    {'name':'nancy','age':25},
    {'name':'lore','age':20},
    {'name':'clara','age':40},
])

insert_things = things.insert().values([
    {'owner':2,'description':'Laptop', 'value':800.50},
    {'owner':1,'description':'Mouse', 'value':50.50},
    {'owner':5,'description':'Keyboard', 'value':100.50},
    {'owner':8,'description':'Book', 'value':30},
    {'owner':2,'description':'Bottle', 'value':10.50},
    {'owner':4,'description':'Speaker', 'value':10.50},
])"""

join_statement = people.join(things,people.c.id == things.c.owner)

select_statement = people.select().with_only_columns(people.c.name,things.c.description).select_from(join_statement)

result = conn.execute(select_statement)

for row in result.fetchall():
    print(row)

"""conn.execute(insert_people)
conn.commit()

conn.execute(insert_things)
conn.commit()"""

"""conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str,age int)"))

conn.commit()

from sqlalchemy.orm import Session

session = Session(engine)

session.execute(text('INSERT INTO people (name,age) VALUES("Mike","30");'))

session.commit()"""

group_by_statement = things.select().with_only_columns(things.c.owner,func.sum(things.c.value)).group_by(things.c.owner)

result = conn.execute(group_by_statement)

for row in result.fetchall():
    print(row)
