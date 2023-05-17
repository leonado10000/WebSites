from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model):
    uid = models.IntegerField()
    uname = models.CharField(max_length=100)
    upassword = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.uname

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

class Scotops(models.Model):
    scoto_id = models.IntegerField(primary_key=True)                                        # ID of each scoto ex. 1034
    scoto_name = models.CharField(max_length=100)                                           # name of the scoto sx. sheduler
    scoto_idea_brief = models.CharField(max_length=120, default="No idea")                                     # explain it in 50-100 words
    scoto_idea_details = models.CharField(max_length=10000 , blank=True, null=True)                                 # challenge you to outwrite the max
    scoto_datetime = models.DateTimeField( default=datetime.now)                            # date and time
    scoto_tag = models.ManyToManyField(Tags, related_name="TA",blank=True)                  # tags like - original/outsourced etc
    scoto_auther = models.ManyToManyField(User,related_name="Auther_names",max_length=10000)# can be multiple auther/writer
    scoto_category = models.ForeignKey(Category,on_delete=models.DO_NOTHING, default=404)    # category as in idea or rant or anything

    def __str__(self) -> str:
        return f"{self.scoto_id} => {self.scoto_name}  {self.scoto_auther}"

class Comments(models.Model):
    c_id = models.ForeignKey(Scotops, on_delete=models.CASCADE)                             # comment id
    c_content = models.CharField(max_length=1000)                                           # The comment
    c_ter = models.ForeignKey(User,on_delete=models.CASCADE, related_name="commeter_name")  # user who commmented
    c_likes = models.IntegerField(default=1)                                                         # likes on the comment
    def __str__(self) -> str:
        return f"{self.c_id}: by {self.c_ter}"
