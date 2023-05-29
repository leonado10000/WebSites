from django.db import models
from datetime import datetime
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Tags(models.Model):
    tag_id = models.IntegerField()
    tag_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.tag_name

class Category(models.Model):
    cat_id = models.IntegerField()
    cat_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.cat_name

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=10,null=True)

    # user_permissions = models.ManyToManyField('User',related_name='ups',null=True)
    # groups = models.ManyToManyField('User',related_name='Gps',null=True)
    def __str__(self) -> str:
        return self.name
    
    
class Scotops(models.Model):
    scoto_id = models.AutoField(primary_key=True)                                           # ID of each scoto ex. 1034
    scoto_name = models.CharField(max_length=100)                                           # name of the scoto sx. sheduler
    scoto_datetime = models.DateTimeField(default=datetime.now)                             # date and time
    
    scoto_idea_brief = models.CharField(max_length=120, default="No idea")                  # explain it in 50-100 words
    scoto_idea_details = models.CharField(max_length=10000 , blank=True, null=True)         # challenge you to outwrite the max
    
    scoto_auther = models.ManyToManyField('User',related_name="Auther_names")               # can be multiple auther/writer
    scoto_tag = models.ManyToManyField('Tags', related_name="TA",blank=True)                # tags like - original/outsourced etc
    scoto_category = models.ForeignKey('Category',on_delete=models.DO_NOTHING)              # category as in idea or rant or anything

    liked = models.ManyToManyField('User',related_name="likedBy")
    image = models.ImageField(upload_to='blog\%Y\%m',default="Scotopia\static\Yorsy.jpg")

    def __str__(self) -> str:
        k = self.scoto_auther.first().__str__()
        return f"{self.scoto_id} => {self.scoto_name}  {k}"
    def likes(self):
        return f"{self.liked.count()} likes"


class Comments(models.Model):
    C_id = models.ForeignKey('Scotops', on_delete=models.CASCADE)                             # comment id
    Comment = models.CharField(max_length=1000)                                               # The comment
    Commenter = models.ForeignKey('User',on_delete=models.CASCADE,related_name="Commenter",null=True)                            # user who commmented
    liked = models.ForeignKey('User',on_delete=models.DO_NOTHING,related_name="LikedComment",null=True)                                                  # likes on the comment
    
    def __str__(self) -> str:
        return f"on {self.C_id}: by {self.Commenter}"
