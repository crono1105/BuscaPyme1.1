from app_oracle.views import index
from django.urls import path, include
from .views import about, index,contact, listing, listingdetails, register,agendar


urlpatterns = [
  path('',index,name="index"),
  path('contact/',contact,name="contact"),
  path('about/',about,name="about"),
  path('listing/',listing,name="listing"),
  path('listingdetails/',listingdetails,name="listingdetails"),
  path('register/',register,name="register"),
  path('agendar/',agendar,name="agendar"),




]