from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('add_data_db', views.add_data_db, name='add_data_db'),
    # path('<id>', views.checkOutTime, name='checkOutTime'),
]
