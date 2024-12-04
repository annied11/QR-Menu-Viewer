from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define Order Model
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    orders = Column(String, nullable=False)
    table_number = Column(Integer, nullable=False)

# Database setup
engine = create_engine('sqlite:///order.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
db_session = Session()
