from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter
import json
import random
from .models import productLine, lineCategory, product,tileColor,solutionLine,solutionCategory, solutionCategory, solution, groutColors, pastProjects, whereToBuy, Downloads, Carousel, feedBacks, applicationVideos
from .serializers import productLineSerializer,lineCategorySerializer, productSerializer, tileColorSerializer,solutionLineSerializer, solutionCategorySerializer, solutionSerializer, solutionNameOnlySerializer,groutColorSerializer, pastProjectsSerializer, pastProjectOnlySerializer,productNameOnlySerializer,  SearchSerializer, whereToBuySerializer, DownloadSerializer, carouselSerializer, feedBackSerializer, applicationVideosSerializer, oneDownloadSerializer, oneapplicationVideosSerializer
# Create your views here.

class productLineList(generics.ListCreateAPIView):
    queryset         = productLine.objects.all()
    serializer_class = productLineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends  = [SearchFilter]
    search_fields    = ['lineName']

    def get_queryset(self):
        queryset = productLine.objects.all()
        linename  = self.request.query_params.get('lineName', None)
        if linename is not None:
            queryset = queryset.filter(lineName = linename)
        return queryset
    

class productLineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = productLine.objects.all()
    serializer_class = productLineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class lineCategoryList(generics.ListCreateAPIView):
    queryset         = lineCategory.objects.all()
    serializer_class = lineCategorySerializer
    filter_backends  = [SearchFilter]
    search_fields    = ['categoryName']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = lineCategory.objects.all()
        linename  = self.request.query_params.get('lineName', None)
        if linename is not None:
            queryset = queryset.filter(lineName = linename)
        return queryset


class lineCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = lineCategory.objects.all()
    serializer_class = lineCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class productList(generics.ListCreateAPIView):
    queryset         = product.objects.all()
    serializer_class = productNameOnlySerializer
    # serializer_class = productSerializer
    filter_backends  = [SearchFilter]
    search_fields    = ['productName']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = product.objects.all()
        categoryname  = self.request.query_params.get('categoryName', None)
        if categoryname is not None:
            queryset = queryset.filter(categoryName = categoryname)
        return queryset

class productDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = product.objects.all()
    serializer_class = productSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



# def prodispatcher(request, productName=None,categoryName=None):
#     productqueryset         = products.objects.all()
#     lis = []
#     pss  = productqueryset.filter(productName = productName, categoryName=categoryName)
#     for ps in pss:
#         lis.append({'productName':ps.productName, 'image':ps.image, 'details':ps.details})

#     data = json.dumps(lis)  
#     # serialized_data = SearchSerializer(lis, many = True)
#     return HttpResponse(data, content_type='application/json')

def soldispatcher(request, solutionName=None,categoryName=None):
    solutionqueryset         = solution.objects.all()
    lis = []
    pss  = solutionqueryset.filter(solutionName = solutionName, categoryName=categoryName)
    for ps in pss:
        lis.append({'categoryName':ps.categoryName,'solutionName':ps.solutionName, 'image':ps.image, 'details':ps.details})

    data = json.dumps(lis)  
    # serialized_data = SearchSerializer(lis, many = True)
    return HttpResponse(data, content_type='application/json')
    

class pastProjectsList(generics.ListCreateAPIView):
    queryset         = pastProjects.objects.all()
    serializer_class = pastProjectOnlySerializer
    filter_backends  = [SearchFilter]
    search_fields    = ['projectTitle']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class pastProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = pastProjects.objects.all()
    serializer_class = pastProjectsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class whereToBuyList(generics.ListCreateAPIView):
    queryset         = whereToBuy.objects.all()
    serializer_class = whereToBuySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DownloadList(generics.ListCreateAPIView):
    queryset         = Downloads.objects.all()
    serializer_class = DownloadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DownloadsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Downloads.objects.all()
    serializer_class = oneDownloadSerializer     
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class applicationVideosList(generics.ListCreateAPIView):
    queryset         = applicationVideos.objects.all()
    serializer_class = applicationVideosSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class applicationVideosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = applicationVideos.objects.all()
    serializer_class = oneapplicationVideosSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class feedbackList(generics.ListCreateAPIView):
    queryset         = feedBacks.objects.all()
    serializer_class = feedBackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class carouselList(generics.ListCreateAPIView):
    # queryset         = sorted(Carousel.objects.all(), key=lambda x: random.random())[:5]
    queryset         = Carousel.objects.all()[:5]
    serializer_class = carouselSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class allcarouselList(generics.ListCreateAPIView):
    queryset         = Carousel.objects.all()
    serializer_class = carouselSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def addFeedback(request):
    mes         = request.GET.get('message', None)
    if mes is None:
        mes = ' '

    countr          = request.GET.get('country', None)
    if countr is None:
        countr = ' '

    fname = request.GET.get('firstName', None)
    if fname is None:
        fname = ' '

    lname = request.GET.get('lastName', None)
    if lname is None:
        lname = ' '

    com   = request.GET.get('company', None)
    if com is None:
        com = ' '

    phon  = request.GET.get('phone', None)
    if phon is None:
        phon = ' '

    em    = request.GET.get('email', None)
    if em is None:
        em = ' '

    toa   = request.GET.get('toa', None)
    if toa is None:
        toa = ' '

    pCode = request.GET.get('postalCode', None)
    if pCode is None:
       pCode = ''

    feedBacks.objects.create(firstName=fname,lastName=lname,company=com, postalCode=pCode, phone=phon, email=em, country = countr,typeOfAssistance=toa,message = mes)
    # send_mail(subject='Laticrete Feedback', message=mes, from_email='dhungel611@gmail.com',recipient_list=['pracant.tandon@gmail.com'],fail_silently=True)
    return(HttpResponseRedirect('../../../laticreteapp/feedback/'))


