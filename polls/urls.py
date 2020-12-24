from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.cl, name='clients'),
    path('admin/', admin.site.urls),
    path('<int:product_id>/', views.detail, name='detail'),
    path('clients/<int:client_id>/', views.detail_cl, name='detail_cl'),

]