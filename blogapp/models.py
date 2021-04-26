from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
class Category(models.Model):
    Name=models.CharField(max_length=256)

    def __str__(self):
        return self.Name

class Post(models.Model):
    Title=models.TextField()
    TitleSlug=models.SlugField(blank=True,null=True)
    OverView=models.TextField()
    Thumbnail=models.ImageField(upload_to='thumbnails/',blank=True,null=True)
    Content=RichTextUploadingField()
    Category=models.ManyToManyField(Category)
    DateAdded=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    Views=models.PositiveIntegerField(default=0)
    CommentCount=models.PositiveIntegerField(default=0)
    Likes=models.PositiveIntegerField(default=0)
    class Meta:
        ordering=['-DateAdded']

    def __str__(self):
        return self.TitleSlug
        
    def save(self,*args,**kwargs):
        self.TitleSlug=slugify(self.Title)
        super(Post,self).save(*args,**kwargs)


class ViewsModel(models.Model):
    User=models.CharField(max_length=256)
    Post=models.ForeignKey(Post,on_delete=models.CASCADE)


class Comment(models.Model):
    Name=models.CharField(max_length=256)
    Comment=models.TextField()
    Post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.Comment


class Like(models.Model):
    User=models.CharField(max_length=256)
    Post=models.ForeignKey(Post,on_delete=models.CASCADE)







    


