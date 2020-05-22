from rest_framework import serializers
from .models import productLine, lineCategory, product,tileColor, solutionLine, solutionCategory, solution, groutColors, pastProjects, whereToBuy, Downloads, feedBacks, Carousel, applicationVideos

class productLineSerializer(serializers.ModelSerializer):
    lineName = serializers.CharField()

    class Meta:
        model  = productLine
        # fields = ('lineName','image','details',)
        fields = ('lineName',)
         

class lineCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model  = lineCategory
        fields = ('lineName','categoryName','image',)

class productSerializer(serializers.ModelSerializer):

    class Meta:
        model  = product
        # fields = ('categoryName', 'productName', 'image', 'details','features',)
        fields = ('categoryName', 'productName', 'image', 'details',)

class productNameOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = ('productName', 'image','pk')

# class groutColorSerializer(serializers.ModelSerializer):

#     class Meta:
#         model  = groutColor
#         fields = ('colorID','groutName','details',)

class pastProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model  = pastProjects
        fields = ('projectTitle', 'details', 'image',)

class pastProjectOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model  = pastProjects
        fields = ('projectTitle', 'image',)

class whereToBuySerializer(serializers.ModelSerializer):

    class Meta:
        model = whereToBuy
        fields = ('country', 'storeName', 'address', 'postalCode', 'telephone', 'faxNumber', 'latitude', 'longitude',)

class carouselSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carousel
        fields = ('imageName', 'image',)

class feedBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = feedBacks
        fields = ('firstName','lastName','company','postalCode','phone','email','country','message','typeOfAssistance')


class DownloadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Downloads
        # fields = ('fileName', 'thumbnail',)
        fields = ('fileName', 'pdfFile',)


class applicationVideosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = applicationVideos
        # fields = ('fileName', 'thumbnail',)
        fields = ('fileName','videoFile',)


class oneDownloadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Downloads
        fields = ('fileName', 'pdfFile',)

class oneapplicationVideosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = applicationVideos
        fields = ('fileName', 'videoFile',)


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'uniqueid')


class solutionLineSerializer(serializers.ModelSerializer):
    lineName = serializers.CharField()

    class Meta:
        model  = solutionLine
        # fields = ('lineName','image','details',)
        fields = ('lineName',)

         
class solutionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model  = solutionCategory
        fields = ('lineName','categoryName','image',)

class solutionSerializer(serializers.ModelSerializer):

    class Meta:
        model  = solution
        # fields = ('categoryName', 'solutionName', 'image', 'details','features',)
        fields = ('categoryName', 'solutionName', 'image', 'details',)


class solutionNameOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = solution
        fields = ('solutionName', 'image','pk')

class tileColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = tileColor
        fields = ('colorName', 'image')

class groutColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = groutColors
        fields = ('colorName', 'image')

