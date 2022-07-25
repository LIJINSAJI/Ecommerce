from django.urls import path
from .import views
app_name='shopapp'
urlpatterns = [
    path('', views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='products_by_catagory'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='prodcatdetail'),

]