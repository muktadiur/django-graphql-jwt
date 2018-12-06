import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from mixer.backend.django import mixer
from graphene.test import Client
from bookshop.schema import SCHEMA


pytestmark = pytest.mark.django_db


def test_resolve_current_user():
    user = mixer.blend('auth.User', email='test@gmail.com')
    client = Client(SCHEMA)
    query = '''
    {
        currentUser {
            email
        }
    }
    '''

    req = RequestFactory().get('/')
    req.user = user
    result = client.execute(query, context=req)
    
    assert result == {
        "data": {
            "currentUser": {
                "email": "test@gmail.com"
            }
        }
    }

def test_resolve_all_authors():
    author = mixer.blend('books.Author', first_name='test', last_name='1')
    mixer.blend('books.Author', user=author.user, first_name='test', last_name='2')
    client = Client(SCHEMA)
    query = '''
    {
        authors {
            edges {
                node {
                    lastName
                    firstName
                }
            }
        }
    }
    '''
    req = RequestFactory().get('/')
    req.user = author.user
    result = client.execute(query, context=req)
    assert result == {
        "data": {
            "authors": {
                "edges": [
                    {
                        "node": {
                            "lastName": "1",
                            "firstName": "test",
                        }
                    },
                    {
                        "node": {
                            "lastName": "2",
                            "firstName": "test",
                        }
                    }
                ]
            }
        }
    }
    
def test_resolve_all_books():
    book = mixer.blend('books.Book', title='Python')
    mixer.blend('books.Book', author__user=book.author.user, title='Django')
    client = Client(SCHEMA)
    query = '''
    {
        books {
            edges {
                node {
                    title
                }
            }
        }
    }
    '''

    req = RequestFactory().get('/')
    req.user = book.author.user
    result = client.execute(query, context=req)
    
    assert result == {
        "data": {
            "books": {
                "edges": [
                    {
                        "node": {
                            "title": "Python"
                        }
                    },
                    {
                        "node": {
                            "title": "Django"
                        }
                    }
                ]
            }
        }
    }

