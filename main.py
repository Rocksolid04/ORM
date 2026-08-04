from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('postgresql+psycopg2://postgres:HINDI@localhost:5432/satutorialdatabase',echo=True)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    age = Column(Integer)

    things = relationship('Thing',back_populates='person')

class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer,primary_key=True)
    description = Column(String,nullable=False)
    value = Column(Float)
    owner = Column(Integer, ForeignKey('people.id'))

    person = relationship('Person',back_populates='things')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_person = Person(name= 'Charlie', age=60)
session.add(new_person)
session.flush()

new_things = Thing(description = 'camera',value =500, owner = new_person.id)
session.add(new_things)

session.commit()

print(new_person.things)
print(new_things.person)
