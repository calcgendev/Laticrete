from django.db import models
import os
# from django.contrib.postgres.fields import ArrayField
# Create your models here.
class productLine(models.Model):
    lineName        = models.CharField(max_length=50, primary_key=True)
    # image           = models.ImageField(upload_to='static/')
    # details         = models.CharField(max_length=1000, null=True)
    
    class Meta:
        verbose_name = 'Product Line'
        verbose_name_plural = 'Product Lines'


    def __str__(self):
        return self.lineName

class lineCategory(models.Model):
    lineName        = models.ForeignKey(productLine, on_delete= models.CASCADE)
    categoryName    = models.CharField(max_length=50, primary_key=True)
    image           = models.ImageField(upload_to='static/', null = True)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.categoryName

class product(models.Model):
    categoryName    = models.ForeignKey(lineCategory, on_delete= models.CASCADE)
    productName     = models.CharField(max_length=50)
    image           = models.ImageField(upload_to='uploads/')
    details         = models.TextField(max_length=10000, null=True)
    videoFile       = models.FileField(upload_to='static/', null=True, blank=True)
    pdfFile         = models.FileField(upload_to='static/', null=True, blank=True)

    # features        = models.TextField(max_length = 10000, null = True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.productName




class solutionLine(models.Model):
    lineName        = models.CharField(max_length=50, primary_key=True)
    # image           = models.ImageField(upload_to='static/')
    # details         = models.CharField(max_length=1000, null=True)

    class Meta:
        verbose_name = 'Solution Line'
        verbose_name_plural = 'Solution Lines'


    def __str__(self):
        return self.lineName

class solutionCategory(models.Model):
    lineName        = models.ForeignKey(solutionLine, on_delete= models.CASCADE)
    categoryName    = models.CharField(max_length=50, primary_key=True)
    image           = models.ImageField(upload_to='static/', null = True)

    class Meta:
        verbose_name = 'Solution Category'
        verbose_name_plural = 'Solution Categories'

    def __str__(self):
        return self.categoryName

class solution(models.Model):
    categoryName    = models.ForeignKey(solutionCategory, on_delete= models.CASCADE)
    solutionName    = models.CharField(max_length=50)
    image           = models.ImageField(upload_to='uploads/')
    details         = models.TextField(max_length=10000, null=True)
    videoFile       = models.FileField(upload_to='static/', null=True, blank=True)
    pdfFile         = models.FileField(upload_to='static/', null=True, blank=True)

    # features        = models.TextField(max_length = 10000, null = True)

    class Meta:
        verbose_name = 'Solution'
        verbose_name_plural = 'Solutions'

    def __str__(self):
        return self.solutionName




class pastProjects(models.Model):
    projectTitle    = models.CharField(max_length= 50, primary_key=True)
    details         = models.TextField(max_length= 10000, null= True)
    image           = models.ImageField(upload_to='uploads/') 

    class Meta:
        verbose_name = 'Past Project'
        verbose_name_plural = 'Past Projects'


    def __str__(self):
        return self.projectTitle


class whereToBuy(models.Model):
    country         = models.CharField(max_length= 30)
    storeName       = models.CharField(max_length= 40) 
    address         = models.CharField(max_length= 50)
    postalCode      = models.CharField(max_length= 40)      
    telephone       = models.CharField(max_length= 15)
    faxNumber       = models.CharField(max_length= 20)
    latitude        = models.CharField(max_length= 15)
    longitude       = models.CharField(max_length= 15)

    class Meta:
        verbose_name = 'Where to buy'
        verbose_name_plural = 'Where to buy'


    def __str__(self):
        return self.storeName   

class Carousel(models.Model):
    imageName       = models.CharField(max_length=30,primary_key=True)
    image           = models.ImageField(upload_to='static/')

    class Meta:
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousels'


class feedBacks(models.Model):
    firstName       = models.CharField(max_length=30, null=True)
    lastName        = models.CharField(max_length=30, null=True) 
    company         = models.CharField(max_length=40, null=True)  
    postalCode      = models.CharField(max_length=30, null=True)  
    phone           = models.CharField(max_length=20, null=True)
    email           = models.CharField(max_length=50, null=True) 
    country         = models.CharField(max_length=30, null=True) 
    typeOfAssistance= models.CharField(max_length=1000, null=True)
    message         = models.TextField(max_length=1000, null=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return self.message   


class Downloads(models.Model):
    fileName        = models.CharField(max_length=30, primary_key=True)
    pdfFile         = models.FileField(upload_to='static/')
    # thumbnail       = models.ImageField(upload_to='static', null=True)

    class Meta:
        verbose_name = 'Download'
        verbose_name_plural = 'Downloads'


class applicationVideos(models.Model):
    fileName        = models.CharField(max_length=30, primary_key=True)
    videoFile       = models.FileField(upload_to='static/')
    # thumbnail       = models.ImageField(upload_to='static', null=True)

    class Meta:
        verbose_name = 'Application Video'
        verbose_name_plural = 'Application Videos'

class tileColor(models.Model):
    colorName   = models.CharField(max_length=30, null=True)
    image       = models.ImageField(upload_to='static/')

    class Meta:
        verbose_name = 'Tile Color'
        verbose_name_plural = 'Tile Colors'

class groutColors(models.Model):
    colorName   = models.CharField(max_length=30, null=True)
    image       = models.ImageField(upload_to='static/')

    class Meta:
        verbose_name = 'Grout Color'
        verbose_name_plural = 'Grout Colors'

class aboutUs(models.Model):
    image           = models.ImageField(upload_to='uploads/')
    content         = models.TextField(max_length = 10000, null = True)

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


