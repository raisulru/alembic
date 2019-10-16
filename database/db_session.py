from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import DATABASE_URI


some_engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=some_engine)
