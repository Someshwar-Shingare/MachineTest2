from django.db import models

# Create your models here.

class Book(models.Model):

    book_name = models.CharField(max_length=32)
    book_description = models.CharField(max_length=30)


class Author(models.Model):

    auth_name = models.CharField(max_length=32)
    email = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)


class Category(models.Model):


    cat_name = models.CharField(max_length=32)




