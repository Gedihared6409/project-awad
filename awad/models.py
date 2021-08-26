from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    photo = models.ImageField(default='Blank-Avatar.JPG', blank =True,null = True)
    Bio = models.CharField(max_length=30,blank =True )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    datecreated= models.DateField(auto_now_add=True,blank =True )

    def __str__(self):
        return self.Bio


class Projects(models.Model):
    title = models.CharField(max_length=30,blank =True)
    description = models.TextField(max_length=300,blank =True)
    projectscreenshot = models.ImageField(blank = True)
    projecturl= models.URLField(max_length=200,blank =True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    datecreated= models.DateField(auto_now_add=True,blank =True )
    
    def __str__(self):
        return self.title
RATE_CHOICES = [
(1,'1- Trash'),
(2,'2- Horrible'),
(3,'3- Terrible'),
(4,'4- Bad'),
(5,'5- Ok'),
(6,'6- Watchable'),
(7,'7- Good'),
(8,'8- Very Good'),
(9,'9- perfect'),
(10,'10- Master Piece'),
]

class Revieww(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    projects = models.ForeignKey(Projects,on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=3000,blank=True)
    design = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default= 0)
    usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    content = models.PositiveSmallIntegerField(choices = RATE_CHOICES,default = 0)
    


    def __str__(self):
        return self.user.username