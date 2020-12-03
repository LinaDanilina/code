from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('<int:book_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:book_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:book_id>/vote/', views.vote, name='vote'),
    #path('<int:book_id>/', views.book, name='book_by_id'),
]