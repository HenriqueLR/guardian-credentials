from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from guardian.models import Credentials
from guardian.permissions import PermissionsGeralMixin
from guardian.forms import CredentialsForm



class CredentialsDeleteView(PermissionsGeralMixin, DeleteView):

	model = Credentials
	template_name = 'guardian/delete_credentials.html'
	success_url = reverse_lazy('main:home')

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, 'credentials remove success')
		return super(CredentialsDeleteView, self).delete(request, *args, **kwargs)



class CredentialsDetailView(PermissionsGeralMixin, DetailView):

	model = Credentials
	template_name = 'guardian/detail_credentials.html'



class CredentialsUpdateView(PermissionsGeralMixin, UpdateView):

	model = Credentials
	form_class = CredentialsForm
	template_name = 'guardian/edit_credentials.html'


	def form_valid(self, form):
		messages.success(self.request, 'credentials edit success')
		return super(CredentialsUpdateView, self).form_valid(form)



class CredentialsAddView(PermissionsGeralMixin, CreateView):

	model = Credentials
	form_class = CredentialsForm
	template_name = 'guardian/add_credentials.html'
	success_url = reverse_lazy('guardian:add_credentials')

	def form_valid(self, form):
		messages.success(self.request, 'credentials add success')
		return super(CredentialsAddView, self).form_valid(form)



delete_credentials = CredentialsDeleteView.as_view()
detail_credentials = CredentialsDetailView.as_view()
edit_credentials = CredentialsUpdateView.as_view()
add_credentials = CredentialsAddView.as_view()