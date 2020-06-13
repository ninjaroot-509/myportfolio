from django.db import models


class Contactus(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        verbose_name_plural = "Contactus"
 
    def __str__(self):
        return self.last_name + "-" +  self.email


class Work(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='myworks/')
    body = models.TextField()
    link = models.CharField(max_length=200)
    
    def str(self):
        return self.title


class Dcoder(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='myworks/')
    body = models.TextField()
    local = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
        
    def str(self):
        return self.name


class Aboutme(models.Model):
    image = models.ImageField(upload_to='myworks/')
    body = models.TextField()
    whatsapp = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
            

class Prog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
            
    def str(self):
        return self.title

CATEGORY_CHOICES = (
    ('D', 'design'),
    ('W', 'web'),
    ('B', 'brand')
)

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
            
    def str(self):
        return self.category        
            
class Myimgacceuil(models.Model):
    image = models.ImageField(upload_to='myimghome/')