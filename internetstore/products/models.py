from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=150)

    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)

    image = models.ImageField()

    content = models.TextField()

    cost = models.DecimalField(max_digits=7, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return '-'.join((self.name, str(self.cost,), str(self.created)))