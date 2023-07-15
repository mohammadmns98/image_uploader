from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserList.as_view(),
         name="user-list"),                  # show all users
     path('create/',views.CreateUser.as_view(),name="create-user"),
     path('<int:id>/',views.RetrieveUser.as_view(),name="user-by-id")

]
