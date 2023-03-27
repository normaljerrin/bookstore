from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import BookListView, BookDetailView, BookCheckoutView, BookLoginView, BookRegisterView, SearchResultsView, \
    PaymentComplete

urlpatterns = [
    path('book_list', BookListView.as_view(),name='list'),
    path('detail/<int:pk>/', BookDetailView.as_view(),name='detail-view'),
    path('checkout/<int:pk>/', BookCheckoutView.as_view(),name='checkout-view'),
    path('login', BookLoginView.as_view(),name='loggin'),
    path('register', BookRegisterView.as_view(),name='reggister'),
    path('complete', PaymentComplete,name='complete'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('search',SearchResultsView.as_view(),name='search'),
    path('',views.home_fun,name='home'),
    ]