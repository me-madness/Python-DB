from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# CONNECTION_STRING='<dialect>+<drive>://<username>:<password>@<host>:<port>/database'
CONNECTION_STRING='postgresql+psycopg2://postgres:Dragulia131@@localhost:5432/sqlalchemy'

engine = create_engine('CONNECTION_STRING')
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    
Base.metadata.create_all(engine)    