class solutionLineList(generics.ListCreateAPIView):
    queryset         = solutionLine.objects.all()
    serializer_class = solutionLineSerializer
    filter_backends  = [SearchFilter]
    search_fields    = ['lineName']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = solutionLine.objects.all()
        linename  = self.request.query_params.get('lineName', None)
        if linename is not None:
            queryset = queryset.filter(lineName = linename)
        return queryset
    

class solutionLineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = solutionLine.objects.all()
    serializer_class = solutionLineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class solutionCategoryList(generics.ListCreateAPIView):
    queryset         = solutionCategory.objects.all()
    serializer_class = solutionCategorySerializer
    filter_backends  = [SearchFilter]
    search_fields    = ['categoryName']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = solutionCategory.objects.all()
        linename  = self.request.query_params.get('lineName', None)
        if linename is not None:
            queryset = queryset.filter(lineName = linename)
        return queryset


class solutionCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = solutionCategory.objects.all()
    serializer_class = solutionCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class solutionList(generics.ListCreateAPIView):
    queryset         = solution.objects.all()
    serializer_class = solutionNameOnlySerializer
    # serializer_class = productSerializer
    filter_backends  = [SearchFilter]
    search_fields    = ['solutionName']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = solution.objects.all()
        categoryname  = self.request.query_params.get('categoryName', None)
        if categoryname is not None:
            queryset = queryset.filter(categoryName = categoryname)
        return queryset


class solutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = solution.objects.all()
    serializer_class = solutionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class tileColorList(generics.ListCreateAPIView):
    queryset         = tileColor.objects.all()
    serializer_class = tileColorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class tileColorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = tileColor.objects.all()
    serializer_class = tileColorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
 
class groutColorList(generics.ListCreateAPIView):
    queryset         = groutColors.objects.all()
    serializer_class = groutColorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class groutColorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = groutColors.objects.all()
    serializer_class = groutColorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def searchAll(request):
    query                   = request.GET.get('search')
    productLinequeryset     = productLine.objects.all()
    lineCategoryqueryset    = lineCategory.objects.all()
    productqueryset         = product.objects.all()
    solutionLinequeryset    = solutionLine.objects.all()
    solutionCategoryqueryset= solutionCategory.objects.all()
    solutionqueryset        = solution.objects.all()


    lis = []
    if query is not None:
        # for line in productLinequeryset:
        #     if query.lower() in line.lineName.lower():
        #         list.append({"id":line.lineName,
        #                      "url": 'productLine/'+query})
        pls  = productLinequeryset.filter(lineName__icontains=query)
        lcs  = lineCategoryqueryset.filter(categoryName__icontains=query)
        pss  = productqueryset.filter(productName__icontains= query)
        #sls  = solutionLinequeryset.filter(lineName__icontains=query)
        scs  = solutionCategoryqueryset.filter(categoryName__icontains=query)
        slns  = solutionqueryset.filter(solutionName__icontains=query)
        # prp  = pastProjectsqueryset.filter(projectTitle__icontains=query)
        # grc  = groutqueryset.filter(colorID__icontains=query)

        for pl in pls:
            lis.append({'id':pl.lineName,'place':'productLine', 'uniqueid':'productLine:'+pl.lineName, 'pk':1})
        for lc in lcs:
            lis.append({'id':lc.categoryName,'place':'lineCategory', 'uniqueid':'lineCategory:'+lc.categoryName, 'pk':1})
        for ps in pss:
            lis.append({'id':ps.productName,'place':'product', 'uniqueid':'product:'+ps.productName, 'pk':ps.pk})
        # for pr in prp:
        #     lis.append({'id':pr.projectTitle,'place':'pastProjects', 'uniqueid':'pastProjects:'+pr.projectTitle})
        #for sl in sls:
        #    lis.append({'id':sl.lineName,'place':'solutionLine', 'uniqueid':'solutionLine:'+sl.lineName, 'pk':ps.pk})
        for sc in scs:
            lis.append({'id':sc.categoryName,'place':'solutionCategory', 'uniqueid':'solutionCategory:'+sc.categoryName, 'pk':1})
        for sln in slns:
            lis.append({'id':sln.solutionName,'place':'solution', 'uniqueid':'solution:'+sln.solutionName, 'pk':sln.pk})

    data = json.dumps(lis)  
    # serialized_data = SearchSerializer(lis, many = True)
    return HttpResponse(data, content_type='application/json')
    # return JsonResponse(serialized_data.data, safe=False)

def index(request):
    return render(request, 'index.html')
