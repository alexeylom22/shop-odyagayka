from django.db import models
from django.utils import timezone
from django.urls import reverse
# from django.contrib.auth.models import User
# from PIL import Image

ITEM_CHOICES = (
    ('F', 'Футболка'),
    ('SC', 'Спортивний костюм'),
    ('K','Кофта'),
    ('Ш', 'Штани'),
)

class Items(models.Model):

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')
    item = models.CharField(
        "Тип товару",
        max_length=2,
        choices=ITEM_CHOICES,
        default='SC'
        )
    name = models.CharField("Назва товару", max_length=300)
    description = models.TextField("Опис товару", max_length=300)
    sizes = models.CharField("Розміри( наприклад 'S-3XL')", max_length=300)
    price = models.DecimalField("Ціна", max_digits=7, decimal_places=2)
    discount = models.IntegerField("Знижка(якщо є)", default=0)
    new_price = models.DecimalField("Ціна зі знижкою", max_digits=7, decimal_places=2)
    date = models.DateTimeField('Дата', default=timezone.now)
    def __str__(self):
        return f'Профайл пользователя {self.item}'

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Товари'
        verbose_name_plural = 'Товари'

    def save(self, *args, **kwargs):
        if self.price and self.discount:
            self.new_price = (self.price * (100 - self.discount))/100
        if self.sizes:
            size_offset = ['XS', 'S', 'M', 'L', 'XL', '2XL', '3XL', '4XL', '5XL', '6XLl', '7XL']
            text=self.sizes.upper().split('-')
            self.sizes = ''
            if "X" in text[1]:
                qty_x = text[1].count('X')
                if qty_x > 1:
                    text[1] = str(qty_x) + 'XL'

            if text[0] in size_offset and text[1] in size_offset:
                start = size_offset.index(text[0])
                end = size_offset.index(text[1]) + 1
                sizes_os = size_offset[start:end]
                for i in sizes_os:
                    self.sizes = self.sizes + str(i.upper()) + " "
            else:
                for i in range(int(text[0]), int(text[1]) + 1):
                    self.sizes = self.sizes + str(i.upper()) + " "
        super(Items, self).save(*args, **kwargs)


