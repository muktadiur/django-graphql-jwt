from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.ForeignKey('auth.User', related_name='authors', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=120)
    isbn = models.CharField(max_length=20)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
