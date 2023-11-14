

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class booking_Model(models.Model):
    first_name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    reservation_date = models.DateTimeField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self) -> str:
        return self.first_name



class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255,db_index=True)
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = 'Categories'

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    description = models.CharField(max_length=1000, default="")
    featured = models.BooleanField(db_index= True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, default =0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0 )

    class Meta:
        unique_together = ('menuitem', 'user')

    def __str__(self):
        return self.user

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User,on_delete=models.SET_NULL, related_name="delivery_crew",null = True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)

    def __str__(self):
        return f'{self.user} {self.pk}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    menuitem = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menuitem')
