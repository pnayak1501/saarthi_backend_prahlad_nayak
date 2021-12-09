from djongo import models

# Create your models here.

class Books(models.Model):
    id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20)
    authors = models.JSONField()
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    release_date = models.DateField()
    objects = models.DjongoManager()


