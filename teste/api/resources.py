from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.exceptions import NotFound
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.exceptions import Unauthorized

from teste.models import Evento, Usuario
from django.contrib.auth.models import User


#-------------RESOURCE USUÁRIO-----------------#
class UsuarioResource(ModelResource):
    class Meta:
        queryset = Usuario.objects.all()
        allowed_methods = ['get','post', 'delete','put']
        aways_return_data = True
        authentication = ApiKeyAuthentication()
        filtering = {
            "Name": ('exact', 'startswith',)
        }

    def obj_create(self, bundle, **kwargs):
        print(bundle)
        if not(Usuario.objects.filter(username = bundle.data['username'])):
            user = Usuario()
            user.username = bundle.data['username']
            user.mail = bundle.data['mail']
            user.password = bundle.data['password']
            user.tipo = bundle.data['tipo']
            user.save()
            bundle.obj = user
            return bundle
        else:
            raise Unauthorized('Já existe Usuário com esse nome.')

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Não permitido.')

#-------------RESOURCE EVENTO-----------------#
class EventoResource(ModelResource):
    class Meta:
        queryset = Evento.objects.all()
        allowed_methods = ['get','post', 'delete','put']
        aways_return_data = True
        authentication = ApiKeyAuthentication()
        filtering = {
            "nome": ('exact', 'startswith',)
        }

    def obj_create(self, bundle, **kwargs):
        usuario = bundle.request.user
        nome = bundle.data['nome']
        evento = Evento()
        evento.administrador = Usuario.objects.get(pk=usuario.pk)
        evento.nome = nome
        evento.save()
        bundle.objeto = evento

    def obj_delete(self, bundle, **kwargs):
        evento = Evento.objects.get(pk=kwargs['pk'])
        admEvento = Usuario.objects.get(username=evento.administrador)
        solicitante = bundle.request.user
        if(admEvento.pk == solicitante.pk):
                evento.delete()
                bundle.obj = evento
        else:
            raise Unauthorized('Apenas o Administrador pode excluir este Evento.')

    def obj_delete_list(self, bundle, **kwargs):
        raise Unauthorized('Não permitido.')
