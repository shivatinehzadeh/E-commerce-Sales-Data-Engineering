from sqlalchemy import  Column, String, Integer, DateTime,BigInteger, Float, Boolean, orm
from sqlalchemy.ext.declarative import declarative_base
from db_session import engine
from pydantic import BaseModel

Base = orm.declarative_base()

class Customers(Base):
    __tablename__ = "customers"
    ID = Column(BigInteger, primary_key=True)
    gender = Column(String(10), nullable=False)
    ever_Married = Column(Boolean, nullable=True)
    age = Column(Integer, nullable=False)
    graduated = Column(Boolean, nullable=True)
    profession = Column(String(50), nullable=True)
    work_Experience = Column(Integer, nullable=False)
    spending_Score = Column(String(10), nullable=True)
    family_Size = Column(Integer, nullable=True)
    var_1 = Column(String(50), nullable=True)
    segmentation = Column(String(5), nullable=True)

class Products(Base):
    __tablename__ = "products"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    invoice = Column(Integer, nullable=False)
    country = Column(String(50), nullable=False)
    customer_id = Column(Integer, nullable=False)
    invoiceDate = Column(DateTime, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    stockCode = Column(Integer, nullable=False)
    description = Column(String(5000), nullable=False)

class Orders(Base):
    __tablename__ = "orders"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    event_time = Column(DateTime, nullable=False)
    event_type = Column(String(10), nullable=True)
    product_id = Column(BigInteger, nullable=False)
    category_id = Column(BigInteger, nullable=False)
    category_code = Column(String(500), nullable=True)
    price = Column(Integer, nullable=False)
    brand = Column(String(100), nullable=True)
    user_id = Column(BigInteger, nullable=False)
    user_session = Column(String(500), nullable=True)

Base.metadata.create_all(bind=engine)