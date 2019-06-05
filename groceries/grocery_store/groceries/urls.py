from django.urls import path

from groceries.views import Grocery_storeList

app_name = 'groceries'

urlpatterns = [
    path('', Grocery_storeList.as_view(), name='index'),
  
    
]  