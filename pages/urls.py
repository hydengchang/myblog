from django.urls import path
from pages.views import index, vlist, about, copyright, message, search,detail


app_name = 'pages'
urlpatterns = [
    path('',index, name="index"),
    path('article/', vlist, name='vlist'),
    path('article/<int:article_id>', detail, name="detail"),
    path('copyright/', copyright, name="copyright"),
    path('about/', about, name='about'),
    path('message/', message, name="message"),
    path('search/', search, name="search")
]