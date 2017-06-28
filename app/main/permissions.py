from django.contrib.auth.decorators import login_required



class PermissionsGeralMixin(object):

    @classmethod
    def as_view(cls):
        return login_required(super(PermissionsGeralMixin, cls).as_view())

    def get_queryset(self):
        qs = self.model.objects.all()

        credential_filter = self.request.GET.get('credential_filter', '')
        if credential_filter != '':
            qs = qs.filter(name__icontains=credential_filter,
            				url__icontains=credential_filter)
        return qs