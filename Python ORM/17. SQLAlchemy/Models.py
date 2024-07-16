from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

CONNECTION_STRING='<dialect>+<drive>://<username>:<password>@<host>:<port>/database'
CONNECTION_STRING='postgresql+psycopg2://postgres:Dragulia131@@localhost:5432/sqlalchemy'

engine = create_engine('CONNECTION_STRING')