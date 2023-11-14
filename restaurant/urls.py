from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('bookings', views.bookings, name='bookings'),
    path('api/menu-items/', views.MenuItemsView.as_view()),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/bookings/', views.BookingView.as_view()),
    path('api/bookings/<int:pk>', views.SingleBookingView.as_view()),
    path('api/cart/menu-items/', views.CartView.as_view()),
    path('api/orders/', views.OrderView.as_view()),
    path('api/orders/<int:pk>', views.SingleOrderView.as_view()),
    path('api/groups/manager/users/', views.GroupViewSet.as_view(
        {'get': 'list','post': 'create' })),

    path('api/groups/manager/users/<int:pk>', views.GroupViewSet.as_view(
        {'get': 'retrieve','delete': 'destroy' })),


    path('api/groups/delivery-crew/users/', views.DeliveryCrewViewSet.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'})),

     path('api/groups/delivery-crew/users/<int:pk>', views.DeliveryCrewViewSet.as_view(
        {'get': 'retrieve','delete': 'destroy' })),

]