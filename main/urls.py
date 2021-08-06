from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowItemsView.as_view(), name ='home'),
    path('add-item', views.create_item.as_view(), name='create_item'),
    path('<int:pk>', views.ItemsDetailView.as_view(), name='item-detail'),
    path('<int:pk>/buy', views.ItemsBuyDetailView.as_view(), name='item-buy'),
    path('<int:pk>/delete', views.ItemsDeleteView.as_view(), name='item-delete'),
    path('<int:pk>/order', views.ItemsOrderView.as_view(), name='item-order'),
]
