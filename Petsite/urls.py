"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from pets import views
from pets.views import PetsList, PetDetail, ContactsView, AddPet, NewsList, TextView

app_name = 'pets'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PetsList.as_view(), name='pets_list'),
    path('pets/', PetsList.as_view(), name='pets_list'),
    path('<int:pk>-<slug:slug>', PetDetail.as_view(), name='pets_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('add/',  AddPet.as_view(), name='pet_add'),
    path('news/', NewsList.as_view(), name='news'),
    path('news/<int:pk>', TextView.as_view(), name='expand'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)