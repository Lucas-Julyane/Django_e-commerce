from django.urls import path

from mysite.settings import MEDIA_ROOT
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('register_pag',views.register_pag,name='register_pag'),
    path('login_pag',views.signin_pag,name='signin_pag'),
    path('cart_pag',views.cart_pag,name='cart_pag'),
    path('checkout_pag',views.checkout_pag,name='checkout_pag')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)