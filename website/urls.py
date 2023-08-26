from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<item_id>', views.update, name='update'),
    path('table', views.table, name='table'),
    path('updateinfo/<item_id>', views.updateinfo, name='updateinfo'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('addcustomer', views.addcustomer, name='addcustomer'),
    path('deletecustomer/<item_id>', views.deletecustomer, name='deletecustomer'),
]