from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('test/', get_test, name='test'),
    path('cats/<int:number>', cats, name='categ'),
    path('info/<str:name>/<int:age>/', info)
]