__author__ = 'gabrielebarbieri'

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os.path import abspath, dirname, join

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(abspath(dirname(__file__)), join('corpus', 'perec.db'))

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
Base = declarative_base()


class Verse(Base):
    __tablename__ = 'perec'

    id = Column(Integer, primary_key=True)
    author = Column(String)
    song = Column(String)
    line = Column(Integer)
    content = Column(String)

    def __repr__(self):
        return '<Verse(author={:}, song={:}, line={:})>'.format(self.author, self.song, self.line)


def create_all():
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sql_session = Session()

