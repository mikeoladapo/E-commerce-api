from django.urls import path
from .views import ProductList,ProductDetail,CategoryList,CategoryDetail,ProfileList,ProfileDetail,OrderList,OrderDetail

urlpatterns = [
    path("product",ProductList.as_view(),name="product_list"),
    path("product/<int:pk>",ProductDetail.as_view(),name="product_detail"),
    path("category",CategoryList.as_view(),name="category_list"),
    path("category/<int:pk>",CategoryDetail.as_view(),name="category_detail"),
    path("profile",ProfileList.as_view(),name="profile_list"),
    path("profile/<int:pk>",ProfileDetail.as_view(),name="profile_detail"),
    path("order",OrderList.as_view(),name="order_list"),
    path("order/<int:pk>",OrderDetail.as_view(),name="order_detail")
]