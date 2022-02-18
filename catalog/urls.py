# Django
from django.urls import path, re_path, include

# View 
from . import views


urlpatterns = [
    # index
    re_path(r'^$', views.index, name='index'),
    
    # signup
    path('signup/', views.SignupView.as_view(), name='signup'),
    
    # book 
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),  

    # author
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),       
    
    #
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    
    #
    path('book/<uuid:pk>/renew/', views.renew_book_librarian , name='renew-book-librarian'),
 
]

    # path(
    #     route='signup/',
    #     view=views.SignupView.as_view(),
    #     name='signup'
    # ),

# Add URLConf to create, update, and delete authors
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]


# Add URLConf to create, update, and delete books
urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

