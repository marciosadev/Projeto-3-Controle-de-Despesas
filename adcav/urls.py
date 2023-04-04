from django.contrib import admin
from django.urls import path, include
from cadastro.views import home, form, create, view, edit, update, delete, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('cadastro/', include('cadastro.urls'))
    path('', home, name='home'),    
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', profile, name='profile'),
  
]
