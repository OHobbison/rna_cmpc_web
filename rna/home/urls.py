from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('aplicar-rna/',views.show_ids,name='aplicar-rna'),
    path('rna-python/',views.show_plots,name='rna-python'),
    path('register/',views.userRegister,name='user-register'),
    path('login/',views.userLogin,name='user-login'),
    path('logout/',views.userLogout,name='user-logout'),
]
