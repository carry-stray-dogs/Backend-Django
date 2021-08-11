# from django.db import models
from djongo import models
from .organization import Organization, OrganizationForm
from django.conf import settings
from djongo.storage import GridFSStorage



class Dog(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    deadline = models.DateField()
    createdAt = models.DateField(auto_now_add=True)
    destination = models.CharField(max_length=100)
    image = models.ImageField(upload_to="dogs", null=True)

    organization = models.EmbeddedField(
        model_container=Organization, model_form_class=OrganizationForm
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
