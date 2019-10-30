from django.urls import path
from .views import (
index,
signup,signin,signout,
edit_info,
menu,menu_add
)


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/',signin, name='login'),
    path('logout/',signout, name='logout'),
    path('edit/',edit_info, name='edit'),
    path('menu/',menu, name='menu'),
    path('menu/add/',menu_add, name='menu_add'),


]
