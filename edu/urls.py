from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'edu'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('result', views.Result.as_view(), name='result'),
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)