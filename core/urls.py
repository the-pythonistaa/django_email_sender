from django.urls import path
from core.views import index, send
app_name = 'core'
urlpatterns  = [
    path('', index, name='index'),
    path('send', send, name='send')
]