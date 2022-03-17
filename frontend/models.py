from django.db import models


class form(models.Model):
    name = models.TextField(null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=15, null=False, unique=True)