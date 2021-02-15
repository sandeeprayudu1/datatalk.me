from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


    def get_absolute_url (self):
        #return reverse('artical-detail',args = str(self.id))
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User,null = True,on_delete = models.CASCADE)
    bio = models.TextField()
    profile_pic = CloudinaryField('images/')
    website_url = models.CharField(max_length = 255,null = True,blank = True)
    facebook_url = models.CharField(max_length = 255,null = True,blank = True)
    twitter_url = models.CharField(max_length = 255,null = True,blank = True)
    instagram_url = models.CharField(max_length = 255,null = True,blank = True)
    pinterest_url = models.CharField(max_length = 255,null = True,blank = True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url (self):
        #return reverse('artical-detail',args = str(self.id))
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length = 255)
    image = CloudinaryField('image')
    header_image = CloudinaryField('headerimage')
    title_tag = models.CharField(max_length = 255)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    category = models.CharField(max_length = 255)
    snippet = models.CharField(max_length = 255)
    body = RichTextField(blank = True,null = True)
    #body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now,blank = True)
    likes = models.ManyToManyField(User,related_name = 'blog_posts')
   
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)


    def get_absolute_url (self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name = "comments",on_delete = models.CASCADE)
    name = models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s - %s' %(self.post.title,self.name)




class Project(models.Model):
    title = models.CharField(max_length = 255)
    image = CloudinaryField('image')
    #header_image = models.ImageField(null = True,blank = True,upload_to = 'Images/')
    #title_tag = models.CharField(max_length = 255)
    #body = RichTextField(blank = True,null = True)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.now,blank = True)
    github_link = models.URLField(max_length = 200)
  

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    message = models.TextField()


    def __str__(self):
        return self.name + ' | ' + str(self.email)
