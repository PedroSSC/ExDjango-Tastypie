from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from teste.api.resources import UsuarioResource, EventoResource

v1_api = Api(api_name='v1')
v1_api.register(UsuarioResource())
v1_api.register(EventoResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
]
