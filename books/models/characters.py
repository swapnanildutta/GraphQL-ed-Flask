from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from ..database.base import Base
from ..models.books import Books

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship(
        Books,
        backref=backref('characters', uselist=True, cascade='delete,all')
    )