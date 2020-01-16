from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class user(Base):
  	__tablename__ = 'user'
   id = Column(Integer, primary_key=True)
   email = Column(String)
   password = Column(string)
   picture_link = Column(String)
   

class cart(Base):
	id=Column(Integer,primary_key=True)
	pid=Column(Integer)