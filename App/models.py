from django.db import models
from datetime import datetime
# Create your models here.

class Persona(models.Model):
    P_id = models.IntegerField()
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    def __str__(self) -> str:
        return f"{self.name}"

    
# class Category(models.Model):
#     C_id = models.IntegerField()
#     name = models.CharField(max_length=30)
#     def __str__(self) -> str:
#         return f"{self.C_id}: {self.name}"


# class Tags(models.Model):
#     T_id = models.IntegerField()
#     name = models.CharField(max_length=30,default="Tag")
#     def __str__(self) -> str:
#         return f"{self.T_id}: {self.name}"




# class Granger(models.Model):
    
#     P_id = models.IntegerField()
#     title = models.CharField(max_length=60)
#     auther = models.ForeignKey("Persona",on_delete=models.DO_NOTHING)
#     date = models.DateTimeField(default=datetime.now())
#     description = models.CharField(max_length=100,null=True,blank=True)
#     P_tags = models.ManyToManyField('Tags',related_name="PTags")
#     category = models.ManyToManyField("Category",related_name="Category")
#     details = models.CharField(max_length=1500,null=True,blank=True)
#     likedby = models.ManyToManyField("Persona",related_name="liked")
#     image = models.ImageField(upload_to=f"post\{P_id}",default="App\static\Yorsy.jpg")
    

#     def __str__(self) -> str:
#         return f"{self.title} by {self.auther}"
#     def likes(self):
#         if self.likedby.count()==1:
#             return "1 like"
#         return f"{self.likedby.count()} likes"
#     def tages(self):
#         return self.tags
    

# class Comment(models.Model):
#     C_id = models.IntegerField()
#     comment = models.CharField(max_length=100)
#     auther = models.ForeignKey("Persona",on_delete=models.DO_NOTHING)
#     liked = models.ManyToManyField("Persona",related_name="Commentlikedby")

#     def likes(self):
#         if self.liked.count()==1:
#             return "1 like"
#         return f"{self.liked.count()} likes"