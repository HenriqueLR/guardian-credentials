from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.permissions import PermissionsGeralMixin
from django.views.generic.list import ListView
from guardian.models import Credentials



class CredentialsListView(PermissionsGeralMixin, ListView):

	model = Credentials
	paginate_by = 12
	template_name = 'main/home.html'


home = CredentialsListView.as_view()