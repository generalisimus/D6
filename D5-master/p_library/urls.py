from django.contrib import admin
from django.urls import path
from p_library import views
from p_library.views import AuthorEdit, AuthorList  
from p_library import urls

from django.contrib import admin  
from django.urls import include, path  
from p_library.views import AuthorEdit, AuthorList, FriendsEdit, FriendsList 
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from p_library.views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many   


from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many    
from django.contrib import admin  
from django.urls import path  
from .views import AuthorEdit, AuthorList, FriendsEdit, FriendsList

app_name = 'p_library'  
urlpatterns = [  
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),  
    path('author_book/create_many/', author_create_many, name='author_book_create_many'), 
    path('friends/create', FriendsEdit.as_view(), name='friend_form'),  
    path('friends', views.index, name='index'),

]