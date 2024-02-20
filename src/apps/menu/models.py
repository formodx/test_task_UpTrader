from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=200)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.name

    def children(self):
        return Menu.objects.filter(parent=self)