"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weDeliver import views
from ecom import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('admlog/',views.adlog,name='adlog'),
    path('admincheck/',views.adchk,name='admin_home'),
    path('adminhome/',views.adminhome,name='admin'),
    path('addprod/',views.addprod,name='add_prod'),
    path('prods/',views.prods, name='prods'),
    path('user_reg/',views.reg,name ='userreg'),
    path('regis/',views.regis,name='register'),
    path('userlog/',views.uslog,name='uslog'),
    path('uservalid/',views.userchk,name='userchk'),
    path('home/',views.userhome,name='userhome'),
    path('allprods/',views.allprods,name='allprods'),
    path('update/',views.update,name='update'),
    path('change/',views.upprod,name='new'),
    path('userlogem/',views.uslogem,name='uslogem'),
    path('userem/',views.userchkem,name='userchkem'),
    path('delprod/',views.delprod,name='delete'),
    path('approve/',views.appruser,name='approve'),
    path('apprdlcnd/',views.apprdlcnd,name='apprdlcnd'),
    path('decluser/',views.declineuser,name='declineuser'),
    path('showpndng/',views.showpndng,name='showpndg'),
    path('showapprd/',views.showapprd,name='showapprd'),
    path('showdclnd/',views.dclndusers,name='showdclnd'),
    path('deleteuser/',views.deletedecuser,name='deleteuser'),
    path('delappuser/',views.delappuser,name='delappuser'),
    path('deletepndng/',views.delpdnguser,name='delpdnguser'),
    path('cart/',views.cart,name='cart'),
    path('cartitems',views.cartitems,name='cartitems'),
    path('delcart/',views.delcart,name='delcart'),
    path('usercart/',views.usercart,name='usercart'),
    path('useritems/',views.useritems,name='useritems'),
    path('delusercart/',views.delusercart,name='delusercart'),
    path('otppage/',views.otppage,name='otppage'),
    path('otpvalidate/',views.otpvalidate,name='otpvalidate')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

