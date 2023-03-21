import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from decouple import config

username = config('DB_USERNAME')
password = config('DB_PASSWORD')
db = config('DB')
ip = config('IP')
port = config('PORT')
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{username}:{password}@{ip}:{port}/{db}"

engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = _declarative.declarative_base()