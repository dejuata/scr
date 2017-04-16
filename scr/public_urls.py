from django.conf.urls import url, include
<<<<<<< HEAD
# from django.contrib import admin
from apps.tenant.admin import admin_site
=======
>>>>>>> usuarios
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.conf import settings

from apps.tenant.views import TenantCreateView
from apps.tenant.admin import admin_site

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="landing/index.html"), name='index'),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
<<<<<<< HEAD
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', include(admin_site.urls)),
=======
>>>>>>> usuarios

    url(r'^admin/', include(admin_site.urls)),

    url(r'^login/', login, {'template_name': 'users/tenant_login.html'}, name='tenant_login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^accounts/login/', login, {'template_name': 'users/tenant_login.html'}, name='tenant_login'),

    url(r'^', include('apps.users.urls_tenant', namespace='usuario')),
    url(r'^registrar-empresa/$', login_required(TenantCreateView.as_view()), name='registrar-empresa'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
