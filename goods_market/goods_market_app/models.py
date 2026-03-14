from django.db import models
from django.contrib.auth.models import User
from transliterate import translit

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)

# Good - продукт
class Good(models.Model):
    # CharField(max_length = 25)
    # IntegerField()
    # DateField()
    # DateTimeField()
    # FilePathField() - путь до файла

    food_types = (
        ('Фр', 'Фрукты'), 
        ('Ов', 'Овощи'), 
        ('Зел', 'Зелень'), 
        ('Сл', 'Сладкое'), 
        ('Мяс', 'Мясо')
    )

    def user_directory_path(instance, filename):
        title = str(translit(value = instance.title, language_code = 'ru', reversed = True))
        id = str(instance.id)
        return f'goods/{id}_{title}/{filename}'
    
    title = models.CharField(max_length = 100) # Название продукта
    price = models.FloatField() # Цена продукта
    description = models.TextField() # Описание продукта
    image = models.ImageField(default='none', upload_to=user_directory_path) # Картинка продукта
    image2 = models.ImageField(default='none', upload_to=user_directory_path)
    quantity = models.IntegerField() # Количество продукта
    expiry_date = models.DateField() # Срок годности
    food_type = models.CharField(max_length = 100, choices = food_types)

    def __str__(self):
        return f'{self.title}'



