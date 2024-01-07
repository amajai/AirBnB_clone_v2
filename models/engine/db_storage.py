#!/usr/bin/python3
"""
Module that manages file storage for HBNB
"""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

models = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage:
    """
    Class for HBNB database storage
    """
    __engine = None
    __session = None

    def __init__(self):
        usr = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{usr}:{pwd}@{host}/{db}",
            pool_pre_ping=True,
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None, id=None):
        """
        Query all classes or specific one by ID
        """
        result = {}
        for clss in models:
            if cls is None or cls is models[clss] or cls is clss:
                print(cls)
                objs = self.__session.query(models[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    result[key] = obj
        return (result)

    def new(self, obj):
        """
        Add a new object to the current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Commit all changes in the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        reload method
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()

    def search(self, cls, id):
        """
        Search for an object of a specific class by ID
        """
        return self.all(cls, id)

    def close(self):
        """
        Close the current database session
        """
        self.__session.close()
