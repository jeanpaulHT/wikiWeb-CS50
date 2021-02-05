from django.urls import path
from . import views
from .util import list_entries


app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:article>/', views.article, name='article'),
    path('search/', views.search, name='search'),
    path('add/', views.add_page, name='add'),
    path('addArticle/', views.addArticle, name='addArticle'),
    path('edit/<str:article>', views.editPage, name='edit'),
    path('editArticle/<str:article>', views.editArticle, name='editArticle'),
    path('randomArticle/', views.getRandom, name='randomArticle')
    
]
