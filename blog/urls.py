from django.urls import path
from .views import home,blog,detail,post,update,delete

urlpatterns=[
    path('', home, name='home'),
    path('blog', blog.as_view(), name="blog"),
    path('article/<int:pk>', detail.as_view(), name="detail"),
    path('post', post.as_view(), name="post"),
    path('article/edit/<int:pk>', update.as_view(), name="update"),
    path('article/<int:pk>/delete', delete.as_view(), name="delete"),
]