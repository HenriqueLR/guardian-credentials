from django.db import models



class Credentials(models.Model):

	id_credentials = models.AutoField(primary_key=True, verbose_name=u'Credentials', db_column='id_credentials')
	name = models.CharField(max_length=100, verbose_name="Nome", db_column="name")
	url = models.CharField(max_length=100, verbose_name="Url", db_column="url")
	password = models.CharField(max_length=100, verbose_name="Password", db_column="password")
	updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
	created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')
	description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Descricao')

	def __unicode__(self):
		return u'%s' % self.name

	@models.permalink
	def get_edit_credential(self):
		return ('guardian:edit_credentials', [int(self.pk)], {})

	@models.permalink
	def get_absolute_url(self):
		return('guardian:detail_credentials', [int(self.pk)], {})

	@models.permalink
	def get_delete_credential(self):
		return('guardian:delete_credentials', [int(self.pk)], {})

	class Meta:
		verbose_name = 'Credentials'
		verbose_name_plural = 'Credentials'
		ordering=['-created_at']
		db_table='credentials'
		permissions = (
			('add_new_credentials', 'add credentials'),
			('list_new_credentials', 'list credentials'),
			('delete_new_credentials', 'delete credentials'),
			('change_new_credentials', 'change credentials'),
			('detail_new_credentials', 'detail credentials'),
		)