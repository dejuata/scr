from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy

from .forms import UserForm, UserUpdateForm


class CreateUser(SuccessMessageMixin, CreateView):
    """
    Create a new user
    """
    model = get_user_model()
    template_name = "users/user_new.html"
    form_class = UserForm
    success_url = reverse_lazy('tenant_login')
    success_message = "Su registro fue exitoso"


class EditUser(UpdateView):
    """
    Edit user data
    """
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = "users/user_edit.html"
    success_url = '/'


class ProfileUserTenant(TemplateView):
    """
    Shows user data
    """
    template_name = "users/user_tenant_profile.html"
    form_class = UserForm
