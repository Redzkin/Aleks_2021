from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FileField(upload_to='img/')


# class Comments(models.Model):
#     author = models.CharField(max_length=150)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return '{} - {}'.format(self.livre.title, self.user)
#
# class Post(models.Model):
#     title = models.CharField(max_length=250)
#     body = models.TextField()
#     cteated_on = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now=True)
#     categories = models.models.ManyToManyField('Category', related_name='posts')
#
# class Category(models.Model):
#     name = models.CharField(max_length=50)