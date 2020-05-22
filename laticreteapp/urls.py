from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from laticreteapp import views
from django.views.generic import TemplateView
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name= 'HomePage'),
    path('laticreteapp/productLine/', views.productLineList.as_view(), name= 'productLineList'),
    path('laticreteapp/lineCategory/', views.lineCategoryList.as_view(), name= 'lineCategoryList'),
    path('laticreteapp/product/', views.productList.as_view(), name = 'productList'),
    path('laticreteapp/groutColor/', views.groutColorList.as_view(), name = 'groutColorList'),
    path('laticreteapp/pastProject/', views.pastProjectsList.as_view(), name = 'pastProjectsList'),
    path('laticreteapp/tileColor/', views.tileColorList.as_view(), name = 'tileColorList'),

    path('laticreteapp/productLine/<path:pk>/', views.productLineDetail.as_view(), name= 'productLineDetail'),
    path('laticreteapp/lineCategory/<path:pk>/', views.lineCategoryDetail.as_view(), name= 'lineCategoryDetail'),
    path('laticreteapp/product/<path:pk>/', views.productDetail.as_view(),name= 'productDetail'),
    path('laticreteapp/groutColor/<path:colorName>/', views.groutColorDetail.as_view(), name= 'groutColorDetail'),
    path('laticreteapp/pastProject/<path:pk>/', views.pastProjectsDetail.as_view(), name= 'pastProjectDetail'),
    path('laticreteapp/tileColor/<path:colorName>/', views.groutColorDetail.as_view(), name= 'groutColorDetail'),
    

    path('laticreteapp/solutionLine/', views.solutionLineList.as_view(), name= 'solutionLineList'),
    path('laticreteapp/solutionCategory/', views.solutionCategoryList.as_view(), name= 'solutionCategoryList'),
    path('laticreteapp/solution/', views.solutionList.as_view(), name = 'solutionList'),    
    path('laticreteapp/solutionLine/<path:pk>/', views.solutionLineDetail.as_view(), name= 'solutionLineDetail'),
    path('laticreteapp/solutionCategory/<path:pk>/', views.solutionCategoryDetail.as_view(), name= 'solutionCategoryDetail'),
    path('laticreteapp/solution/<int:pk>/', views.solutionDetail.as_view(), name= 'solutionDetail'),



    path('laticreteapp/search/', views.searchAll, name="Search"),

    path('laticreteapp/wheretobuy/', views.whereToBuyList.as_view(), name='whereToBuy'),
    path('laticreteapp/downloads/', views.DownloadList.as_view(), name = 'downloads'),
    path('laticreteapp/applicationvideo/', views.applicationVideosList.as_view(), name = 'applicationvideo'),
    path('laticreteapp/carousel/', views.carouselList.as_view(), name = 'carousel'),
    path('laticreteapp/feedback/', views.feedbackList.as_view(), name = 'feedback'),
    path('laticreteapp/allcarousel/', views.allcarouselList.as_view(), name = 'allcarousel'),
    path('laticreteapp/addfeedback/', views.addFeedback, name='addfeedback'),

    path('laticreteapp/downloads/<str:pk>/',views.DownloadsDetail.as_view(), name= 'DownloadsDetail'),
    path('laticreteapp/applicationvideo/<str:pk>/',views.applicationVideosDetail.as_view(), name= 'applicationVideoDetail'),

    # static(settings.MEDIA_URL, document_root = settings.M)
] 
