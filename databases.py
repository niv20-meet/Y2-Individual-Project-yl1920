from model import Base


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(username,password,email,picture_link):

    user_object = User(
        username = username,
        email=email,
        password=password,
        picture_link=picture_link
        )
    session.add(user_object)
    session.commit()

def edit_password(email,new_password):

     user_object = session.query(
     User).filter_by(
     email).first()
     user_object.password=new_password
     session.commit()

def get_user(username):
    """Find the first user in the DB, by their username."""
    return session.query(User).filter_by(username=username).first()


def query_all():
    all_users = session.query(
    User).all()
    return all_users




