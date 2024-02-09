import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

user = os.getenv("MYSQL_USER", "root")
password = os.getenv("MYSQL_PASSWORD", "password")
host = os.getenv("MYSQL_HOST", "localhost")
port = os.getenv("MYSQL_PORT", "3306")
database = os.getenv("MYSQL_DATABASE", "test")

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
