from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType
from graphene import relay, ObjectType, Field
from graphene_django.filter import DjangoFilterConnectionField
from .models import Author, Book

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude_fields = ('password',)

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = ['first_name', 'last_name']
        interfaces = (relay.Node,)

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        filter_fields = ('title', 'publish_date')
        interfaces = (relay.Node,)


class Query(ObjectType):
    current_user = Field(UserType)
    author = relay.Node.Field(AuthorType)
    authors = DjangoFilterConnectionField(AuthorType)
    book = relay.Node.Field(BookType)
    books = DjangoFilterConnectionField(BookType)

    def resolve_current_user(self, info):
        if not info.context.user.is_authenticated:
            return None
        return info.context.user

    def resolve_authors(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return Author.objects.none()

        return Author.objects.filter(user=info.context.user)

    def resolve_books(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return Book.objects.none()

        return Book.objects.filter(author__user=info.context.user)
