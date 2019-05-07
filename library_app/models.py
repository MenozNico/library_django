from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.surname

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books')
    genre = models.ManyToManyField('Genre')
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

class AuthorBook(models.Model):
    author_id = models.ForeignKey('Author', on_delete=models.CASCADE)
    book_id = models.ForeignKey('Book', on_delete=models.CASCADE)

