from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('goods/', GoodsListView.as_view(), name='goods_list'),
    path('new_good/', NewGoodView.as_view(), name='new_good'),
    path('get_token/', TokenView.as_view(), name='get_token'),
]