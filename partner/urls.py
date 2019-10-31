from django.urls import path
from .views import (
index,
signup,signin,signout,
edit_info,
menu,menu_add,menu_detail,menu_edit,menu_delete
)


urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/',signin, name='login'),
    path('logout/',signout, name='logout'),
    path('edit/',edit_info, name='edit'),
    path('menu/',menu, name='menu'),
    path('menu/<int:menu_id>/',menu_detail, name='menu_detail'),
    path('menu/<int:menu_id>/edit/',menu_edit, name='menu_edit'),
    path('menu/add/',menu_add, name='menu_add'),
    path('menu/<int:menu_id>/delete',menu_delete, name='menu_delete'),
]
