from django.urls import path
from . import views


urlpatterns = [



    # images

    path('', views.ImageList.as_view(), name="image-list"),
    path('userImage/', views.UserImageList.as_view(),
         name="user-image"),
    # path('delete/<int:pk>/', views.DeleteImage.as_view(), name='delete-image'), # delete image by id
    path('<int:id>/', views.ImageRetrieve.as_view(), name="retrieve-image")





]
