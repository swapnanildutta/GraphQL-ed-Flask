import graphene
from graphene import relay

from ..models.genres import Genres as GenresModel
from ..models.books import Books as BooksModel
from ..types.books import Books

class Query(graphene.ObjectType):
    node = relay.Node.Field()

    books_by_name = graphene.List(Books, name=graphene.String())
    books_by_genre = graphene.List(Books, name=graphene.String())

    @staticmethod
    def resolve_books_by_name(parent, info, **args):
        q = args.get('name')

        books_query = Books.get_guery(info)

        return books_query.filter(BooksModel.name.contains(q)).all()

    @staticmethod
    def resolve_books_by_genre(parent, info, **args):
        q = args.get('genre')

        books_query = Books.get_guery(info)

        return books_query.join(GenresModel).filter(GenresModel.name == q).all()