from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=0)
    image = models.ImageField(upload_to='extra_service_images')
    category = models.ForeignKey(to=ServiceCategory, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'Услуга: {self.name} | Категория: {self.category.name}'
