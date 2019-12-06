from django.db import models
from django.urls import reverse


class Information(models.Model):
    visitor_name = models.CharField(max_length=30)
    visitor_email = models.EmailField(max_length=254)
    visitor_number = models.CharField(max_length=16)

    host_name = models.CharField(max_length=30)
    host_email = models.EmailField(max_length=254)
    host_number = models.CharField(max_length=16)

    check_in = models.TimeField(auto_now_add=True)
    check_out = models.TimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('home_page', kwargs={'id': self.id})

    def __str__(self):
        return self.visitor_name
