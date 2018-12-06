import pytest
from .. import schema

pytestmark = pytest.mark.django_db

def test_user_type():
    instance = schema.UserType()
    assert instance

def test_author_type():
    instance = schema.AuthorType()
    assert instance

def test_book_type():
    instance = schema.BookType()
    assert instance

