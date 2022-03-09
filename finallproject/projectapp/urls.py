from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('blog', views.blog, name="blog"),
    path('cart', views.cart, name="cart"),
    path('product/<int:id>', views.product, name='product'),
    path('category', views.category, name="category"),
    path('contact', views.contact, name="contact"),
    path('create_product', views.create_product, name="create_product"),
    path('update_product/<str:pk>', views.update_product, name="update_product"),
    path('delete_product/<str:pk>', views.delete_product, name="delete_product"),
    path('login', views.login_user, name="login"),
    path('register', views.registerPage, name="register"),
    path('profile/<str:pk_test>', views.profile, name="profile"),
    path('logout', views.logout_user, name="logout"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('fav/<int:id>', views.favorite_add, name='favorite_add'),
    path('favorites', views.favorite_list, name='favorite_list'),
]
