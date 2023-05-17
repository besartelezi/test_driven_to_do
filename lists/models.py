from django.db import models
from django.core.urlresolvers import reverse

class List(models.Model):
    # list = models.TextField(default='')
    def get_absolute_url(self):
        return reverse("view_list", args=[self.id])


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('id',)
        # Sets of field names that, taken together, must be unique
        unique_together = ('list', 'text')