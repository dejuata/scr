from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django_tenants.utils import tenant_context

from .models import Tenant, Domain
from .forms import TenantForm


def create_admin_tenant(tenant, user_id):
    user = get_user_model().objects.get(pk=user_id)
    tenant = Tenant(schema_name=tenant)

    with tenant_context(tenant):
        get_user_model().objects.create_superuser(username=user.username, password='123', email=user.email, first_name=user.first_name, last_name=user.last_name)


class TenantCreateView(CreateView):
    model = Tenant
    form_class = TenantForm
    template_name = 'tenant/tenant_form.html'
    success_url = '/'

    def form_valid(self, form):
        tenant_registrado = form.instance
        tenant_registrado.schema_name = tenant_registrado.nombre_comercial
        self.object = form.save()
        dominio_tenant = Domain(domain=self.object.nombre_comercial + '.localhost',
                                is_primary=True,
                                tenant=tenant_registrado
                                )
        dominio_tenant.save()

        # url redirect
        url = 'http://' + tenant_registrado.nombre_comercial + '.localhost:8000/admin'

        # create superuser in the new schema_name
        user_id = tenant_registrado.user_id
        tenant = tenant_registrado.nombre_comercial

        super(TenantCreateView, self).form_valid(form)
        create_admin_tenant(tenant, user_id)
        return redirect(url)
