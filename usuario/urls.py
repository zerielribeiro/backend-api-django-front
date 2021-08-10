from django.urls import path
from . import views
from .views import UsuarioCreate, Usuarioupdate, UsuarioDelete


urlpatterns = [
   path('', views.UsuarioList, name='list-usuario'),
   path('create/', UsuarioCreate.as_view(), name='create'),
   path('update/<int:pk>/', Usuarioupdate.as_view(),name='update'),
   path('delete/<int:pk>/', UsuarioDelete.as_view(),name='delete'),
  
]