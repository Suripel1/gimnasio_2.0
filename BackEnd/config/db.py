from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_AqjWcfGnCVnYtG4JTrx@mysql-3bb66c0d-suripeli04-67e5.l.aivencloud.com:22923/defaultdb"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/test"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()