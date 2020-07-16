from django.contrib import admin
from .models import productLine, lineCategory, product, groutColors,tileColor, pastProjects, Downloads, feedBacks, Carousel, whereToBuy, applicationVideos, solutionLine, solutionCategory, solution, aboutUs


# Register your models here.
admin.site.register([productLine,lineCategory,tileColor,product,solutionLine, solutionCategory, solution, groutColors,pastProjects, Downloads, feedBacks, Carousel, whereToBuy, applicationVideos, aboutUs])
# admin.site.register(lineCategory)
# admin.site.register(product)
# admin.site.register(groutColor)
# admin.site.register(pastProjects)
