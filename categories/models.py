from django.db import models

class Category(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	logo = models.ImageField(upload_to="images/categories", null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name

	@property
	def logo_url(self):
		return f'/media/{self.logo}'
