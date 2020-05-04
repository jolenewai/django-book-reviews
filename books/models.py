from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=35)
    last_name = models.CharField(blank=False, max_length=35)
    dob = models.DateField(blank=True)

    def __str__(self):
        author_name = self.first_name + ' ' + self.last_name
        return author_name