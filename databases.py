from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(password,email,picture_link):

    user_object = user(
        email=email,
        password=password,
        picture_link=picture_link
        )
    session.add(user_object)
    session.commit()

def edit_password(email,new_password):

     user_object = session.query(
     user).filter_by(
     email).first()
    user_object.password=new_password
    session.commit()



def query_all():

  all_users = session.query(
    user).all()
   return all_users




