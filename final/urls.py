
from django.urls import path, include
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required
from config import settings

from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name = "index"),
    path('single',single_sweets, name="single_sweet"),
    path('single/<str:single_product_slug>/',single_sweets_detail, name="single_product_link"),
    path('weight',weight_sweets, name="weight_sweet"),
    path('weight/<str:product_slug>',weight_sweets_detail, name="product_link"),
    path('about',about, name="about_company"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)