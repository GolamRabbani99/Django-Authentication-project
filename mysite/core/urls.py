from django.urls import path
from. views import HomeView,SignUpView,secret_page,darkroom
urlpatterns = [
 path('',HomeView ,name ='home'),
 path('signup/',SignUpView,name ='signup'),
 path('secret/',secret_page,name ='secret'),
 path('darkroom/',darkroom.as_view(),name ='darkroom')
]