from django.urls import path
from shop.views import healthz
from shop import views
from shop.views import index,detail,checkout,confirmation

urlpatterns=[
    path('',index,name='home'),
    path('<int:myid>',detail,name="detail"),
   path('checkout', checkout, name="checkout"),
  path('confirmation', views.confirmation, name="confirmation")

]
urlpatterns += [
    path("healthz", healthz),
]