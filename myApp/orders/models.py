from django.db import models

# Create your models here.
class orderTable(models.Model) :
    # id = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=200)
    productCount = models.IntegerField(default=1)
    # testInt = models.IntegerField(default=5)

    def __str__(self) :
        return self.productName