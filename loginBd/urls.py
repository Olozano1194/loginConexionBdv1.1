from django.urls import path
from .views import Login, welcome, singoff, formcheckin, home, delete_user, update_user, actualizar



urlpatterns = [
    path('', Login, name='login'),
    path('checkin/', formcheckin, name='checkin'),
    path('welcome/', welcome, name='welcome'),
    path('logout/', singoff, name='logout'),
    path('read/', home, name='read'),
    path('update/<int:id>', update_user, name='update'),
    path('updateUsers/<int:id>', actualizar, name='updateUsers'),
    path('delete/<int:id>', delete_user, name='delete'),
]
