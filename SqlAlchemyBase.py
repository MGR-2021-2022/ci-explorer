from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:MyNewPass@localhost:3306/vscode')
Session = sessionmaker(bind=engine)

Base = declarative_base()