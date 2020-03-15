from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class School(models.Model):
    Name=models.CharField(max_length=256)
    Principal=models.CharField(max_length=256)
    Location=models.CharField(max_length=256)

    def __str__(self):
        return self.Name
class Student(models.Model):
    Name=models.CharField(max_length=32)
    Age=models.PositiveIntegerField()
    school=models.ForeignKey(School,related_name='SMI',on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
class Post(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    published = models.DateField(auto_now_add = True)
    slug = models.SlugField(unique = True, max_length = 100)
    tags = TaggableManager()

    def __str__(self):
        return self.title
