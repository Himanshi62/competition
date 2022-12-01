from django.urls import path,include
from . import views

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('logiq', views.logiq, name="logiq"),
    path('accounts/', include('allauth.urls')),
    path('register-logiq', views.registerLogiq, name="registerLogiq"),
    path('submitted', views.submitted, name="submitted"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)