from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_store, name='create_store'), # store 앱 url 연결
    path('home/', views.view_store, name='home'),
    # 우리가 파리바게트 판매자를 기준으로 홈화면 띄우기로 했어서 이렇게 함
    path('list', views.list_store, name="list_store"), # 가게 목록
    path('create/<int:pk>/product', views.create_product, name="create_product"),
    path('<int:pk>/product/list', views.list_product, name="list_product"),
    path('<int:pk>/purchase/list', views.list_purchase, name='list_purchase'),
    path('<int:pk>/order/<int:order_id>/update-status', views.order_update, name="order_update"),
]