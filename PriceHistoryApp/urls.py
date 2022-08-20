from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#In python,'/' will be written in the end of the prefix
#In HTML, '/' will be written in the beginning of the prefix
urlpatterns = [
        path('login/', views.login, name='login'),
        path('register/', views.register, name='register'),
        path('register/registeruser', views.registeruser, name='registeruser'),
        
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
