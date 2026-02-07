from django.db import models
from django.contrib.auth.models import User

# Good - продукт
class Good(models.Model):
    # CharField(max_length = 25)
    # IntegerField()
    # DateField()
    # DateTimeField()
    # FilePathField() - путь до файла
    
    title = models.CharField(max_length = 100) # Название продукта
    price = models.FloatField() # Цена продукта
    description = models.TextField() # Описание продукта
    image = models.ImageField() # Картинка продукта
    quantity = models.IntegerField() # Количество продукта
    expiry_date = models.DateField() # Срок годности

    def __str__(self):
        return f'{self.title}'



